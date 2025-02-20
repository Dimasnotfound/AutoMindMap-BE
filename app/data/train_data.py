import json
import spacy
from spacy.util import minibatch, compounding
from spacy.training.example import Example
import random

# Membaca dataset dari file JSON
with open("app/data/dataset_dummy.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Format dataset untuk spaCy: (text, {"entities": [(start, end, label), ...]})
TRAIN_DATA = [
    (item["text"], {"entities": [(ent["start"], ent["end"], ent["label"]) for ent in item["entities"]]})
    for item in raw_data
]

def train_model(n_iter=30):
    # Membuat model kosong untuk bahasa Inggris
    nlp = spacy.blank("en")
    print("Pipeline awal:", nlp.pipe_names)
    
    # Menambahkan komponen NER ke pipeline
    if "ner" not in nlp.pipe_names:
        nlp.add_pipe("ner", last=True)
    ner = nlp.get_pipe("ner")
    
    # Menambahkan label secara dinamis dari dataset
    for _, annotations in TRAIN_DATA:
        for start, end, label in annotations.get("entities"):
            ner.add_label(label)
    
    # Mulai training
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        # Membuat batch secara dinamis
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.5))
        for batch in batches:
            examples = []
            for text, ann in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, ann)
                examples.append(example)
            nlp.update(examples, drop=0.5, sgd=optimizer, losses=losses)
        print(f"Iterasi {itn+1}, Losses: {losses}")
    
    # Menyimpan model ke direktori "model_automindmap"
    output_dir = "./model_automindmap"
    nlp.to_disk(output_dir)
    print("Training selesai. Model disimpan di:", output_dir)

if __name__ == "__main__":
    train_model()
