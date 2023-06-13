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

    keys = user_msg.split('/')

    if(len(keys)==3):
        text = ''
        result = bt.getNotas(keys[0], keys[1], keys[2])
        for i in result:
            text = text + str(i)
        send(text, number)
        return jsonify({'message': 'Success'})
    else:
        return jsonify({'message': 'Faliure'})   

    

  
if __name__ == "__main__":
    app.run()
    
