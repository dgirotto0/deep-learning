import torch
import torch.nn as nn # 

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)  # define a primeira camada
        self.l2 = nn.Linear(hidden_size, hidden_size) # define a segunda camada
        self.l3 = nn.Linear(hidden_size, num_classes) # define a camada de saída
        self.relu = nn.ReLU() # define a função de ativação ReLu

    def forward(self, x):
        out = self.l1(x) # Aplica a primeira camada linear
        out = self.relu(out) # aplica a função ReLU
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        
        # no activation and no softmax at the end
        return out