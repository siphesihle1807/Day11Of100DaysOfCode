import random
from Rules import rules

# Creating a blackjack game.
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score, user_name):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return f"Lose, {user_name} has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def game_main():
    print(logo)
    user_name = input("Enter gamer's name: ").title()
    print(f"Welcome {user_name}, Let's play BlackJack")
    print("You'll be playing against a computer.")
    
    see_rules = False
    gamer_rules = input("Would you like to see the rules? (Y/N): ")
    if gamer_rules.lower() == 'y':
          see_rules == True
          rules()
    else:
          see_rules == False

    
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"{user_name}'s final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score, user_name))

def start():
      if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        game_main()
      else:
            print("The game has ended. See you next time :)")
start()
