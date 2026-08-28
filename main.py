from ai import ask_ai
from datetime import datetime
from prompt_toolkit import prompt 

print("Welcome to Rondesores.")
name = input("May I ask your name? ")
memory = []

print(f"\nIt's a pleasure to meet you, {name}.")
print("How can I help you today?\n")

while True:
    question = prompt("> ")
    if not question.strip():
        print("Please enter your question again.")
        continue
    if question.lower() == "journal":
        break
    answer = ask_ai(question, name, memory)
print("1. New reflection")
print("2. View past reflections")
print("3. Exit")
choice = input("\nChoose an option: ")
if choice == "1":
    print("Welcome to your awareness practice.")
    observation = input("What did you observe today that most people ignored? ")
    emotion = input("What emotion guided your actions today? ").lower ()
    compassion = input("How did you show compassion today? ")
    dream = input("What dream or vision stayed in your mind today? ")
    print("\nReflection:")
    print("Observation strengthens awareness.")
    print("Emotion directs energy.")
    print("Compassion multiplies harmony.")
    print("Dreams guide the future.")
    print("\nRemember:")
    print("Attention shapes reality.")
    if emotion == "sad":
        print("Sadness asks for joy. Do something small that brings light.")
    elif emotion == "happy":
        print("Happiness grows when shared. Spread harmony.")
    elif emotion == "frustrated":
        print("Frustration asks for patience. Slow down and observe carefully. Breathe deep and exhale.")
    elif emotion == "Jealous":
        print("Jelousy is a mirror. Turn it into inspiration to improve yourself.")
    elif emotion == "fear":
        print("Fear asks for courage. Breathe, observe, and move forward calmly.")
    elif emotion == "angry":
        print("Anger is strong energy. Transform it into compassionate action.")
    elif emotion == "peaceful":
        print("Peace multiplies harmony. Let others feel your calm presence.")
    else:
        print("Every emotion carries a lesson if you observe it carefully.")

    print("\nYour awareness today:")
    print("Observation:", observation)
    print("Compassion:", compassion)
    print("Dream", dream)
    print("When attention rests on a possibility, it becomes reality.")
    print("\nHold your vision with emotion, then release it.")
    print("What is planted in faith returns multiplied.")
    print("Faith is the action born from what you recognize as truth.")
    print("\nCreation reflection:")
    print("In the beginning there was a possibility.")
    print("Light appears when awareness speaks with intention.")
    print("What is spoken with belief begins to take form.")
    print("\nMind reflection:")
    print("What you observe, you rememner.")
    print("What you feel, you believe.")
    print("Attention writes memory.")
    print("Emotion gives belief its strength.")
    print("\nAwareness formula:")
    print("\n1. Observe")
    print("What you observe, you remember.")
    print("Attention collapses possibility into experience.")
    print("\n2. Feel")
    print("What you feel, you believe.")
    print("Belief is the truth each mind accepts as real.")
    print("Emotion gives belief its living energy")
    print("\n3. Transform")
    print("Where compassion moves through the heart, reality begins to change.")
    print("Shared emotion connects minds like entangle particles")
    print("\nReflection question:")
    print("Did your compassion today influence the emotional state of someone else? ")
    print("Where two or more hearts shared the same hope, what possibility appeared? ")
    print("\nRemember:")
    print("Attention shapes reality.")
    print("\nSaving your awareness entry...")
    current_time = datetime.now() .strftime ("%Y-%m-%d %H:%M")
    with open("awareness_log.txt", "a") as file:
        file.write(f"\n--- New Entry ({current_time}) ---\n")
        file.write("Observation: " + observation + "\n")
        file.write("Emotion: " + emotion + "\n")
        file.write("Compassion: " + compassion + "\n")
        file.write("Dream: " + dream + "\n") 
    print("Your reflection has been saved.")

elif choice == "2":
    print("\nPast reflection:\n")
    from datetime import datetime, timedelta
    today = datetime.now ().date()
    yesterday = today - timedelta (days=1)
    with open("awareness_log.txt", "r") as file:
        show_entry = False
        last_label = None
        seen_dates = set()
        found_reflection = False
        for line in file:
            if line.startswith("--- New Entry") and "(" in line:
                date_text = line.split("(") [1].split(") ")[0]
                entry_date = datetime.strptime(date_text.split()[0], "%Y-%m-%d").date()        
        
                if entry_date == today:
                        if last_label == "today":
                            continue
                        label = entry_date.strftime("today")
                        show_entry = True

                elif entry_date == yesterday:
                    label = entry_date.strftime("yesterday")
                    show_entry = True
                else:
                    show_entry = False
                    continue
                if entry_date not in seen_dates and show_entry:
                    print(f"\n📆 {label}")
                    found_reflection = True
                    seen_dates.add(entry_date)
                    last_label = label

            if show_entry:
                    print("  " + line.strip())
        if not found_reflection:
            print("\nNo reflections from today or yesterday.")
            print("What changed in you today? ")


        elif choice == "3":
            print("Goodbye. Stay aware.")