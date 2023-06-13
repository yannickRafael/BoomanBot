from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import getMarksBot as bt
from twilio.rest import Client


def getContent(tabela):
    retorno = ' '
    for linha in tabela:
        for elemento in linha:
            retorno = retorno+' '+elemento
        retorno = retorno + "\n"+"========================================================================================================"+"\n"
    
    return retorno
 

def send(message, number):
    account_sid = 'ACa5c83e45677a24409033440f8499727b'
    auth_token = '4fe2c205a0bb3e88c24302af80b4057a'
    client = Client(account_sid, auth_token)	
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=message,
    to=number
    )
  
app = Flask(__name__)
  
@app.route("/", methods=["POST"])
  
# chatbot logic
def bot():
    # user input
    user_msg = request.values.get('Body', '')
    number = request.form.get('From')
    print(user_msg)
    send('Comando recebido, buscando notas', number) 
   

    if user_msg == 'getNotas':
        tabela = bt.getNotas()
        tamanho = len(tabela)
        meio1 = tamanho // 4
        meio2 = meio1 * 2
        meio3 = meio1 * 3
        tab1 = tabela[:meio1]
        tab2 = tabela[meio1:meio2]
        tab3 = tabela[meio2:meio3]
        tab4 = tabela[meio3:]

        send(getContent(tab1), number)
        send(getContent(tab2), number)
        send(getContent(tab3), number)
        send(getContent(tab4), number)
    return jsonify({'message': 'Success'})

  
if __name__ == "__main__":
    app.run()
    
