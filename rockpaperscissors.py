
#make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

while True:
  print("Welcome to Two-Player Rock-Paper-Scissors!")
  player1_choice=input("Player 1, choose Rock, Paper, or Scissors:")
  player2_choice=input("Player 2, choose Rock, Paper, or Scissors:")
  if player1_choice.lower() == "rock" and player2_choice.lower() == "rock":
    print("You guys tied!")
    playagain = input("Do you want to play again?: (y/n)")
    if playagain.lower() == "n":
      print("Thanks for playing!")
      break
    else:
        print("Another round!")
  elif player1_choice.lower() == "rock" and player2_choice.lower() == "scissors":
    print("Player 1 won!")
    playagain = input("Do you want to play again?: (y/n)")
    if playagain.lower() == "n":
      print("Thanks for playing!")
      break
    else:
      print("Another round!")
  elif player1_choice.lower() == "rock" and player2_choice.lower() == "paper":
    print("Player 2 won!")
    playagain = input("Do you want to play again?: (y/n)")
    if playagain.lower() == "n":
      print("Thanks for playing!")
      break
    else:
      print("Another round!")
  else:
    if player1_choice.lower() == "paper" and player2_choice.lower() == "paper":
      print("You guys tied!")
      playagain = input("Do you want to play again?: (y/n)")
      if playagain.lower() == "n":
        print("Thanks for playing!")
        break
      else:
        print("Another round!")
    elif player1_choice.lower() == "paper" and player2_choice.lower() == "scissors":
      print("Player 2 won!")
      playagain = input("Do you want to play again?: (y/n)")
      if playagain.lower() == "n":
        print("Thanks for playing!")
        break
      else:
        print("Another round!")
    elif player1_choice.lower() == "paper" and player2_choice.lower() == "rock":
      print("Player 1 won!")
      playagain = input("Do you want to play again?: (y/n)")
      if playagain.lower() == "n":
        print("Thanks for playing!")
        break
      else:
        print("Another round!")
    else:
      if player1_choice.lower() == "scissors" and player2_choice.lower() == "scissors":
        print("You guys tied!")
        playagain = input("Do you want to play again?: (y/n)")
        if playagain.lower() == "n":
          print("Thanks for playing!")
          break
        else:
          print("Another round!")
      elif player1_choice.lower() == "scissors" and player2_choice.lower() == "paper":
        print("Player 1 won!")
        playagain = input("Do you want to play again?: (y/n)")
        if playagain.lower() == "n":
          print("Thanks for playing!")
          break
        else:
          print("Another round!")
      elif player1_choice.lower() == "scissors" and player2_choice.lower() == "rock":
        print("Player 2 won!")
        playagain = input("Do you want to play again?: (y/n)")
        if playagain.lower() == "n":
          print("Thanks for playing!")
          break
        else:
          print("Another round!")
      else:
        print("Choose rock, paper or scissors and try again!")
