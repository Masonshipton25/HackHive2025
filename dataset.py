# dataset.py
# Mason Shipton, Lukas Fenkam, Rayan Alam, Christopher Kiige
# Description: Loads dataset and tokenizes the sentences.
# Date Created: 2025-02-08.
# Date Last Revised: 2025-02-08.

import torch

class IndigenousDataset(torch.utils.data.Dataset):
    def __init__(self, data_path, tokenizer, max_length=128):
        """
        Initializes the dataset by loading and tokenizing the data.
        
        Parameters:
        - data_path: Path to the dataset file (text file).
        - tokenizer: Tokenizer used for tokenizing the sentences.
        - max_length: Maximum token length (default: 128).
        """
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.texts = self.load_data(data_path)
        self.encodings = self.tokenize()

    def load_data(self, data_path):
        """Loads the dataset from the provided text file."""
        with open(data_path, 'r') as file:
            texts = file.readlines()
        return [text.strip() for text in texts]

    def tokenize(self):
        """Tokenizes all sentences in the dataset."""
        return self.tokenizer(self.texts, padding=True, truncation=True, return_tensors="pt", max_length=self.max_length)
    
    def __len__(self):
        """Returns the size of the dataset."""
        return len(self.texts)

    def __getitem__(self, idx):
        """Gets an item (input and label) from the dataset."""
        # Creates a copy of the encoding for labels
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        
        # Creates labels: Set non-masked positions to -100 (ignore in loss)
        labels = item["input_ids"].clone()  # Copy the input IDs to the labels
        labels[labels == self.tokenizer.pad_token_id] = -100  # Set padding tokens to -100 (ignore in loss)
        
        # Assigns labels to the item
        item["labels"] = labels
        
        return item
