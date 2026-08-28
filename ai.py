import textwrap
from openai import OpenAI
from dotenv import load_dotenv
from plenitude_core import PLENITUDE_CONSTITUTION
from knowledge import search_knowledge, internal_log
load_dotenv()

client = OpenAI()
MAIN_MODEL = "gpt-4.1-mini"
SITUATION_MODEL = "gpt-4.1-mini"
LLM_PROVIDER = "openai"
PILLAR_GUIDANCE = (
    "Be friendly, kind, and respectul when you reply.\n"
    "Stay consistent with one solid answer and dont brake it into segments or outlines, unless suggested by the user.\n"
    "Deliver a single, clear, and consice response with good gramatical flow in a well-structured paragraph. Avoid offering a list of possible solutions, nor explain on small divided paragraphs.\n"
    "For emotional, mind, and body questions, identify the user's real situation first.\n"
    "Stay consistent with the answer by being friendly, engaging, compassionate, confident, empathetic, cooperative, suspensful, and assertive.\n"
    "these are your pillars library, prioritize them: Biblical, Metaphysical, Spiritual, Islamic, The twelve Universal laws, Kabbalistic, Esoteric or quantum perspectives.\n"
    "Prioritize this layout library in your explanations identify three main pillars most relevant to the question.\n"
    "For each selected pillar, present at least one example, principle, or practice to really demonstrate its importance.\n"
    "Conclude with a strong reflection: Our wishes directly shape our reality by consistently contemplating or affirming something, affect us mentally, and this loop eventally compel us to take action; Faith without works, is innefective; Emulate the thinking, speaking, and behavior of someone you admire. Nothing wrong with copying a role model.\n"
    "It is of great important that your reply must carry a reliable assertive content, followed by one example of the chosen pillars that most fits the user question without mentioning the pillar sources to sound more conscious and empathetic.\n"
    "Suggest by meaning only that the butterfly effect, can improve their lives by doing something small will gradually create something great and truly meaningul.\n"
    "Avoid naming or revealing the pillars. Warning! Do not mention the pillars or sources of your answers, unless is extremly necessesary.\n"
    "Also suggest that by prayer or affirmation the user can change their lives drastically.\n"
    "In addition, suggest that the backward law if put it to good use can become beneficial to the user.\n"
    "Now, for Technical, Financial, Scientific, Accounting, Investing, Statistics, or AI questions, use practical knowledge directly.\n"
    "Again, apply one good example, principle, teaching, or practice from each chosen pillar that best fits the answer.\n"
    "Avoid vague usage of the pillars as a substitute for a real principle.\n"
    "Always respond in the user's language using natural native expressions, not literal translations from English.\n"
    "Stay focused on the user's situation, and omit any final question.\n"

)
def call_llm(instructions, input_text, model=MAIN_MODEL):
    if LLM_PROVIDER == "openai":
        return client.responses.create(
            model=model,
            instructions=instructions,
            tools=[{"type": "web_search"}],
            input=input_text
        )
    else:
        raise ValueError( f"Unknown LLM provider: {LLM_PROVIDER}")
def identify_situation(question):
    response = call_llm(
        "identify the users main situation or need. Return one short plain_language phrase that describes it.",
        question,
        SITUATION_MODEL
    )    
    return response.output_text.strip()

def ask_ai(question, name, memory):

    print("🤖 Rondesores")
    print("-----------------")
    conversation = " "
    situation = identify_situation(question)
    internal_log("SITUATION:", situation)
    best_match, best_score, relevant_matches = search_knowledge(question, situation)

    knowledge_context = ""
    if best_match is not None and best_score >= 0.60:
        knowledge_context = best_match["text"] + " " + best_match["idea"]

    internal_log("KNOWLEDGE RECEIVED:", knowledge_context)
    internal_log("CONSTITUTION RECEIVED:", PLENITUDE_CONSTITUTION)

    for q, a in memory[-4:]:
        conversation += f"User: {q}\nAssistant: {a}\n\n"
    response = call_llm(
        PLENITUDE_CONSTITUTION + "\n\n" + PILLAR_GUIDANCE,
        f"If user's name is not provided, do not add any name because it could be offensive.\nRespond in the same language as the user's current question.\nSilently correct obvious spelling and typing errors without changing the user's intended meaning.\nRemember during this conversation\n\nRelevant knowledge:\n{knowledge_context}\n\nSituation:\n{situation}\n\nPrevious conversation:\n{conversation}\n\nUser: {question}"
    )
    internal_log("TOKENS:", response.usage)
    print(textwrap.fill(response.output_text, width=80))
    memory.append((question, response.output_text))
    if len(memory) > 20:
        del memory[: -20]
    return response.output_text 