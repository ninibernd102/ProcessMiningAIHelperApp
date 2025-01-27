from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Modell und Tokenizer für Llama 3.2 laden
model_name = "meta-llama/Llama-3.2-1B" 
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Padding-Token setzen, falls es nicht definiert ist
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token  

# Lade den Datensatz (Training und Validierung)
dataset = load_dataset("json", data_files={"train": "data.jsonl", "validation": "data_valid.jsonl"}) 

# Daten vorbereiten
def preprocess_function(examples):
    inputs = tokenizer(examples["prompt"], truncation=True, padding="max_length", max_length=512)
    labels = tokenizer(examples["completion"], truncation=True, padding="max_length", max_length=512)
    inputs["labels"] = labels["input_ids"]  
    return inputs

# Tokenisieren der gesamten Trainingsdaten und Validierungsdaten
tokenized_dataset = dataset["train"].map(preprocess_function, batched=True)
tokenized_eval_dataset = dataset["validation"].map(preprocess_function, batched=True)

# Training-Parameter
training_args = TrainingArguments(
    output_dir="./fine_tuned_model", 
    evaluation_strategy="steps",  
    learning_rate=5e-5,
    per_device_train_batch_size=2, 
    num_train_epochs=3,
    save_steps=500,  
    logging_dir="./logs",  
    no_cuda=True, 
    eval_steps=500
)

# Trainer einrichten
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_eval_dataset 
)

# Fine-Tuning starten
trainer.train()

# Modell speichern
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")
