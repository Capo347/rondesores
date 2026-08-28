import math
from openai import OpenAI
from dotenv import load_dotenv
from knowledge_base import KNOWLEDGE_BASE
load_dotenv()
client = OpenAI()

DEBUG = False
KNOWLEDGE_EMBEDDINGS = {}

def internal_log(*args):
    if DEBUG: 
        print(*args)

def create_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def similarity(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(b * b for b in vector2))

    return dot_product / (magnitude1 * magnitude2)


def search_knowledge(question, situation=""): 
    question_vector = create_embedding(question + " " + situation)
    best_match = None
    best_score = -1
    relevant_matches = []

    for entry in KNOWLEDGE_BASE:
        entry_text = entry["text"] + " " + entry["idea"]
        if entry_text not in KNOWLEDGE_EMBEDDINGS:
            KNOWLEDGE_EMBEDDINGS[entry_text] = create_embedding(entry_text)

        entry_vector = KNOWLEDGE_EMBEDDINGS[entry_text]
        score = similarity(question_vector, entry_vector)
        internal_log("MATCH SCORE:", round(score, 3))

    if score > best_score:
        best_score = score
        best_match = entry

    if score >=0.60: 
        relevant_matches.append((entry, score))

    return best_match, best_score, relevant_matches




