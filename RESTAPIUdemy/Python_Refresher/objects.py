#!/bin/python
# Simple programming using JSON and classes and objects

# Simple JSON objects
lottey_player = {
    'name' : 'Rolf',
    'number' : (1,2,3,4,5,6,7)
}

players = {
    'player1' : {
        'name' : 'joe',
        'numbers' : (1,2,3,4,5)
    },
    'player2' : {
        'name' : 'mike',
        'numbers' : (7,6,3,2,5)
    },
    'player3' : {
        'name' : 'yass',
        'numbers' : (1,4,6,3,1)
    },
    'player4' : {
        'name' : 'tim',
        'numbers' : (1,7,4,22,1)
    }
}

class LotteryPlayer:

    # this acts like a constructor method
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers 

    # return method for name
    def total(self):
        return sum(self.numbers)

# We can make internal data objects from the JSON data
player_one = LotteryPlayer(players['player1']['name'],players['player1']['numbers'])
player_two = LotteryPlayer(players['player2']['name'],players['player2']['numbers'])


print(player_one.name == player_two)

# We loop over one player
for number in player_one.numbers:
    if number == 7:
        print(player_one.name, " won!")
    else: 
        print(player_one.name + " nothing to won.")

# We can also loop over the the JSON objects
# Use items() to iterate across dictionary
for playerno, playerinfo  in players.items():
    print(playerno, playerinfo)
    for number in playerinfo['numbers']:
        if number == 7:
            print(playerno + " is " + playerinfo['name'] + " and has the number 7")
   
# We can calculate the average number picked by the users.
total = 0
average = 0
number_of_players = 0
for playerno, playerinfo  in players.items():
    total = total + sum(playerinfo['numbers'])
    number_of_players = number_of_players + 1
print("The total is: " + str(total) + " Number of players: " + str(number_of_players))
print ('The average numbers of the number is ' + str(total/number_of_players))    