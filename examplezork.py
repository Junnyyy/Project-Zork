import random
floor_1=['room_1','room_2','room_3','stairs_up']
floor_2=['room_1','room_2','room_3','stairs_up']
floor_3=['room_1','room_2','Boss_battle','Prize']
items_monster=['Sword','Magic Stone','Monster','NOTHING']
random=random.choice(items_monster)
inventory=['knife','0','0']
user_health=10
user_room=0
user_floor=floor_1
print("Welcome unfortunate victim, this is a test of your skills in combat and how fast you can think on your feet.  Currently you are locked in a warehouse there are 3 normal 'guests' and one very very special 'guest'. Can you defeat the 'guests' and retrieve the key to escape?  Which room on this floor would you like to go to? Or maybe you'd like to go to a different floor?(room_1,room_2,room_3,stairs_up for room commands and floor_1,floor_2, and floor_3 for floor commands.)")
#Unable to code multiple room travel so go to staircase


option=input()
if option=="room_2":
    print("You enter the room and search to find "+random)
if random=='Sword':
    print("You take the sword.")
if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
if random=='Monster':
    print("You fight the monster and kill it.")
if option=="room_3":
  print("You enter the room and search to find "+random)
  if random=='Sword':
    print("You take the sword.")
  if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
  if random=='Monster':
    print("You fight the monster and kill it.")
if option=="stairs_up":
  print("You find the staircase on this floor. You go up.")
  
  print("You begin in the first room, where would you like to go now?")
  option=input()
if option=="room_2":
  print("You enter the room and search to find "+random)
  if random=='Sword':
    print("You take the sword.")
  if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
  if random=='Monster':
    print("You fight the monster and kill it.")
if option=="room_3":
  print("You enter the room and search to find "+random)
  if random=='Sword':
    print("You take the sword.")
  if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
  if random=='Monster':
    print("You fight the monster and kill it.")
if option=="stairs_up":
  print("You find the staircase on this floor. You go up.")
  user_floor=floor_3
  
print("You begin in the first room, where would you like to go no?(There is a Boss_battle room and a prize room)")
option=input()
if option=="room_2":
  print("You enter the room and search to find "+random)
  if random=='Sword':
    print("You take the sword.")
  if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
  if random=='Monster':
    print("You fight the monster and kill it.")
if option=="room_3":
  print("You enter the room and search to find "+random)
  if random=='Sword':
    print("You take the sword.")
  if random=='Magic Stone':
    print("You take the stone, you can feel its power in your pocket.")
  if random=='Monster':
    print("You fight the monster and kill it.")
if option=='Boss_battle':
  print("You fight the boss and move on to the prize room with the key.")
  print("Victory.")
  
