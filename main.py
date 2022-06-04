import random

while True:
   options = ["R", "P", "S"]
   computer = random.choice(options)
   player = None

   while player not in options:

      player = input("Pick an option between 'R', 'P', 'S': ").upper()

   if player == "R" and computer == "R":
      print("Player (Rock): computer (Rock)")
      print("Tie!")

   if player == "P" and computer == "P":
      print("Player (Paper): computer (Paper)")
      print("Tie!")
   
   if player == "S" and computer == "S":
      print("Player (Scissors): computer (Scissors)")
      print("Tie!")

   elif player == "R":
      if computer == "P":
         print("computer(Paper)")
         print("Player(Rock)")
         print("You Lose!")
      if computer == "S":
         print("computer(Scissors)")
         print("Player(Rock)")
         print("You Win!")

   elif player == "S":
      if computer == "R":
         print("computer(Rock)")
         print("Player (Scissors)")
         print("You Lose!")
      if computer == "P":
         print("computer(Paper)")
         print("Player (Scissors)")
         print("You Win!")

   elif player == "P":
      if computer == "S":
         print("computer(Scissors)")
         print("Player (Paper)")
         print("You Lose!")
      if computer == "R":
         print("computer(Rock)")
         print("Player (Paper)")
         print("You Win!")

   play_again = input("Play again? (yes/no): ").lower()         

   if play_again != "yes":
      break

print("bye!")




