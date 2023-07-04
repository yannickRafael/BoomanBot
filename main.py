from flask import Flask, request, jsonify
import getMarksBot as bt
from twilio.rest import Client
#1

def getContent(tabela):
    retorno = ' '
    for linha in tabela:
        for elemento in linha:
            retorno = retorno+' '+elemento
        retorno = retorno + "\n"+"========================================================================================================"+"\n"
    
    return retorno
 

def send(message, number):
    account_sid = 'ACa5c83e45677a24409033440f8499727b'
    auth_token = 'c1b4fb1c0d36280276b9f8a0b6a68cf2'
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
    print('bot() iniciado')
    # user input
    user_msg = request.values.get('Body', '')
    number = request.form.get('From')
    print(user_msg)
    send('Comando recebido, buscando notas', number) 

    keys = user_msg.split('/')

    if(len(keys)==3):

        primeira_linha, linhas_encontradas, ultima_linha = bt.getNotas(keys[0], keys[1], keys[2])

        ans = []
        for i in range(0, len(linhas_encontradas)):
            if i >= 2:
                text = linhas_encontradas[i] + ': ' + primeira_linha[i] + '/' + ultima_linha[i - 1]
                ans.append(text)
            if i < 2:
                text = linhas_encontradas[i] + ': ' + primeira_linha[i]
                ans.append(text)

        text = ""
        for i in ans:
            text = text + i + '\n'


        if(len(linhas_encontradas)==0):
            send("Estudante nao encontrado", number)
        else:
            send(text, number)
        return jsonify({'message': 'Success'})
    else:
        return jsonify({'message': 'Faliure'})   

    

  
if __name__ == "__main__":
    app.run()
    print('main() iniciado')
    
