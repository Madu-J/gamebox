#----------------------------------------------------- */
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Choose (A, B, C or D): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
    

#----------------------------------------------------- */
def check_answer(answer, guess):
    
    if answer == guess:
        print('WELDONE! The answer is correct !')
        return 1
    else:
        print('Wrong Answer !')
        return 0

#----------------------------------------------------- */
def display_score(correct_guesses, guesses):
    print("---------------------------------------------------")
    print("Results")
    print("---------------------------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("You have scored: "+str(score)+"%")

#----------------------------------------------------- */
def play_again():
    pass
#----------------------------------------------------- */


questions = {
    "Which geografical location is Sweden?: ": "C",
    "How old is Sweden as a country?: ": "D",
    'How big is Sweden in square kirometres? ': 'B',
    'When was Sweden founded as a country? ': 'C',
    'What currency does Swedes use? ': 'A',
    'Which of these two are Swedish neighbouring countries? ': 'D',
    'How many languages does Swedes speak? ': 'A',
    'How many countries speak Swedish as official language? ': 'C',
    'What is Swedish best dish? ': 'D',
    'Which music band is the most popular in Sweden? ': 'B'
}

options = [['A. Eastern Europe', 'B. Western Europe', 'C. Northern Europe', 'D. Middle East'],
['A. Over 100 years', 'B. Over 500 years', ' C. Over 50 years',  'D. Over 1000 years'],
['A. About 500295 km', 'B. About 450295 km', 'C. About 250295 km', 'D. About 450295 km'],
['A.1823', 'B.1553' 'C. 1523' 'D. 1630'],
['A. Kronor (SEK)', 'B. Euro', 'C. NOK', 'D. USD'],
['A. Germany and Poland', 'B. Italy and Spain', 'C. Holand and Hungary', 'D. Finland and Norway'],
['A. Approximately 200 languages', 'B. Approximately 300 languages', 'C. Only one language', 'D. Only two official languages'],
['A. Three countries', 'B. Up to thirty countries', 'C. Two countries', 'D. Only one country'],
['A. Smögås', 'B. Potato chips', 'C. Kebab pizza', 'D. Köttbullar potatismos, gräddsås recipe'],
['A. Swedish House Mafia', 'B. Abba', 'C. Roxette', 'D. Europe']]

new_game()