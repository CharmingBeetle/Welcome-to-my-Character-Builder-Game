import os
import random
import time


def rollDice(sides):
  dice = random.randint(1, sides)
  return dice

def health(): 
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  hth = ((dice6 * dice12) / 2) + 10
  return hth

def strength():
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  st = ((dice6 * dice12) / 2) + 12
  return st

def charDmg(char1str, char2str):
  strDiff = abs(char1str - char2str)
  dmg = (strDiff) + 1
  return dmg

global char1Health
global char2Health
char1Health = health()
char2Health = health()

def startGame():
  print("Welcome to War of the Worlds Character Builder! 🎊")
  time.sleep(2)
  os.system("clear")

def battle():
  global winBattle
  global char1Health
  global char2Health
  winBattle = 0
  char1Health = health()
  char2Health = health()

  while True:
    winBattle += 1
    char1dice = rollDice(6)  
    char2dice = rollDice(6)
    dmg = charDmg(char1str, char2str)

    print("Currently rolling dice...🎲")
    time.sleep(1)
    os.system("clear")
    print("Currently rolling dice...🎲🎲")
    time.sleep(1)
    os.system("clear")
    print("Currently rolling dice...🎲🎲🎲")
    time.sleep(1)
    os.system("clear")

    print(name1, "rolled a", char1dice, "and", name2, "rolled a", 
  char2dice, "...")
    time.sleep(3)
    os.system("clear")

    if char1dice > char2dice:
      winBattle += 1
      char2Health -= dmg
      print(name1,"wins the blow this round!")
      time.sleep(2)
      os.system("clear")
      print(name2,"takes a hit, with", dmg, "damage")
      time.sleep(2)
      os.system("clear")
      print("Current status: ", name1, "has", char1Health, "health and", name2, "has", char2Health, "health")
      time.sleep(2)
      os.system("clear")

    elif char2dice > char1dice:
        winBattle += 1
        char1Health -= dmg
        print(name2, "wins the the blow this round!")
        time.sleep(2)
        os.system("clear")
        print(name1, "takes a hit, with", dmg, "damage")
        time.sleep(2)
        os.system("clear")
        print("Current status: ", name1, "has", char1Health, "health and", name2, "has", char2Health, "health")
        time.sleep(2)
        os.system("clear")

    else:
        print("It's a draw!")
        time.sleep(2)
        os.system("clear")

while True:
  startGame()
  #Character 1
  name1 = input("What is your first character's name? ")
  print()
  type1 = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
  print("Your first character is", name1, "and is a", type1)
  time.sleep(1)
  char1Health = health()
  print("Health:", char1Health)
  time.sleep (1)
  char1str = strength()
  print("Strength:", char1str)
  print()
  time.sleep(1)

  print("Who are they battling? ")
  print()
  time.sleep(1)

  #Character 2
  name2 = input("What is your second character name?: ")
  type2 = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
  print("Your second character is", name2, "and is a", type2)
  time.sleep(1)
  char2Health = health()    
  print("Health:", char2Health)
  time.sleep (1)
  char2str = strength()
  print("Strength:", char2str)
  time.sleep(2)
  os.system("clear")

  print("Let the battle begin!")
  time.sleep(3)
  os.system("clear")

  battle()


    #Who won?
  if char1Health <= 0:
        print("Oh no", name1, "has died!")
        print("Game over!", name2, "won in", winBattle, "rounds")
        time.sleep(2)
        os.system("clear")
        end = input("Would you like to play again? ")
        if end == "yes":
              char1Health = health()
              char2Health = health()
              startGame()
        else:
              exit()

  elif char2Health <= 0:
        print("Oh no", name2, "has died!")
        print("Game over!", name1, "won in", winBattle, "rounds")
        time.sleep(2)
        os.system("clear")
        end = input("Would you like to play again? ")
        if end == "yes":
              startGame()
  else:
        exit()



