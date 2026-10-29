import random

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards.append(random.choice(cards))

    def score(self):
        total = sum(self.cards)

        if total == 21 and len(self.cards) == 2:
            return 0
        if 11 in self.cards and total > 21:
            total -= 10

        return total
test_hand = Hand()
test_hand.add_card()
test_hand.add_card()
test_hand.add_card()

print("Test cards:", test_hand.cards)
print("Test score:", test_hand.score())
print()

user_hand = Hand()
computer_hand = Hand()

for _ in range(2):
    user_hand.add_card()
    computer_hand.add_card()

game_over = False

while not game_over:
    user_score = user_hand.score()
    computer_score = computer_hand.score()

    print(f"Your cards: {user_hand.cards}, current score: {user_score}")

    if computer_hand.cards:
        print(f"Computer's first card: {computer_hand.cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == "y":
            user_hand.add_card()
        else:
            game_over = True


while computer_hand.score() != 0 and computer_hand.score() < 17:
    computer_hand.add_card()


user_score = user_hand.score()
computer_score = computer_hand.score()

print(f"\nYour final hand: {user_hand.cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_hand.cards}, final score: {computer_score}")
print(compare(user_score, computer_score))