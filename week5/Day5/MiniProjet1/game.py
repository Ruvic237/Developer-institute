# program with a Game class which will have functions 
# to play a single game of rock-paper-scissors against the computer,
# determine the game’s result, and return the result.

import random

class Game(): #class game with four methods
    
    def __init__(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        self.winner = self.get_game_result()
        
    @staticmethod
    def get_user_item(): #method to get user input
        
        user_item = input("Make a choice btw (rock/paper/scissors) \n")
        choice1 = ["rock","paper","scissors"]
        
        for i in choice1: # loop through the list of options
            
            if i == user_item:
                return user_item
            
            while user_item not in choice1:
                user_item = input("Make a choice btw (rock/paper/scissors) \n") 
    @staticmethod
    def get_computer_item(): #method for computer choice
        
        choice2 = ["rock","paper","scissors"]
        computer = random.choice(choice2)
        return computer
    
    def get_game_result(self): #method to display winner
        if self.user_item == "rock" and self.computer_item == "paper":
            return "computer won"
        if self.user_item == "rock" and self.computer_item == "scissors":
            return "user won"
        if self.user_item == "paper" and self.computer_item == "rock":
            return "user won"
        if self.user_item == "scissors" and self.computer_item == "rock":
            return "computer won"
        if self.user_item == "rock" and self.computer_item == "rock":
            return "draw"
        if self.user_item == "paper" and self.computer_item == "scissors":
            return "computer won"
        if self.user_item == "scissors" and self.computer_item == "paper":
            return "user won"
        if self.user_item == "paper" and self.computer_item == "paper":
            return "draw"
        if self.user_item == "scissors" and self.computer_item == "scissors":
            return "draw"
    
    def play(self):  
        if self.winner == "draw":     
           print(f'user 1 selected {self.user_item} and computer selected {self.computer_item} so there is draw')
        else:
            print(f'user 1 selected {self.user_item} and computer selected {self.computer_item} so the winner is {self.winner}')
                       
test = Game()

# test.get_user_item()
# test.get_computer_item()
test.play()





   
    