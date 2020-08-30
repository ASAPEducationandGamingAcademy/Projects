print("Welcome to my first adventure game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

if age >= 10:
	print("You are old enough to play!")
else:
	print("You cannot play without supervision, please get an adult to play this game")
	exit()
	
wants_to_play = input("Do you want to play (yes / no)? ").lower()
if wants_to_play == "yes":
	print("You are starting with", health, "health")
	print("Let's play!")
		
	left_or_right = input("First choice... Left or Right (left / right) ").lower()
	if left_or_right == "right":
		print("You lost the game. Please feel free to play again.")
		
	elif left_or_right == "left":
		ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around or go back to the start(across / around / back to start) ").lower()
			
		if ans == "around":
			print("You went around and reached the other side of the lake")
	
		elif ans == "back to start":
			print("You lost the game!")
		# break
			
		elif ans == "across":
			print("You managed to get across, but were bit by a fish and lost 5 health")
			health -= 5
			health = 5
			print("You have", health, "health")
				
			if ans == "across":
				health = 5

		if ans != "back to start":		
			ans = input("You notice a house, river, and a forest. Which do you go to (house / river / forest)? ")
			if ans == "house":
				print("You lost 5 health because the man in the house cooked you up!")
				health -= 5
				if health == 0:
					print("You lost the game, please feel free to play again")
				else:
					print("You have managed to win, thanks for playing.")
					
			if ans == "river":
				health -= 2.5
				if health == 5:
					health = 2.5
				elif health == 10:
					health = 7.5
				if health > 0:
					print("You have", health, "health")
					print("You managed to survive, and won the game")
				else:
					print("You lost the game")
				
			elif ans == "forest":
				print("You managed to get through the forest")
				if health == 10:
					print("You have 10 health")
				elif health != 10:
					print("You have 5 health")
