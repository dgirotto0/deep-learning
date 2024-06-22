import json
import random
import torch
import numpy as np
from nltk_utils import tokenize, bag_of_words
from model import NeuralNet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') # define o dispositivo de execução

with open('intents.json', 'r', encoding='utf-8') as json_data: # abre o json em modo de leitura
    intents = json.load(json_data)

FILE = "data.pth" 
data = torch.load(FILE) # carrega os dados do modelo treinado

input_size = data["input_size"] # obtém tamanho da entrada
hidden_size = data["hidden_size"] # tamanho de camadas ocultas (?)
output_size = data["output_size"] # tamanho da camada de saída 
all_words = data['all_words'] # todas as palavras do vocabulario
tags = data['tags'] # lista de tags
model_state = data["model_state"] 

model = NeuralNet(input_size, hidden_size, output_size).to(device) # cria uma instância do modelo NeuralNet no dispositivo definido
model.load_state_dict(model_state)
model.eval()

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model(X) # realiza a inferência da rede neural
    _, predicted = torch.max(output, dim=1) # encontra o índice da classe mais provável
    tag = tags[predicted.item()] # obtem a tag da classe mais provável

    probs = torch.softmax(output, dim=1) # calcula a probabilidade de cada classe
    prob = probs[0][predicted.item()] # obtem a probabilidade da classe mais provável

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses']) # retorna uma resposta aleatória da lista de respostas 
    
    return "Desculpe, não entendi sua pergunta. Pode reformular?"
