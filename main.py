from flask import Flask, request
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
 

def send(message):
    account_sid = 'ACa5c83e45677a24409033440f8499727b'
    auth_token = 'fc4ab831440341e82ea9a49cdef7e15d'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=message,
    to='whatsapp:+258844236139'
    )
  
app = Flask(__name__)
  
@app.route("/", methods=["POST"])
  
# chatbot logic
def bot():
  
    # user input
    user_msg = request.values.get('Body', '')
    print(user_msg)
  
   

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

        send(getContent(tab1))
        send(getContent(tab2))
        send(getContent(tab3))
        send(getContent(tab4))


  
if __name__ == "__main__":
    app.run()
    