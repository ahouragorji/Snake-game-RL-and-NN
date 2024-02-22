import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence


class QNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(QNetwork,self).__init__()

        self.fc1 = nn.Linear(in_features=input_dim,out_features=hidden_dim)
        self.fc2 = nn.Linear(in_features=hidden_dim,out_features=hidden_dim)
        self.fc3 = nn.Linear(in_features=hidden_dim,out_features=hidden_dim)
        self.fc4 = nn.Linear(in_features=hidden_dim,out_features=output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        if x.dtype != self.fc1.weight.dtype:
            x = x.to(self.fc1.weight.dtype)
        l1 = self.relu(self.fc1(x))
        l2 = self.relu(self.fc2(l1))
        l3 = self.relu(self.fc3(l2))
        l4 = self.fc4(l3)
        return l4


def get_network_input(player, apple):
    proximity = player.get_proximity()
    x = torch.cat([torch.from_numpy(player.pos).double(), torch.from_numpy(apple.pos).double(),
                   torch.from_numpy(player.dir).double(), torch.tensor(proximity).double()])
    return x
