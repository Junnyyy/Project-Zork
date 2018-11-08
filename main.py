import random

# Floor 1-3
floor3 = ['sword', 'stairs down', 'nothing', 'boss monster', 'prize']
floor2 = ['magic stone', 'stairs up', 'monster', 'stairs down', 'nothing']
floor1 = ['nothing', 'sword', 'monster', 'stairs up', 'sword']
# inventory, user room, and user floor variables 
inventory = [0,0,0]
user_room = 0
user_floor = floor1
game_over = 0
last = 'grab'
print("Welcome unfortunate victim, this is a test of your skills in combat and how fast you can think on your feet.  Currently you are locked in a warehouse there are 3 normal 'guests' and one very very special 'guest'. Can you defeat the 'guests' and retrieve the key to escape?  Which room on this floor would you like to go to? Or maybe you'd like to go to a different floor? Type 'help' for the commands.\n")
# if statements for game function
while game_over == 0:
  if user_floor[user_room] == 'nothing':
    print("This room has nothing in it.")
  elif user_floor[user_room] == 'sword':
    print("This room has a sword in it!")
  elif user_floor[user_room] == 'magic stone':
    print("This room has magic stones in it!")
  elif user_floor[user_room] == 'stairs up':
    print("This room has stairs going up.")
  elif user_floor[user_room] == 'stairs down':
    print("This room has stairs going down.")
  elif user_floor[user_room] == 'monster':
    print("There is a monster in the room with you.")
  x = input("What do you do?")
  if x == 'help':
    print("left, right, up, down, grab, fight, help, end")
  elif x == 'left':
    if user_floor[user_room] == 'monster' and last == 'left':
      print("You can pass the monster without a fight.")
    elif user_room > -1:
      user_room -= 1
    else:
      print("You run straight into a wall.")
  elif x == 'right':
    if user_floor[user_room] == 'monster' and last == 'right':
      print("You can pass the monster without a fight.")
    elif user_room < 5:
      user_room += 1
    else:
      print("You run straight into a wall")
  elif x == 'up':
    if user_floor[user_room] == 'stairs up':
      if user_floor == floor1:
        user_floor = floor2
        print("You went up the stairs")
      elif user_floor == floor2:
        user_floor = floor3
        print("You went up the stairs")
  elif x == 'down':
    if user_floor[user_room] == 'stairs down':
      if user_floor == floor2:
        user_floor = floor1
        print("You went down the stairs")
      elif user_floor == floor3:
        user_floor = floor2
        print("You went down the stairs")
  elif x == 'grab':
    if user_floor[user_room] == 'sword':
      slots = 0
      var = 0
      while var == 0:
        if inventory[slots] == 'sword' or inventory[slots] == 'magic stone':
          slots += 1
        else:
          inventory[slots] = "sword"
          print("You picked up a sword")
          var = 1
          user_floor[user_room] = "nothing"
    if user_floor[user_room] == 'magic stone':
      slots = 0
      var = 0
      while var == 0:
        if inventory[slots] == 'sword' or inventory[slots] == 'magic stone':
          slots += 1
        else:
          inventory[slots] = "magic stone"
          print("You picked up a magic stone")
          var = 1
          user_floor[user_room] = "nothing"
  elif x == 'fight':
    print(last)
  elif x == 'end':
    print("You killed yourself. How pityful.")
    game_over = 1
  else:
    print("That is not a command.")
  last = x
