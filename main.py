# all imports
import random
from tkinter import *

# important variables
root = Tk()  # creates a new window
winScore = 0  # the win score of our game which we'll be using later on
loseScore = 0  # the lose score of our game which we'll be using later on
tieScore = 0  # the tie score of our game which we'll be using later on

# window functions
root.geometry("420x420")  # Changes window height and width
root.title("RPS game")  # Changes window title
root.config(background="#36393E")

# button callback functions


def detectWin(player_guess, computer_guess):
    global winScore, loseScore, tieScore

    # Tie event
    if (player_guess == 'rock' and computer_guess == 'rock') or (player_guess == 'paper' and computer_guess == 'paper') or (player_guess == 'scissors' and computer_guess == 'scissors'):
        tieScore += 1
        return f"Its a tie! The computer choose {computer_guess} and you choose {player_guess} too."

    # lose or win
    if (player_guess == 'rock' and computer_guess == 'scissors') or (player_guess == 'paper' and computer_guess == 'rock') or (player_guess == 'scissors' and computer_guess == 'paper'):
        winScore += 1
        return f"You win! The computer choose {computer_guess} and you choose {player_guess}."

    elif(player_guess == 'rock' and computer_guess == 'scissors') or (player_guess == 'paper' and computer_guess == 'rock') or (player_guess == 'scissors' and computer_guess == 'rock'):
        loseScore += 1
        return f"You lose! The computer choose {computer_guess} and you choose {player_guess}."


def rock():
    playerGuess = 'rock'
    options = ['rock', 'paper', 'scissors']
    computerGuess = random.choice(options)

    loseOrWin = detectWin(playerGuess, computerGuess)

    resultLabel.config(text=loseOrWin)


def paper():
    playerGuess = 'paper'
    options = ['rock', 'paper', 'scissors']
    computerGuess = random.choice(options)

    loseOrWin = detectWin(playerGuess, computerGuess)

    resultLabel.config(text=loseOrWin)


def scissors():
    playerGuess = 'scissors'
    options = ['rock', 'paper', 'scissors']
    computerGuess = random.choice(options)

    loseOrWin = detectWin(playerGuess, computerGuess)

    resultLabel.config(text=loseOrWin)


def quitRoot():
    root.destroy()


def quit():
    resultLabel.config(
        text=f"Thanks for playing! You won {winScore} rounds, lost {loseScore} rounds and had {tieScore} ties.")
    root.after(2000, quitRoot)


# all elements
resultLabel = Label(root,
                    text="",
                    background="#36393E",
                    foreground="white")

rockButton = Button(root, text="rock",
                    command=rock,
                    height=1,
                    width=7,
                    background="#f5f5f5",
                    foreground="#36393E")

paperButton = Button(root,
                     text="paper",
                     command=paper,
                     height=1,
                     width=7,
                     background="#f5f5f5",
                     foreground="#36393E")

scissorsButton = Button(root,
                        text="scissors",
                        command=scissors,
                        height=1,
                        width=7,
                        background="#f5f5f5",
                        foreground="#36393E")

quitButton = Button(root,
                    text="quit",
                    command=quit,
                    height=1,
                    width=7,
                    background="#f5f5f5",
                    foreground="#36393E")

# packing/displaying every element
resultLabel.place(x=210,
                  y=350,
                  anchor="center")

rockButton.place(x=110,
                 y=50,
                 anchor="center")

paperButton.place(x=210,
                  y=50,
                  anchor="center")

scissorsButton.place(x=310,
                     y=50,
                     anchor="center")

quitButton.place(x=210,
                 y=100,
                 anchor="center")

# mainloop function
root.mainloop()
