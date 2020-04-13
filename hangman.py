def generate_random_word():
    import random
    word_list = ['apple', 'pick', 'brandeis', 'sherman', 'python']
    global random_word
    random_word = list(random.choice(word_list))

    return random_word


def guess():
    chances = len(random_word)
    global guess123
    guess123 = ['-'] * chances
    return guess123


def play_hangman():
    def word(random_word, letter):
        positions = []
        start_at = -1
        while True:
            try:
                position = random_word.index(letter, start_at + 1)
            except ValueError:
                break
            else:
                positions.append(position)
                start_at = position

        return positions

    question1 = input('Do you want to play hangman?')
    if question1.lower().startswith('y'):
        while True:
            length = int(len(random_word))
            chances = int(len(random_word))
            correct_answer = random_word
            while length > 0 and chances > 0:
                print('----------------------------------------------')
                print(guess123)
                print(chances, 'chances left')
                letter = input('Guess a letter')
                if letter in guess123:
                    chances = chances - 1
                    print("You have already guessed this letter. Please try another one. You have", chances,
                          'more chances')
                    continue
                if letter in correct_answer:
                    positions = word(random_word, letter)

                    for i in positions:
                        guess123[i] = correct_answer[i]
                        length = length - 1
                    print("Great!", chances, 'chances left')
                    print(guess123)
                if letter not in correct_answer:
                    chances = chances - 1
                    print("Sorry, this letter is not in the word. Please try again. You have", chances, "more chances")
            if length == 0:
                question2 = input(("Great! you won! Do you want to play it again?"))
                if question2.lower().startswith('y'):
                    continue
                else:
                    print("Thank you for playing the game")
                    break
            if chances == 0:
                question3 = input(("Sorry, you lose. Do you want to play it again?"))
                if question3.lower().startswith('y'):
                    continue
                else:
                    print("Thank you for playing the game")
                    break
    else:
        print('Why did you open it??????')

generate_random_word()
guess()

play_hangman()
