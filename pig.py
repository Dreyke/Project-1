__author__ = 'Dreyke Boone'

import random

# class to roll die
class Dice():

    # gets a random integer and returns its value
    def roll(self):
        self.value = random.randint(1,6)
        return self.value

class Points():

    # constructor method with instance variables
    def __init__(self, turnTotal, player, playerCount, score, finalScore):
        self.turnTotal = turnTotal
        self.player = player
        self.playerCount = playerCount
        self.score = score
        self.finalScore = finalScore

def main():

    # game object - sets up instance variables of constructor method
    game = Points(0, 0, 2, [0] * 2, 20)

    # while loop to run the game. Loop ends when a player wins.
    while max(game.score) < game.finalScore:

        # ask user if they would like to roll or pass. Displays their total score and their accumulative score for their
        # turns.
        playerRoll = input("\nPlayer %i: Do you want to roll the die? (Y or N)"
                        "\n(Your Total Score = %i, Your Current Score = %i) "
                        % (game.player, game.score[game.player], game.turnTotal)) in {'yes', 'y', ''}

        # loop, with nested loops, to roll dice, keep track of score, and player turn
        if playerRoll:
            # dieRoll object to get a random value from the Die class
            diceRoll = Dice().roll()
            print(' You rolled %i' % diceRoll)

            # loop to track if player rolls a 1. If they do, they lose their score for that round. Goes to next players turn
            if diceRoll == 1:
                print(' You rolled a 1. You lose %i points but still keep your previous %i'
                      % (game.turnTotal, game.score[game.player]))
                game.turnTotal, game.player = 0, (game.player + 1) % game.playerCount
            else:
                game.turnTotal += diceRoll
        else:
            game.score[game.player] += game.turnTotal
            if game.score[game.player] >= game.finalScore:
                break
            print(' Player %i is sticking with %i points' % (game.player, game.score[game.player]))
            game.turnTotal, game.player = 0, (game.player + 1) % game.playerCount

    # display winners score
    print('\nPlayer %i wins with a total score of %i' % (game.player, game.score[game.player]))

main()