import random
def playGame():
    def deal_card():
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def sum(deckofCards):
        total_sum = 0
        for num in deckofCards:
            total_sum += num
        return total_sum

    sumUser = sum(user_cards)
    sumComputer = sum(computer_cards)

    def win_or_lose(user_score, computer_score):
        """Determines the winner based on final scores."""
        if user_score > 21:
            return "You BUSTED! You Lose! 😭"
        elif computer_score > 21:
            return "Computer BUSTED! You Win! 🎉"
        elif user_score > computer_score:
            return "You Win! Your score is higher. 🎉"
        elif computer_score > user_score:
            return "You Lose! Computer's score is higher. 😭"
        else:
            return "It's a Draw! 🤝"

    print("--- Welcome to Console Blackjack! ---")
    print(f"Your Cards: {user_cards} (Score: {sumUser})")
    print(f"Computer's first card: [{computer_cards[0]}]")
    is_user_turn_over = False

    while not is_user_turn_over:
        if sumUser >= 21:
            is_user_turn_over = True
            continue

        should_continue = input("Type 'y' to get another card (hit), or 'n' to pass (stand): ").lower()

        if should_continue == 'y':
            user_cards.append(deal_card())
            sumUser = sum(user_cards)
            
            print(f"Your cards: {user_cards}, current score: {sumUser}")

            if sumUser > 21:
                is_user_turn_over = True
        else:
            is_user_turn_over = True

    # --- COMPUTER'S TURN ---

    if sumUser <= 21:
        print("\n--- Computer's Turn (Dealer Hits until 17) ---")
        
        while sumComputer < 17:
            print(f"Computer hits (score is currently {sumComputer})...")
            computer_cards.append(deal_card())
            sumComputer = sum(computer_cards)
            
        print(f"Computer's final hand: {computer_cards}, final score: {sumComputer}")
        print("---------------------------------------------")

    print(f"\nFINAL SCORES: You: {sumUser} | Computer: {sumComputer}")
    print(win_or_lose(sumUser, sumComputer))

while(input("Do you want to play a game of black jack? 'y or 'n' \n") =='y'):
    print("\n" * 20)
    playGame()