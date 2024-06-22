from flask import Flask, request, jsonify # A função jsonify do Flask permite converter dados  
from chat import get_response             # Python em formato JSON, facilitando a comunicação com a API.

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json.get('message')
    response = get_response(message)

    # retorna a resposta como json
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
