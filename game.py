

def player_info():
        global player_hp
        global known
        global player_name
        playerH = 15
        player_weapon = "Knife"
        player_armor
        known = False

        print("Your HP: " + str(player_hp) + "\n")
        print("Your Weapon: " + player_weapon + "\n")

        print("Please enter your name: ")
        player_name = input()
        print("\nHello " + player_name + ", let's start your adventure!\n")

def intro_scene():
    print("Welcome to the land of Alduul\n")
    player_info()
    calhollow_town_gate()

def calhollow_town_gate():
    print("\n")
    print("----------------------------------------------------------------------")
    print("")
    print("You are at the gate of the town.")
    print("A guard is standing in front of you.")
    print("What do you want to do?")
    print("")
    print("1: Talk to the guard.")
    print("2: Attack the guard.")
    print("3: Leave.")
    choice = input('Please enter a choice: ')
    if choice == "1":
        if known:
            print(
                    f"Guard: Hello {player_info().playerame}.\n Welcome to calhollow, please enter the gate.")
        else:
            print("Guard: Hello there stranger. \n Sorry but we cannot let a stranger enter our town.")

    elif choice == "2":
        print("Guard: Hey dont't be stupd. \n\nThe guard hit you so hard and you gave up.)")
        

def town_crossroad():            
		print("----------------------------------------------------------------------\n")
		print("You are at a crossroad. If you go south, you will go back to the town.\n\n")
		print("1: Go north")
		print("2: Go east")
		print("3: Go south")
		print("4: Go west")
		print("----------------------------------------------------------------------\n")

def river():
    pass        

def forest():
    pass


intro_scene()