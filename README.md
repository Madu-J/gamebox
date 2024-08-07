# Gamebox App - Project 3
![Gamebox app]()

Gamebox App live link - https://gamebox-quiz-app-bd65f9b140e9.herokuapp.com/

### Introduction to the project

The program created is an online quiz game on things to know about sweden

[Delpoyed link](https://gamebox-quiz-app-bd65f9b140e9.herokuapp.com/) Leads to my deployed project.

###  Gamebox App Heading

- Featured at the top of the page is the Gamebox app heading and is easy to see for the users.
Upon viewing the page, the user will be able to see the name of the game and a start game button!

![Gamebox heading](readme/gamebox-heading.png)

### Gameplay

First, the player is asked if he wants to play giving option to play or quit. If player choses "y" the game rules will be displayed but if the player input is not "y", the game ends. If player input is y and the game rules is displayed, the player is asked to type "s" to start or "q" to quit. If the player input is not "s", the game end but if the player input is "s" indicating interest in playing the game, the player is asked to enter his name. This allows the computer to address the player directly. When the game has started.

### Target audience

- People who like Browsergamers.
- People who want to pass some free time.
- People who want to like quiz game.

### User story

As a first time user of the game, you want to:
- As a first-time user I want to easily understand what the site main purpose is all about.
- As first-time user I use my phone often, so I want to view the website content clearly on my mobile.
- As a first-time user I want to found the site interesting.
- Play a bug-free game.
- Play a self-explanatory game.
- Be able to navigate easily over the terminal window.
- I would like to be able to read the rules of the game.

As a frequent user of the website, you want to:
- Repeat the game experience.
- Improve the last game result.

Objectives of the website operator is to:
- Provide an easy to navigate and to play game.
- Provide a feedback of all user inputs.
- Provide an error free game.
- Provide an entertaining diversion to pass the time.

How this requirements are met:
- The game will be free to play.
- There will be a welcome screen from which the player can navigate.
- All important elements will be shown in the terminal.
- A response is given to every user input, especially if the input is not expected by the computer.
- The player can see the rules of the game.
- There is always the possibility to quit the game before the quiz starts.

## Purpose
Gamebox App is a quiz app designed for people to engage their mind or test their knowledge in a kind coffee break situation. You can find the live link here - [Delpoyed link](https://gamebox-quiz-app-bd65f9b140e9.herokuapp.com/)

 Gamebox is easy to play game app, perfect for who want to try out new things. User will go by choosing their prefer answers within the aphabet A, B, C and D.

The quiz has 10 questions in total and the player gets 10% per point on each question answered correctly.

The questions flow in orderly, one after the other as next question displays once user picks an answer.

At the end of the quiz the app displays user scores by percentage.

This quiz game app demonstrate how Python works in a real-world context, and can be played by anyone who finds it interesting. The questions are carefully selected to make user to want to play more.

The site is a fully responsive python game that will allow users to read a question regardless of the screen size.

![Responsive Mockup](readme/responsive.png)

## Features

### Existing Features

### The Game Area

- The quiz game site has a welcome message for user followed by a question if user wants to play the quiz.

![Gamebox user welcome note](readme/welcome.png)

- If user types y then the quiz rules will be displayed but if user types n or any other input then the game ends.
![Gamebox App rules](readme/game-rules.png)
![Gamebox App quit](readme/quit-game.png)

- Once the user types in an answer, its irreversible. If player is correct it will display "Weldone! The answer is correct!" and 
 and if user input is not A, B, C OR D it will print Invalid input telling user to choose A,B,C,D. And if the answer is incorrect, it will print "Wrong Answer" and print the correct answer

![Invalid input](readme/invalid-input.png)

![Correct](readme/correct.png)

![Wrong Answer](readme/wrong.png)

- At the end of the game, the user will get a thank you message followed by their score and as well a message to direct the user where to click if user wants to try again.
![Thank you for playing](readme/result.png)

### The Score Area

- The user will only see result at the end of the game.

![score](readme/secore.png)
![answers](readme/answers.png)

### Features Left to Implement
- Time to answer each question
## Testing

### Validator Testing
- I have tested this project code by:
- Pasting the code on PEP8 linter and there were no error found. ![PEP8 Python Validation](readme/validationfixed.png)
- Tested after deployment on Code Institute Heroku terminal and it run successfully.

### Debug

- Wrong identation fixed. ![PEP8 Python Validation](readme/validation.png)
![PEP8 Python Validation](readme/no-error.png)


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku and the steps for deployment are as followed:
### First step
- Sign in to Heroku app
- Create a new app with a unique name
- Go to setting and create a _Config Var_ called `PORT`. Set the value to `8000`
- Then click on  buildpacks and add the following:
1. `heroku/python`
2. `heroku/nodejs`

### Second step
- Click on deploy at the top left side and select github to connect to github. Confirm your connection and 
  search for the github repository name, click connect to link up the Heroku app earlier creacted with the repository.
- Choose either automatic deploy or manual. I used manual which is deploy branch.
- Allow the app to build until it shows successfully then click view and it takes me to my live deployed link.

## Credit 
- Bro Code Youtube Channel
- Google Search Engine

<br>

[Back to top](#top)
