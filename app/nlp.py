import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text: str):
    doc = nlp(text)
    nodes = []
    for ent in doc.ents:
        nodes.append({
            "text": ent.text,
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_
        })
    if not nodes:
        nodes = [{"text": chunk.text, "start": chunk.start_char, "end": chunk.end_char} for chunk in doc.noun_chunks]
    mindmap = {"nodes": nodes, "edges": []}
    return mindmap
