import torch
from torch.utils.data import Dataset
import numpy

class SeqsData(Dataset):
    def __init__(self, seqs):
        seqs = numpy.transpose(seqs)
        tensor_seqs = list(torch.tensor(seq[1]).float() for seq in seqs)
        tensor_labels = list(torch.tensor(seqs[0]).long() for seqs in seqs)
        self.data = torch.stack(tensor_seqs)
        self.labels= torch.stack(tensor_labels)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, id):
        data=self.data[id]
        labels=self.labels[id]

        return data, labels


