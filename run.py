import time

start_time = time.time()


print("Welcome To Gamebox Quiz App !")

# Let player choose if they want to play or quit
player = input("Few Things About Sweden. Do You Want To Play? y/n ")
print()

# Check If user condition is true. If yes then play else quit
if player.lower() != "y":
    quit("You chose to quit the game, thanks for stoping by")
else:
    print("Here is the rules for the game ")
    print(" . There are 10 questions in total, and 4 options ")
    print(" . Choose from options; A, B, C and D ")
    print(" . The correct answer will appear if your answer is incorrect")
    print(" . Your score will be displayed at the end of the game")
    print(" . Please note: You can not exit the game once you start.")
    print()

    player = input(" . If you are ready, type 'S to start or Q to quit' ")

if player.lower() != "s":
    quit()
else:
    print("Okay, lets' go :)")

print()
# Let player enter name
user_name = input("Enter your name: ").capitalize()
# The strip() method ensures that something has to be entered and
# the isalpha() method ensures that only letters can be entered
while not user_name.strip() or not user_name.isalpha():
    user_name = input("The input field must not be left blank.\n"
                      "The user name must not contain any spaces, "
                      "only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
"Name: "
print("Hi,", str(user_name) + "!" + " The game starts now")
# End player name

questions = {
    "Which geografical location is Sweden?: ": "C",
    "How old is Sweden as a country?: ": "D",
    'How big is Sweden in square kirometres? ': 'B',
    'When was Sweden founded as a country? ': 'C',
    'What currency does Swedes use? ': 'A',
    'Which of these are Sweden neighbouring countries? ': 'D',
    'How many languages does Swedes speak? ': 'A',
    'How many countries speak Swedish as official language? ': 'C',
    'What is Swedish best dish? ': 'D',
    'Which music band is the most popular in Sweden? ': 'B'
}

options = [[
    'A. Eastern Europe', 'B. Western Europe',
    'C. Northern Europe', 'D. Middle East'
    ],
    [
        'A. Over 100 years', 'B. Over 500 years',
        'C. Over 50 years',  'D. Over 1000 years'
        ],
    [
        'A. About 500295 km', 'B. About 450295 km',
        'C. About 250295 km', 'D. About 100295 km'
             ],
        [
            'A.1823', 'B.1553', 'C. 1523', 'D. 1630'],
        [
            'A. Kronor (SEK)', 'B. Euro', 'C. NOK', 'D. USD'],
        [
            'A. Germany and Poland', 'B. Italy and Spain',
            'C. Holand and Hungary', 'D. Finland and Norway'],
        [
            'A. Approximately 200 languages', 'B. Approximately 300 languages',
            'C. Only one language', 'D. Only two official languages'],
        [
            'A. Three countries', 'B. Up to thirty countries',
            'C. Two countries', 'D. Only one country'],
        [
            'A. Smögås', 'B. Potato chips', 'C. Kebab pizza',
            'D. Köttbullar potatismos, gräddsås recipe'],
        [
            'A. Swedish House Mafia', 'B. Abba', 'C. Roxette', 'D. Europe']]

correct_answer = ("C", "D", "B", "C", "A", "D", "A", "C", "D", "B")

guesses = []
score = 0
que_number = 0

# Display all questions
for que in questions:
    print("------------------------------")
    print(que)

# Display options
    for choice in options[que_number]:
        print(choice)

    player_choice = input("Make a choice (A, B, C, D): ").upper()
    guesses.append(player_choice)
    if player_choice == correct_answer[que_number]:
        score += 1
        print("Your answer is correct!")  # Print only when user answer is correct
    else:
        print("Wrong answer!")  # Print when user answer is wrong
        print()
        print(f"The answer is {correct_answer[que_number]} ")  # print correct answer

    que_number += 1
    