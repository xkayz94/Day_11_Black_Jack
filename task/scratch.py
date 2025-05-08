import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def black_jack(user):
    if sum(user) == 21 and len(user) == 2:
        return 0

    if 11 in user and sum(user) > 21:
        user.remove(11)
        user.append(1)

    return sum(user)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_continue = True
    user_score = -1
    computer_score = -1
    while game_continue:

        user_score = black_jack(user_cards)
        computer_score = black_jack(computer_cards)

        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'Computer is first card: {computer_cards[0]}')

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_continue = False
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass:")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_continue = False

    while user_score != 0 and user_score < 17:
        computer_cards.append(deal_card())
        computer_score = black_jack(computer_cards)

    print(compare(user_score, computer_score))

game()



