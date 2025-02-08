# Mason Shipton, Lukas Fenkam, Rayan Alam, Christopher Kiige
# Description: Loads the model and tests the model on sample test.
# Date Created: 2025-02-08.
# Date Last Revised: 2025-02-08.

from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

# Loads pre-trained masked language model
model_name = "bert-base-multilingual-cased" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

# Sample sentence with a mask token
text = "The capital of France is [MASK]."

# Tokenizes the input text
inputs = tokenizer(text, return_tensors="pt")

# Runs the model
with torch.no_grad():
    outputs = model(**inputs)

# Gets the logits for the masked token
logits = outputs.logits

# Finds the index of the [MASK] token
mask_token_index = torch.where(inputs.input_ids == tokenizer.mask_token_id)[1]

# Gets the top predicted token for the mask
predicted_token_id = logits[0, mask_token_index, :].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id)

print(f"Predicted token: {predicted_token}")
