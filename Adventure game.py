#intro to adventure game
print("you wake up in an airport")
print("there is no one around")

print("you reach for your backpack but it's completely empty, you walk around and you catch a glimpse of the what you assume to be the last airplane leaving.")

print("you walk over to an empty restuarant and notice there is food still there and you are starving")

#decision
print("[1] Take as much food as you can")
print("[2] Don't take anything and walk away")

choice = input("Enter a choice: ")

if choice == "1":
  print("you hear someone walking in the airport")
elif choice == "2":
  print("you leave the restuarant in hopes of finding out where you are and how you got here")

#what happens after decision 1
print()
print("You start getting a move on and once you reach the main terminal, you find someone and he asks you what your profession is.")

#Decision 2
print("[1] A doctor")
print("[2] A bodybuilder")
print("[3] An aircraft mechanic")

choice = input("Enter a choice: ")

if choice == "1":
  print("You tell him that you are a doctor")
  intellect = 99
  strength = 20
  dexterity = 50
if choice == "2":
  print("You tell him that your are a bodybuilder")
  intellect = 55
  strength = 100
  dexterity = 15
if choice == "3":
  print("you tell him you are an aircraft mechanic")
  intellect = 25
  strength = 45
  dexterity = 95
#Display stats to user
print()
print("Your stats: ")
print(f"Intellect: {intellect}")
print(f"Strength: {strength}")
print(f"Dexterity: {dexterity}")

#Encounter with first human
print()
print("The man explains to you how everyone had to evacuate the country due to an apocalypse.")
print("[1] How did I get here? ")
print("[2] How did this happen? ")

choice = input("How do you respond? ")

if choice == "1":
  print("You were rushed to this airport when the apocalypse broke out but you passed out and they couldn't board you on the plane.")
if choice == "2":
  print("No one knows, it all happened so quickly and the entire globe is under complete lockdown.")
print("The man leaves and you are left completely alone.")
print()
print("[1] Yes")
print("[2] No")
object_to_pick_up = input("You notice a sword on the ground, do you wish to pick it up? ")

print()
print("You become extremely bored while being alone in the airport.")
print("[1] Read a book about how to survive a zombie apocalypse")
print("[2] Do some pushups")
print("[3] Start doing a rubix cube")
choice = input("What do you choose to do during your downtime? ")

if choice == "1":
  intellect = intellect + 20
if choice == "2":
  strength = strength + 20
if choice == "3":
  dexterity = dexterity + 20

#Display stats to user 
print()
print("Your stats: ")
print(f"Intellect: {intellect}")
print(f"Strength: {strength}")
print(f"Dexterity: {dexterity}")

print()
print("After spending an entire day alone in this empty airport you decide to finally go to sleep, but as you are falling asleep you hear something behind the window at the bench you are sitting on.")
print("You realise the zombies from the apocalypse that the guy was talking about are right outside the airport")
if intellect > 90:
  print("You decide to use your intelligence to your advantage so you set up traps at the entrances of the building, which buys you time to escape the airport.")
if strength > 90:
  if object_to_pick_up == "2":
    print("You try to take on the zombies but without a weapon they overwhelm you and you go down in the horde. ")
  if object_to_pick_up == "1":
    print("you grab the sword that you took from earlier and kill the zombies 1 by one until they are all dead, which allows you to escape the airport.")
if dexterity > 90:
  print("since you are an aircraft mechanic, you quickly rush to the runway where you find an airplane, the control panel seems to be damaged but you work around it and quickly fix it. The airplane slowly starts up and the zombies are right outside the plane but you initiate take off and get away safely. ")
