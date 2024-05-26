import torch
from torch import autograd
import numpy as np

class EWC:
    def __init__(self, model, dataloader, device):
        self.model = model
        self.dataloader = dataloader
        self.device = device
        self.params = {n: p for n, p in self.model.named_parameters() if p.requires_grad}
        self._precision_matrices = self._compute_fisher()
        for n, p in self.params.items():
            self.params[n] = p.clone().detach()

    def _compute_fisher(self):
        precision_matrices = {n: torch.zeros_like(p) for n, p in self.params.items()}
        self.model.eval()
        for input, target in self.dataloader:
            input, target = input.to(self.device), target.to(self.device)
            self.model.zero_grad()
            output = self.model(input).log()
            loss = torch.nn.functional.nll_loss(output, target)
            loss.backward()
            for n, p in self.model.named_parameters():
                if p.grad is not None:
                    precision_matrices[n].data += p.grad.data ** 2 / len(self.dataloader)

        precision_matrices = {n: p for n, p in precision_matrices.items()}
        return precision_matrices

    def penalty(self, model):
        loss = 0
        for n, p in model.named_parameters():
            _loss = self._precision_matrices[n] * (p - self.params[n]) ** 2
            loss += _loss.sum()
        return loss
