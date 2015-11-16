import random

rand = random.randint(1, 10)
guessed_nums = []
max_guesses = 5

while len(guessed_nums) < max_guesses:
  guess = input("Please guess a number between 1 and 10: ")

  try:
    player_num = int(guess)
  except:
    print("That isn't a whole number!")
    break

  if not player_num > 0 or not player_num < 11:
    print("The number has to be between 1 and 10!")
    break

  guessed_nums.append(player_num)

  if player_num == rand:
    print("Congratulations! My number was {}".format(rand))
    print("It took you {} tries!".format(len(guessed_nums)))
    break
  else:
    if player_num < rand:
      print("Nope! My number is higher than {}. Guess #{}".format(player_num, len(guessed_nums)))
    else:
      print("Nope! My number is lower than {}. Guess #{}".format(player_num, len(guessed_nums)))
    continue

if not rand in guessed_nums:
  print("Sorry! My number was {}".format(rand))
