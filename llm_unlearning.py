import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModel, AutoTokenizer

class LLMUnlearning:
    def __init__(self, model_name):
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def gradient_based_unlearning(self, data_to_unlearn, learning_rate=1e-5):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

    def knowledge_distillation(self, teacher_model_name, data_to_unlearn, learning_rate=1e-5):
        teacher_model = AutoModel.from_pretrained(teacher_model_name)
        teacher_model.eval()
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        criterion = nn.KLDivLoss(reduction='batchmean')

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            with torch.no_grad():
                teacher_outputs = teacher_model(**inputs)
            student_outputs = self.model(**inputs)
            loss = criterion(student_outputs.logits, teacher_outputs.logits)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    def selective_fine_tuning(self, fine_tuning_data, learning_rate=1e-5):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        criterion = nn.CrossEntropyLoss()

        for data in fine_tuning_data:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

    def parameter_pruning(self, data_to_unlearn, pruning_percentage=0.1):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=1e-5)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        total_params = sum(p.numel() for p in self.model.parameters())
        params_to_prune = int(total_params * pruning_percentage)
        all_params = [(name, p) for name, p in self.model.named_parameters() if p.requires_grad]
        all_params.sort(key=lambda x: x[1].abs().sum().item(), reverse=True)

        for name, param in all_params[:params_to_prune]:
            param.data.zero_()

    def embedding_adjustment(self, data_to_unlearn, adjustment_factor=0.1):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=1e-5)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        for name, param in self.model.named_parameters():
            if 'embedding' in name:
                param.data.mul_(adjustment_factor)

    def embedding_noise_injection(self, data_to_unlearn, noise_level=0.1):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=1e-5)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        for name, param in self.model.named_parameters():
            if 'embedding' in name:
                noise = torch.randn_like(param) * noise_level
                param.data.add_(noise)

    def embedding_replacement(self, data_to_unlearn, replacement_value=0.0):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=1e-5)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        for name, param in self.model.named_parameters():
            if 'embedding' in name:
                param.data.fill_(replacement_value)

    def embedding_masking(self, data_to_unlearn, mask_value=0.0):
        self.model.train()
        optimizer = optim.Adam(self.model.parameters(), lr=1e-5)
        criterion = nn.CrossEntropyLoss()

        for data in data_to_unlearn:
            inputs = self.tokenizer(data['text'], return_tensors='pt')
            labels = torch.tensor(data['labels']).unsqueeze(0)
            optimizer.zero_grad()
            outputs = self.model(**inputs)
            loss = criterion(outputs.logits, labels)
            loss.backward()
            optimizer.step()

        for name, param in self.model.named_parameters():
            if 'embedding' in name:
                param.data.masked_fill_(param.data != 0, mask_value)
