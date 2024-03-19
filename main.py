import os, time, random
from replit import audio

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
  

def startGame():
  source = audio.play_file('theduel.mp3')
  source.paused = False # unpause the playback
  print('\033[35m'+"Welcome to War of the Worlds Character Builder! 🧨🏹🗡 ")
  time.sleep(2)
  os.system("clear")
  print('\033[34m',"Let's build your character!")
  time.sleep(2)
  os.system("clear")
  
  while True:
  
    #Character 1
    name1 = input('\033[36m'+"What is your first character's name? ")
    print()
    type1 = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
    print('\033[33m'+"Your first character is", name1, "and is a", type1)
    time.sleep(1)
    char1health = health()
    print("Health:", char1health)
    time.sleep (1)
    char1str = strength()
    print("Strength:", char1str)
    time.sleep(1)
    print()
    print('\033[30m'+"Who are they battling? ")
    time.sleep(1)
    print()
  
    #Character 2

    name2 = input('\033[36m'+"What is your second character name?: ")
    type2 = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc):")
    print('\033[33m'+"Your second character is", name2, "and is a", type2)
    time.sleep(1)
    char2health = health()    
    print("Health:", char2health)
    time.sleep (1)
    char2str = strength()
    print("Strength:", char2str)
    time.sleep(2)  
    print()
    os.system("clear")
  
    print('\033[31m'+"Let the battle begin!⚔🪓🏹")
    time.sleep(3)
    os.system("clear")
  
  #Battle
    winBattle = 0
    while True:
      winBattle += 1
      char1dice = rollDice(6)  
      char2dice = rollDice(6)
      dmg = charDmg(char1str, char2str)
        
      print('\033[31m'+"Currently rolling dice...🎲")
      time.sleep(1)
      os.system("clear")
      print("Currently rolling dice...🎲🎲")
      time.sleep(1)
      os.system("clear")
      print("Currently rolling dice...🎲🎲🎲")
      time.sleep(1)
      os.system("clear")
           
      print('\033[32m'+ name1, "rolled a", char1dice, "and", name2, "rolled a", char2dice, "...")
      time.sleep(3)
      os.system("clear")
  
      if char1dice > char2dice:
        winBattle += 1
        char2health -= dmg
        if winBattle == 1:
          print('\033[35m'+ name1,"wins the first blow! 💪");
        else:
          print('\033[35m'+ name1,"wins round", winBattle, "and deals", dmg)
        time.sleep(2)
        os.system("clear")
        print('\033[33m'+ "Current status:", name1, "has", char1health, "health and", name2, "has", char2health, "health")
        time.sleep(2)
        os.system("clear")
  
      elif char2dice > char1dice:
        winBattle += 1
        char1health -= dmg
        if winBattle == 1:
          print('\033[35m'+ name2,"wins the first blow! 💪");
        else:
          print('\033[35m'+ name2,"wins round", winBattle, "and deals", dmg)
          time.sleep(2)
          os.system("clear")
          print('\033[33m'+ "Current status:", name1, "has", char1health, "health and", name2, "has", char2health, "health") 
          time.sleep(2)
          os.system("clear")
          
      else:
          print("It's a draw!")
          time.sleep(2)
          os.system("clear")
          
  
      #Who won?
      if char1health <= 0:
        print('\033[31m'+ "Oh no", name1, "has died!")
        print("Game over!", name2, "won in", winBattle, "rounds")
        time.sleep(2)
        os.system("clear")
        end = input("Would you like to play again? ")
        if end == "yes":
          os.system("clear")
          startGame()
          continue
        else:
          exit()
  
      elif char2health <= 0:
        print('\033[31m'+"Oh no", name2, "has died!")
        print("Game over!", name1, "won in", winBattle, "rounds")
        time.sleep(2)
        os.system("clear")
        end = input('\033[32m'+"Would you like to play again? ")
        if end == "yes":
          os.system("clear")
          startGame()
          continue
        else:
          source.paused = True # pause the playback
          exit()
        


startGame()
