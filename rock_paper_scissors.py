import random

class Game:
    def __init__(self, user_name):
        self.user_name = user_name
        # Points counter
        self.points = 0
        # Reading rating file
        self.rating = open('rating.txt', 'r')
        self.user_points = self.rating.readlines()
        self.rating.close()
        # Read every name in file lines and compare with the name of the player
        for n in self.user_points:
            if self.user_name in n:
                # If the user exists count the number of indexes and add one (the blank space)
                self.user_score = len(self.user_name) + 1
                # Take every index after the blank space and convert it on in an integer
                self.data = (int(n[self.user_score:]))
                # Setup this value as started point for self.points
                self.points = self.data
        self.rating.close()

    def welcome (self):
        print(f'Hello, {self.user_name}')
        self.user_options = input().split(',') # User list
        self.user_options.reverse()
        print('Okay, let\'s start')
        self.user_dict = {}
        look = len(self.user_options) // 2
        items = self.user_options + self.user_options[:look]
        for j,i in enumerate(self.user_options):
            self.user_dict[i] = items[j+1 : j+1+look]

    def play (self, user_choice):
        if len(self.user_options) == 1:
            self.options = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        else:
            self.options = self.user_dict

        self.user_choice = user_choice
        self.comp = random.choice(list(self.options))
        if self.user_choice == '!exit':
            print('Bye!')
            exit()
        elif self.user_choice == '!rating':
            print(f'Your rating: {self.points}')
        elif self.user_choice not in list(self.options):
            print('Invalid input')
        elif  self.user_choice in self.options[self.comp]:
            print(f"Sorry, but computer chose {self.comp}")
        elif self.comp in self.options[self.user_choice]:
            print(f"Well done. Computer chose {self.comp} and failed")
            self.points += 100
        elif self.user_choice == self.comp:
            print(f"There is a draw ({self.comp})")
            self.points += 50

player = Game(input('Enter your name:'))
player.welcome()

while True:    
    player.play(input())