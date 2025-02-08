# run_model.py
# Mason Shipton, Lukas Fenkam, Rayan Alam, Christopher Kiige
# Description: Loads the fine-tuned model and makes predictions on input sentences.
# Date Created: 2025-02-08.
# Date Last Revised: 2025-02-08.

from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

def run_model(model_path, tokenizer_path, input_sentence):
    """
    Run the fine-tuned model to predict the masked words in a sentence.
    
    Parameters:
    - model_path: Path to the fine-tuned model directory.
    - tokenizer_path: Path to the tokenizer directory.
    - input_sentence: Sentence containing a masked token (use [MASK] to represent the masked token).
    
    Returns:
    - The predicted word for the masked token.
    """
    # Loads the fine-tuned model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    model = AutoModelForMaskedLM.from_pretrained(model_path)

    # Tokenizes the input sentence
    inputs = tokenizer(input_sentence, return_tensors="pt")

    # Finds the position of the [MASK] token in the input sentence
    mask_token_index = torch.where(inputs.input_ids == tokenizer.mask_token_id)[1]

    # Forwards pass to get predictions
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Gets the predicted token for the [MASK] token
    mask_token_logits = logits[0, mask_token_index, :]
    predicted_token_id = torch.argmax(mask_token_logits, dim=1)

    # Decodes the predicted token ID back into a word
    predicted_token = tokenizer.decode(predicted_token_id)

    return predicted_token

if __name__ == "__main__":
    model_path = './indigenous_model'  # Path to fine-tuned model
    tokenizer_path = './indigenous_model'  # Path to tokenizer
    input_sentence = "The Cree people speak the [MASK] language in Canada (Northern regions)."
    
    predicted_word = run_model(model_path, tokenizer_path, input_sentence)
    print(f"Predicted word: {predicted_word}")
