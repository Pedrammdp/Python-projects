import random
word_list = ['Garden', 'Window', 'Coffee', 'Bridge', 'Planet', 'Jungle', 'Anchor', 'Castle', 'Forest', 'Bottle', 'Mirror', 'Target', 'Summit', 'Future', 'Travel', 'Reason', 'Matter', 'Policy', 'Energy', 'Option', 'Engine', 'Figure', 'Volume', 'Period', 'Device', 'Create', 'Explore', 'Imagine', 'Develop', 'Receive', 'Publish', 'Improve', 'Manage', 'Support', 'Produce', 'Invest', 'Discuss', 'Confirm', 'Perform', 'Advance', 'Adjust', 'Gather', 'Reflect', 'Observe', 'Settle', 'Depart', 'Relate', 'Finish', 'Attack', 'Convey', 'Vibrant', 'Silent', 'Smooth', 'Gentle', 'Active', 'Recent', 'Former', 'Distant', 'Crucial', 'Worthy', 'Bitter', 'Global', 'Intense', 'Unique', 'Lively', 'Fierce', 'Simple', 'Curious', 'Yellow', 'Narrow', 'Steady', 'Obvious', 'Modern', 'Formal', 'Bright', 'Truth', 'Justice', 'Wisdom', 'Freedom', 'Purpose', 'Empathy', 'Success', 'Moment', 'Theory', 'System', 'Effort', 'Design', 'Change', 'Belief', 'Vision', 'Action', 'Growth', 'Impact', 'Crisis', 'Method', 'Source', 'Future', 'Detail', 'Spirit', 'Scheme']
lowercase_word_list = [word.lower() for word in word_list]

chosen_word = random.choice(lowercase_word_list)
word_len = len(chosen_word)

placeholder = ""

for position in range(word_len):
    placeholder += "_"

print(placeholder)

lives = 6

gameOver = False
correct_letters = []
while (gameOver != True):
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display +=  letter
        else:
            display += "_"
    

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Number of lives remaining: {lives}")
        if lives == 0:
            gameOver = True
            print("You lose")
            print(chosen_word)

    if "_" not in display:
        gameOver = True
        print("You win.")


