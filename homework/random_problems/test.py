import random

def exercise_one():
	count = 3
	while True:
		user_input = input("child: why???")
		count -= 1
		print("partent: because")
		if str(user_input).lower() == "stop":
			print(count)
			break


def exercise_two():
	pass



options = {"rock", "paper", "scissors"}
game_limit = 3
player1 = {"hand": 0, "score":0} 
player2 = {"hand": 0, "score":0} 

def game():
	pass
	while game_limit > 0:
		player1["hand"] = options[random.random(len(options))]
		player2["hand"] = options[random.random(len(options))]
		if player1["hand"] == player2["hand"]:
			print("tie")
		elif player1["hand"] == "rock" &&  player2["hand"] == "paper"
if __name__ == "__main__":
	exercise_one()

