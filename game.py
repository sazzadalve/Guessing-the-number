import random
import logo

def guess_number(number):
  option = input("Choose the difficulty. Type 'easy' or 'hard'\n").lower()
  if option == "easy":
    time = 10
  elif option == "hard":
    time = 5
  else:
    print("Invalid input")
    return guess_number(number)
  print(f"You have {time} attempts remaining to guess the number")
  while time > 0:
    my_guess = int(input("Guess the number\n"))
    if my_guess == number:
      print("You win")
      break
    elif my_guess > number:
      print("Too high")
      time -= 1
    elif my_guess < number:
      print("Too low")
      time -= 1
    else:
          print("Invalid input")
    if time == 0:
      print("You lose")
      print(f"The number is {number}")
      break
    print(f"You have {time} attempts remaining to guess the number")
print(logo)
number = random.randint(1, 100)
guess_number(number)