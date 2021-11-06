#Quiz game.
name = input(str("what's your name \n "))
print ("Hi " + str.upper(name) + " It is nice to meet you.\n")
#function to check the answer
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer!')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again.')
                attempt = attempt + 1

            if attempt == 3:
                print('The correct answer is ' + answer +'.')
#set score to 0
score = 0

# game intro
print('Welcome to Guessing the Animal Quizzo.')
print('The rules are simple.\n 1. There will be a variety of 10 questions, where each question is worth 3 points.\n 2. Each question contains 3 attempts. One point will be deducted per attempt used until you have reached the maximum of 3 attempts.\n 3. The maximum overall score each player can get is 30.\n LET\'S GET STARTED!')

start = input('Please press ENTER to begin quiz.')
#ask question
guess1 = input('Which bear lives at the North Pole? ')
#to check ans.
check_guess (guess1, 'polar bear')
guess2 = input('Which is the fastest land animal? ')
check_guess (guess2, 'cheetah')

guess3 = input('Which is the largest animal? ')
check_guess (guess3, 'blue whale')

guess4 = input('Which is the slowest animal? ')
check_guess (guess4, 'sloth')

guess5 = input('Which animal is a universal symbol for peace? ')
check_guess (guess5, 'dove')

guess6 = input('Which animal does not have vocal chords? ')
check_guess (guess6, 'giraffe')

guess7 = input('Which animal cannot fart? ')
check_guess (guess7, 'kangaroo')

guess8 = input('Which animal\'s eyes are bigger than its brain? ')
check_guess (guess8, 'ostrich')

guess9 = input('Which aniaml eats sugar cane? ')
check_guess (guess9, 'panda')

guess10 = input('Which animal is a symbol of hope? ')
check_guess (guess10, 'sparrow')

#display score
if score == 30:
    print('Congratulations! ' + str.upper(name) + ' You answered all of the questions correctly! Your score is ' + str(score)+'.')
elif score >= 20:
    print('Good Job!' + str.upper(name) + ' Your score is ' + str(score)+'.')
else:
    print(str.upper(name) + ' Try again next time. Your score is ' + str(score)+'.')

#to play again
play_again = input("1.play again      2.exit \n ")
while True:
    if play_again == 1:
        continue
    else:
        print("Thankyou for playing ")
        break


