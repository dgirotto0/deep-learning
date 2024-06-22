import os
from flask import Flask, request # para criar um servidor web que aceita requisições HTTP
from twilio.twiml.messaging_response import MessagingResponse
from chat import get_response
from dotenv import load_dotenv

# carrega variáveis de ambiente do .env
load_dotenv()

app = Flask(__name__)

# define rota para receber mensagens do WhatsApp via POST
@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    # extrai mensagem recebida
    incoming_msg = request.values.get('Body', '').strip() # pega a mensagem da requisição, limpando espaçoes em branco
    app.logger.info(f"Incoming message: {incoming_msg}")

    # obtém resposta do chatbot
    response = get_response(incoming_msg)
    app.logger.info(f"Response: {response}")
    
    # crias as respostas usando a twilio
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response)
    
    # retorna a resposta formatada 
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
