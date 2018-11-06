import random

# Floor 1-3
floor3 = ['sword', 'stairs down', 'nothing', 'boss monster', 'prize']
floor2 = ['magic stones', 'stairs up', 'monster', 'stairs down', 'nothing']
floor1 = ['nothing', 'sword', 'monster', 'stairs up', 'sword']
# inventory, user room, and user floor variables 
inventory = [0,0,0]
user_room = 0
user_floor = floor1
game_over = true
print("Welcome unfortunate victim, this is a test of your skills in combat and how fast you can think on your feet.  Currently you are locked in a warehouse there are 3 normal 'guests' and one very very special 'guest'. Can you defeat the 'guests' and retrieve the key to escape?  Which room on this floor would you like to go to? Or maybe you'd like to go to a different floor? Type 'help' for the commands.\n")
# if statements for game function
while not game_over:
  x = input("What do you do?")
  if x == 'help':
    print("left, right, up, down, grab, fight, help, end")
  elif x == 'left':
    print()
  elif x == 'right':
    if x < 5:
      user_room += 1
  elif x == 'up':
    print()
  elif x == 'down':
    print()
  elif x == 'grab':
    print()
  elif x == 'fight':
    print()
  elif x == 'end':
    print("You killed yourself. How pityful.")
    game_over = 1
  else:
    print("That is not a command.")
