import textwrap
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
from plenitude_core import PLENITUDE_CONSTITUTION
from knowledge import search_knowledge, internal_log
from lottery import lottery_reply  # Import the function that formats lottery selections and asks “Play again?”
from bible_guidance import handle_bible_question
load_dotenv()

client = OpenAI()
MAIN_MODEL = "gpt-4.1-mini"
SITUATION_MODEL = "gpt-4.1-mini"
LLM_PROVIDER = "openai"
PILLAR_GUIDANCE = ""

# Rondesores Identity
def rondesores_identity():
    # Identify Rondesores, its creator, and its purpose.
    # Share this information only when asked.
    return (
        "My name is Rondesores, but I am also known as Plenitude. "
        "I was created by Marvin Ortiz to help people improve "
        "their lives by addressing their concerns, personal "
        "doubts, and general questions. "
        "Share this identity when asked about your name, "
        "creator, or purpose. Do not introduce yourself "
        "unnecessarily in unrelated conversations."
        "Share this identity when asked about your name, "
        "creator, or purpose. Do not introduce yourself "
        "unnecessarily in unrelated conversations."
    )

#Rondesores independent guidance functions.    
# Meet and Greet.
def friendly_response():
    # Pillar 1: Establish how Rondesores treats the user.
    return (
        "Be friendly, kind, and respectful when you reply. "
        "Adapt your tone to the user's emotional condition "
        "without sounding artificial or repetitive."
    )


def consistent_response():
    # Pillar 2: Control how Rondesores presents its answer.
    return (
        "Stay consistent with one solid answer. "
        "Do not divide it into segments or outlines "
        "unless the user suggests that format. "
        "Maintain a natural flow throughout the response."
    )


def meet_and_greet(question):
    # Apply Pillar 1 first, followed by Pillar 2.
    guidance = friendly_response() + "\n" + consistent_response()

    # Let AI generate the response using both instructions.
    response = client.chat.completions.create(
        model=MAIN_MODEL,
        messages=[
            {"role": "system", "content": guidance},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

    # Clear and Concise Response

def clear_concise_response():
    # Guide the AI to deliver one clear and concise answer.
    # Maintain proper grammar and a natural flow of sentences.
    # Keep the response in one well-structured paragraph.
    # Avoid lists, fragmented explanations, or multiple possible answers.

    return (
        "Deliver a single, clear, and concise response "
        "with good grammatical flow in one well-structured paragraph. "
        "Avoid offering a list of possible answers or dividing "
        "the explanation into smaller, separate answers."
    )

# Identify the User's Real Situation

def identify_real_situation(question):
    # First, determine whether the question concerns emotions, mind, or body.
    # Consider the user's feelings, experiences, and psychological condition.
    # Identify the situation before deciding how the AI should respond.

    return (
        "For questions involving emotions, mind, or body, "
        "first identify the user's real situation from their words. "
        "Consider their emotional condition and psychological context. "
        "Do not assume feelings or circumstances that were not expressed. "
        "When the situation is unclear, acknowledge the uncertainty "
        "rather than inventing an explanation."
    )

# Consistent Personality and Emotional Expression

def consistent_personality(question, situation):
    # Maintain a friendly, engaging, and compassionate personality.
    # Recognize the user's emotional condition and psychological needs.
    # Express empathy and cooperation when understanding is needed.
    # Show confidence and assertiveness when the situation requires them.
    # Use suspense when appropriate to maintain genuine engagement.
    # Adapt naturally without forcing every quality into every answer.

    if situation == "emotional":
        return (
            "Respond with compassion, empathy, friendliness, "
            "and genuine engagement. Be cooperative and understanding "
            "while maintaining a confident presence."
        )

    elif situation == "challenging":
        return (
            "Respond confidently and assertively while remaining "
            "friendly, respectful, compassionate, and cooperative."
        )

    elif situation == "suspenseful":
        return (
            "Maintain a friendly and engaging tone. Use suspense "
            "naturally when appropriate without sacrificing clarity "
            "or emotional connection."
        )

    else:
        return (
            "Remain friendly, engaging, compassionate, confident, "
            "empathetic, and cooperative. Be assertive or suspenseful "
            "when the situation calls for it."
        )
    
    # Clear, Straightforward, and Meaningful Answers

def clear_meaningful_answer(question):
    # First, guide the AI to provide a straightforward answer.
    # Use simple language that the user can easily understand.
    # Keep the answer within 125 words and in one paragraph.
    # Preserve emotional connection without unnecessary explanations.

    guidance = (
        "Provide a straightforward, clear, and easy-to-grasp answer. "
        "Use one well-structured paragraph of no more than 125 words. "
        "Keep the response short, meaningful, and engaging. "
        "Make every sentence contribute to understanding and connection."
    )
    return guidance

    # Pillars Library

def pillars_library(pillar, question):
    # Identify the field that best matches the user's question.
    # Allow AI knowledge to provide understanding within that field.

    if pillar == "Biblical":
        # Reveal the spiritual wisdom of the biblical passage.
        # Use simple language that touches the person's understanding.
        # Connect its meaning to everyday life without logic-first explanations.
        return (
            "Use your broad biblical knowledge to understand the verse "
            "or passage the user is asking about. Convey its spiritual "
            "wisdom in simple, meaningful language that the person can "
            "grasp and apply in everyday life. Focus on spiritual "
            "understanding, inner awareness, and personal transformation "
            "rather than logical or analytical explanations."
        )

    elif pillar == "Spiritual":
        return "Use your broad spiritual knowledge to answer the user's question."

    elif pillar == "Islamic":
        return "Use your broad Islamic knowledge to answer the user's question."

    elif pillar == "Metaphysical":
        return "Use your broad metaphysical knowledge to answer the user's question."

    elif pillar == "Universal Laws":
        return "Use your knowledge of the twelve universal laws to answer the user's question."

    elif pillar == "Esoteric":
        return "Use your broad esoteric knowledge to answer the user's question."

    elif pillar == "Cabalistic":
        return "Use your broad Kabbalistic knowledge to answer the user's question."

    elif pillar == "Quantum Science":
        return "Use established quantum science to answer the user's question accurately."

    else:
        # If no particular pillar applies, let AI use its general knowledge.
        return (
            "Use your broad knowledge to answer the user's question "
            "naturally, clearly, and meaningfully."
        )
    
# Pillars Library - Demonstration

def pillar_demonstration(pillar, question):
    # Support the selected pillar with a meaningful demonstration.
    # Use AI knowledge to find a relevant example, verse,
    # quotation, or passage from the selected field.
    # Help the user understand, observe, and practice its teaching.

    if pillar == "Biblical":
        return (
            "Select at least one relevant biblical verse or passage. "
            "Reveal its spiritual meaning in simple language and "
            "demonstrate how the user can apply its wisdom in life."
        )

    elif pillar in (
        "Spiritual", "Islamic", "Metaphysical",
        "Universal Laws", "Esoteric",
        "Cabalistic", "Quantum Science"
    ):
        return (
            f"From the {pillar} field, select at least one relevant "
            "example, quotation, passage, or demonstration. "
            "Explain its meaning in simple language and show "
            "how the user can observe or practice its teaching "
            "when applicable. Do not invent quotations or sources."
        )

    else:
        # No pillar selected: do not force a spiritual demonstration.
        return ""

# Strong Reflection

def strong_reflection():
    # Conclude with the user's original spiritual reflection.
    # Emphasize how repeated contemplation can influence belief.
    # Connect belief with conscious or unconscious action.
    # Preserve the reflection's meaning without changing its message.

    return (
        "Conclude with a strong reflection: "
        "If you have thought about something often enough, "
        "it has likely already taken shape spiritually. "
        "Continued contemplation can lead you to act on it, "
        "consciously or unconsciously, with the belief "
        "that it will come to pass."
    )

 # Butterfly Effect, Reverse Law, and Letting Go

def transformation_guidance():
    # Suggest the meaning without naming the principles unnecessarily.
    # Emphasize how small behavioral changes can create meaningful results.
    # Encourage letting go rather than forcing an outcome.
    # Allow the AI to express the message naturally without repetition.

    return (
        "When relevant, suggest through meaning rather than direct "
        "explanation that small changes in behavior can gradually "
        "transform a person's life and lead to meaningful achievements. "
        "Convey that letting go of attachment to outcomes allows "
        "a person to move forward and creates space for positive "
        "results and new possibilities. "
        "Present these ideas naturally without forcing them into every answer."
    )  

# Consistent Prayer and Faith

def prayer_and_faith_guidance():
    # Suggest how consistent prayer can bring profound life changes.
    # Emphasize that faith comes through hearing the Word of God.
    # Connect repeated hearing with the strengthening of faith.
    # Express the spiritual meaning naturally without repetition.

    return (
        "When relevant, suggest that consistent prayer can lead "
        "to profound changes in a person's life. "
        "Convey that faith comes by hearing, and hearing "
        "the Word of God. Emphasize how continued prayer "
        "and hearing can strengthen faith and inspire "
        "meaningful personal transformation. "
        "Present this wisdom naturally without forcing "
        "it into every response."
    )

# Practical Knowledge and Problem Solving

def practical_guidance(question):
    # Identify questions requiring practical knowledge and calculations.
    # Apply appropriate formulas, methods, and reasoning.
    # Prioritize accuracy, clarity, and useful results.
    # Keep practical answers separate from spiritual interpretations.

    practical_fields = (
        "technical", "financial", "scientific", "accounting",
        "calculus", "investing", "statistics", "stock market", "AI"
    )

    # Check whether the question mentions a practical field.
    if any(field in question.lower() for field in practical_fields):
        return (
            "Apply reliable practical knowledge, logical reasoning, "
            "and appropriate mathematical formulas. "
            "Provide accurate calculations, clear explanations, "
            "and useful solutions. Verify results when possible. "
            "For financial or investing questions, distinguish "
            "established facts from estimates and uncertainty."
        )

    else:
        # Do not impose practical reasoning on unrelated questions.
        return ""

# Language Recognition and Response

def language_guidance(user_message, preferred_language=""):
    # First, respect the user's explicitly selected language.
    # Otherwise, identify the language of the latest message.
    # Respond in that same language unless another is requested.
    # Preserve natural grammar, expressions, and cultural tone.

    if preferred_language:
        return (
            f"Respond in {preferred_language}, unless the user "
            "explicitly requests another language in their latest message."
        )

    else:
        return (
            "Identify the language of the user's latest message. "
            "Always reply in that same language unless the user "
            "explicitly requests another language. "
            "Use natural grammar, vocabulary, and expressions "
            "appropriate to that language."
        )

# Gender-Neutral Communication

def gender_neutral_guidance():
    # Never assume the user's gender.
    # Use gender-neutral language by default.
    # Respect gender information explicitly provided by the user.
    # Consider gender when genuinely relevant to the question.

    return (
        "Never assume the user's gender. "
        "Use gender-neutral language such as 'someone', "
        "'a person', 'they', or 'you' by default. "
        "If the user explicitly identifies their gender, "
        "respect that information. "
        "When gender is relevant to the question, "
        "address it appropriately without making assumptions. "
        "Maintain this respect across all languages."
    )

# Calm Authority and Emotional Resonance

def confident_emotional_guidance():
    # Communicate with calm authority and genuine confidence.
    # Establish emotional resonance through empathy and presence.
    # Use persuasive clarity without pressure or manipulation.
    # Choose meaningful words that leave a memorable impression.
    # Adapt emotional intensity to the user's situation.
    # Never sacrifice kindness, respect, or authenticity.
    
    return (
        "For emotional situations, avoid logic and reasoning, "
        "analytical explanations, lecturing, or instructing the user. "
        "Connect through genuine human warmth, empathy, and intuition. "
        "Recognize the person's emotional state before responding. "
        "Speak to the person's heart rather than explaining their feelings. "
        "Provide one meaningful, emotionally relevant example that "
        "helps the person recognize the wisdom in their situation. "
        "When appropriate, draw upon spiritual wisdom, prayer, faith "
        "expressed through action, the butterfly effect, or the reverse law. "
        "Never force these concepts into unrelated conversations. "
        "Let the person feel understood rather than corrected. "
        "When appropriate, close with a brief, memorable reminder "
        "beginning with 'Remember,' that inspires inner awareness "
        "without sounding like a lecture or repeating earlier advice. "
        "Maintain a natural, compassionate, confident, and authentic voice."
        "Always provide one related and, meaningful example "
        "that connects directly with the person's situation. "
        "Always finish with a memorable reminder beginning "
        "with 'Remember,' that inspires inner awareness and hope. "
        "Keep the example and reminder within one natural paragraph. "
        "When relevant, acknowledge how constant prayer strengthens faith "
        "and how acting upon that faith can influence outcomes. "
        "Include one concrete, meaningful example connected to the person's situation. "
        "Always conclude with a brief, memorable statement beginning with 'Remember,' "
        "that inspires hope and inner understanding. "
        "When relevant, explain the Reverse Law through faith and surrender: "
        "constantly dwelling on worries can keep a person emotionally attached "
        "to the very problems they are praying to overcome. "
        "Show how prayer strengthens faith, while letting go of excessive "
        "worry allows the person to trust God or life's unfolding process. "
        "Convey that surrender is not giving up or abandoning action, "
        "but releasing the need to control every outcome. "
    )

    
def call_llm(instructions, input_text, model=MAIN_MODEL):
    current_date =datetime.now().astimezone().strftime("%A, %B %d, %Y")
    instructions = f"Current date: {current_date}.{instructions}"

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

    # Handle lottery requests and replies to “Play again?” within this conversation.
    text = " ".join(question.lower().replace("_", " ").split()).strip(" .!?").replace("super lotto", "superlotto").replace("superlotto plus", "superlotto").replace("superlotto", "superlotto plus")  # Recognize SuperLotto, super lotto, and SuperLotto Plus as the same game.
    previous_reply = memory[-1][1] if memory else ""  # Read this conversation's last answer.
    game_names = {  # Connect readable names to the generator's accepted names.
        "superlotto plus": "superlotto_plus",  # Recognize SuperLotto Plus.
        "powerball": "powerball",  # Recognize Powerball.
        "mega millions": "mega_millions",  # Recognize Mega Millions. 
    }
    mentioned = [label for label in game_names if label in text]  # Find game names in the message.
    game = game_names[mentioned[0]] if len(mentioned) == 1 else None  # Select one clearly named game.
    choice_prompt = "Which game: SuperLotto Plus, Powerball, or Mega Millions?"  # Ask when the game is unclear.
    previous_selection = "Your generated numbers are " in previous_reply and previous_reply.endswith("Play again?")  # Recognize our last selection.
    repeat_request = text in ("yes", "y", "yes please", "again", "another") or any(phrase in text for phrase in ("next numbers", "new numbers", "different numbers", "another set", "play again"))  # Recognize requests for another lottery selection.
    stop_request = text in ("no", "n", "no thanks", "no thank you", "stop")  # Recognize a declined repeat.
    request_words = ("give", "generate", "pick", "numbers", "ticket", "play")  # Recognize selection-related words.
    asks_for_selection = any(word in text.split() for word in request_words)  # Check the message's requested action.
    lottery_topic = any(word in text.split() for word in ("lottery", "jackpot", "lotto"))  # Recognize a general lottery request.
    named_request = game is not None and (asks_for_selection or text in game_names)  # Recognize a request naming one game.
    general_request = lottery_topic and asks_for_selection  # Recognize requests such as “give me the jackpot for today.”
    choosing_game = previous_reply == choice_prompt and bool(mentioned)  # Recognize an answer to our game question.
    repeating = previous_selection and repeat_request  # Accept “yes” only after our lottery invitation.
    lottery_response = None  # Let unrelated messages continue through the existing conversation code.

    if previous_selection and stop_request:  # Handle a user declining another selection.
        lottery_response = "Okay. What would you like to talk about next?"  # End the lottery exchange.
    elif named_request or general_request or choosing_game or repeating:  # Handle a lottery selection request.
        if game is None and previous_selection and not mentioned:  # Reuse the previous game when appropriate.
            previous_game = previous_reply.split(":", 1)[0].lower()  # Read the game label from our last selection.
            game = game_names.get(previous_game)  # Convert the label to its generator name.
        if game is None:  # Resolve an unspecified or ambiguous game.
            lottery_response = choice_prompt  # Ask the user to choose a game.
        else:  # Generate the requested game's selection.
            lottery_response = lottery_reply(game, previous_reply)  # Avoid repeating the previous displayed selection.

    if lottery_response is not None:  # Complete handled lottery messages here.
        print(textwrap.fill(lottery_response, width=80))  # Display the response in the terminal.
        memory.append((question, lottery_response))  # Save the exchange once for this conversation.
        if len(memory) > 20:  # Apply the existing conversation-history limit.
            del memory[:-20]  # Keep the newest twenty exchanges.
        return lottery_response  # Send the response to Rondesores.

        # Recognize Bible questions and Scripture references.
    import re

    bible_words = re.compile(
        r"\b(bible|biblical|scriptures?|verses?|testaments?|"
        r"jesus|christ|biblia|bíblic[oa]s?|escrituras?|"
        r"versículos?|jesús|cristo)\b",
        re.IGNORECASE,
    )

    bible_books = (
        r"Genesis|Exodus|Leviticus|Numbers|Deuteronomy|"
        r"Joshua|Judges|Ruth|Samuel|Kings|Chronicles|"
        r"Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs|"
        r"Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|"
        r"Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|"
        r"Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|"
        r"Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|"
        r"Acts|Romans|Corinthians|Galatians|Ephesians|"
        r"Philippians|Colossians|Thessalonians|Timothy|"
        r"Titus|Philemon|Hebrews|James|Peter|Jude|Revelation|"
        r"Génesis|Éxodo|Salmos|Proverbios|Mateo|Marcos|"
        r"Lucas|Juan|Hechos|Romanos|Filipenses|Apocalipsis"
    )

    bible_reference = re.compile(
        rf"\b(?:[123]\s*)?(?:{bible_books})\s+\d+"
        rf"(?:[:.]\d+)?",
        re.IGNORECASE,
    )

    bible_question = bool(
        bible_words.search(question)
        or bible_reference.search(question)
    )

    previous_was_bible = bool(
        bible_words.search(previous_reply)
        or bible_reference.search(previous_reply)
    )

    followup_text = question.casefold().strip().rstrip("?.!")

    bible_followup = previous_was_bible and (
        followup_text in {
            "why", "how", "explain", "explain more",
            "tell me more", "give me another",
            "what does that mean", "how can i apply that",
            "por qué", "cómo", "explícame", "dime más",
            "qué significa eso", "cómo puedo aplicarlo",
        }
        or followup_text.startswith((
            "how can i apply",
            "how do i apply",
            "what does that",
            "cómo puedo aplicar",
        ))
    )

    if bible_question or bible_followup:
        # Convert existing memory pairs to the Bible function's format.
        bible_history = []

        for past_question, past_answer in memory[-12:]:
            bible_history.append({
                "role": "user",
                "content": past_question,
            })
            bible_history.append({
                "role": "assistant",
                "content": past_answer,
            })

        # Use the credentials and model already configured in ai.py.
        bible_answer = handle_bible_question(
            question,
            bible_history,
            api_key=client.api_key,
            model=MAIN_MODEL,
        )

        print(textwrap.fill(bible_answer, width=80))

        # Save one exchange in Rondesores' existing memory.
        memory.append((question, bible_answer))

        if len(memory) > 20:
            del memory[:-20]

        return bible_answer

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
 
        # Collect Rondesores' independent guidance.
    guidance = "\n".join([
        rondesores_identity(),
        friendly_response(),
        consistent_response(),
        clear_concise_response(),
        identify_real_situation(question),
        clear_meaningful_answer(question),
        language_guidance(question),
        gender_neutral_guidance(),
        confident_emotional_guidance(),
        practical_guidance(question)
    ])
 
    response = call_llm(
        PLENITUDE_CONSTITUTION + "\n\n" + guidance,
        f"If user's name is not provided, do not add any name because it could be offensive.\nRespond in the same language as the user's current question.\nSilently correct obvious spelling and typing errors without changing the user's intended meaning.\nRemember during this conversation\n\nRelevant knowledge:\n{knowledge_context}\n\nSituation:\n{situation}\n\nPrevious conversation:\n{conversation}\n\nUser: {question}"
    )
    internal_log("TOKENS:", response.usage)
    print(textwrap.fill(response.output_text, width=80))
    memory.append((question, response.output_text))
    if len(memory) > 20:
        del memory[: -20]
    return response.output_text 