# train.py
# Mason Shipton, Lukas Fenkam, Rayan Alam, Christopher Kiige
# Description: Loads the dataset, initializes the model, and trains it.
# Date Created: 2025-02-08.
# Date Last Revised: 2025-02-09.

from transformers import AutoTokenizer, AutoModelForMaskedLM, Trainer, TrainingArguments
from dataset import IndigenousDataset

def train_model(dataset_path, model_name="bert-base-multilingual-cased", epochs=50, batch_size=8):
    """
    Trains a masked language model on the given dataset.
    
    Parameters:
    - dataset_path: Path to the dataset text file.
    - model_name: Pretrained model to fine-tune (default: "bert-base-multilingual-cased").
    - epochs: Number of training epochs (default: 10).
    - batch_size: Batch size for training (default: 8).
    """
    # Loads the pre-trained tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)

    # Loads and tokenize the dataset
    dataset = IndigenousDataset(dataset_path, tokenizer)

    # Prepares the training arguments
    training_args = TrainingArguments(
        output_dir="./output",         # Directory where the model will be saved
        num_train_epochs=epochs,       # Sets the number of epochs here (default: 5)
        per_device_train_batch_size=batch_size, # Batch size for training
        save_steps=10_000,             # Saves the model after every 10,000 steps
        save_total_limit=2,            # Keeps only the last 2 saved models
        logging_dir='./logs',          # Logs directory for monitoring
    )

    # Initializes the Trainer
    trainer = Trainer(
        model=model,                           # The model to train
        args=training_args,                    # The training arguments
        train_dataset=dataset,                 # The dataset to train on
        tokenizer=tokenizer,                   # The tokenizer to use during training
    )

    # Trains the model
    trainer.train()

    # Saves the fine-tuned model
    model.save_pretrained("./indigenous_model")
    tokenizer.save_pretrained("./indigenous_model")

if __name__ == "__main__":
    dataset_path = 'IndigenousCultures.txt' 
    train_model(dataset_path, epochs=100) 
