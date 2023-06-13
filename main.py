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
    auth_token = '4fa8e282d88e547c2b171857a31e1196'
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
        result = bt.getNotas(keys[0].strip(), keys[1].strip(), keys[2].strip())
        print(keys[0])
        print(keys[1])
        print(keys[2])
        if(len(result)==0):
            send("Estudante nao encontrado", number)
        else:
            print(len(result))
            for i in result:
                text = text + str(i)+"\n"
            send(text, number)
        return jsonify({'message': 'Success'})
    else:
        return jsonify({'message': 'Faliure'})   

    

  
if __name__ == "__main__":
    app.run()
    
