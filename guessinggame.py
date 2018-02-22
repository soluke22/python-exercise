#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
while True:
  rand=random.randint(1,9)
  user=int(input("Choose a number between 1 and 9:"))
  if int(user) == int(rand):
    print("That's exactly right!")
    exit=input("Type 'exit' to quit. Type anything else to continue.")
    if exit.lower() == "exit":
      break
    else:
      print("")
  elif int(user) > int(rand):
    print("Too high, try again!")
    exit=input("Type 'exit' to quit. Type anything else to continue.")
    if exit.lower() == "exit":
      break
    else:
      print("")
  else:
    print("Too low, try again!")
    exit=input("Type 'exit' to quit. Type anything else to continue.")
    if exit.lower() == "exit":
      break
    else:
      print("")
