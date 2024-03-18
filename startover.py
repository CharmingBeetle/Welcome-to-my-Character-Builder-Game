import os
import time
import random

def rollDice(sides):
  dice = random.randint(1, sides)
  return dice

def health(): 
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  hlth = ((dice6 * dice12) / 2) + 10
  return hlth

def strength():
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  str = ((dice6 * dice12) / 2) + 12
  return str

#Generate character 1
def generatechar1(name, type, health, strength):
  name1 = name
  type1 = type

  name = input("What is your character's name? ")
  type = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
  print("Your character is", name, "and is a", type)

  health1 = health()
  strength1 = strength()
  
  return name1, type1, health1, strength1

#Generate character 2
def generatechar2(name, type, health, strength):
  name2 = name
  type2 = type
  
  name2 = input("What is your character's name? ")
  type2 = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
  print("Your character is", name2, "and is a", type2)

  health2 = health()
  strength2 = strength()

  return name2, type2, health2, strength2

# Character Damage 
def chardmg():
  strDiff = abs(generatechar1(strength) - generatechar2(strength))
  dmg = (strDiff) + 1
  return dmg

#Battle by rolling dice 
def battle():
  battlecnt = 0
  name1 = generatechar1()
  name2 = generatechar2()
  hea
  
  while True:
    char1dice = rollDice(6)  
    char2dice = rollDice(6)
    print("Currently rolling dice...🎲")
    time.sleep(1)
    os.system("clear")
    print("Currently rolling dice...🎲🎲")
    time.sleep(1)
    os.system("clear")
    print("Currently rolling dice...🎲🎲🎲")
    time.sleep(1)
    os.system("clear")
    if char1dice > char2dice:
  
      print(name1, "wins the first blow")
    else:
      print(name2, "wins the first blow")
      
      print(name1, "has", hlth, "and", str, "and", name2, "has", hlth)
      
      continue

      if generatechar1(name, type, health <=0, strength):
        print("Oh no", name1, "has died!")
        time.sleep(2)
        os.system("clear")
        end = input("Would you like to play again? ")
        if end == "yes":
          continue

      elif generatechar2(name, type, health <=0, strength):
        print("Oh no", name2, "has died!")
        time.sleep(2)
        os.system("clear")
        end = input("Would you like to play again? ")
        if end == "yes":
          continue


  print("Welcome to the World of Warcraft Character Builder! 🎊")
  time.sleep(2)
  os.system("clear")

  
  

generatechar1(name)
generatechar2(name)
battle()
