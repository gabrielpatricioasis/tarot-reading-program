import random

# Step 1: Define a Tarot Deck
tarot_deck = {
    "The Fool": "New beginnings, optimism, trust in life",
    "The Magician": "Action, the power to manifest",
    "The High Priestess": "Inaction, going within, the subconscious",
    "The Empress": "Abundance, nurturing, fertility, life in bloom!",
    "The Emperor": "Structure, stability, rules and power",
    "The Hierophant": "Institutions, tradition, society and its rules",
    "The Lovers": "Sexuality, passion, choice, uniting",
    "The Chariot": "Movement, progress, integration",
    "Strength": "Courage, subtle power, integration of animal self",
    "The Hermit": "Meditation, solitude, consciousness",
    "Wheel of Fortune": "Cycles, change, ups and downs",
    "Justice": "Fairness, equality, balance",
    "The Hanged Man": "Surrender, new perspective, enlightenment",
    "Death": "The end of something, change, the impermeability of all things",
    "Temperance": "Balance, moderation, being sensible",
    "The Devil": "Destructive patterns, addiction, giving away your power",
    "The Tower": "Collapse of stable structures, release, sudden insight",
    "The Star": "Hope, calm, a good omen!",
    "The Moon": "Mystery, the subconscious, dreams",
    "The Sun": "Success, happiness, all will be well",
    "Judgement": "Rebirth, a new phase, inner calling",
    "The World": "Completion, wholeness, attainment, celebration of life",
}

# Step 2: Welcome the User
def welcome_user():
    print("Welcome to the Tarot Reading Program!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's see what the cards have in store for you today.")
    return name

# Step 3: Ask for a Question or Focus
def get_user_question():
    question = input("Do you have a question or focus for your reading? (If not, just press Enter) ")
    if question:
        print(f"Focusing on: {question}")
    else:
        print("No specific focus? That's okay! The cards will guide you.")
    return question

# Step 4: Draw a Card
def draw_cards(num_cards=3):
    cards_drawn = random.sample(list(tarot_deck.items()), num_cards)
    print("\nYour Reading:")
    for card, meaning in cards_drawn:
        print(f"\n{card}: {meaning}")
    return cards_drawn

# Step 5: Ask to Play Again
def ask_replay():
    replay = input("\nWould you like another reading? (yes/no): ").lower()
    if replay == "yes":
        return True
    return False

# Step 6: Main Function
def main():
    welcome_user()
    while True:
        get_user_question()
        draw_cards()
        if not ask_replay():
            print("Thank you for using the Tarot Reading Program! Goodbye!")
            break

if __name__ == "__main__":
    main()