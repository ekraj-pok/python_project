import pygame
import time
pygame.init()
#### Item definition and variable creation in Prison Cell

prison_cell = {
    "name": "prison cell",
    "type": "room",
}

cell_bed = {
    "name": "cell bed",
    "type": "furniture",
}

cell_door = {
    "name": "cell door",
    "type": "door",
}

toilet = {
    "name": "toilet",
    "type": "furniture",
}

old_calendar = {
    "name": "old calendar",
    "type": "furniture",
}

lockpick = {
    "name": "lockpick for cell door",
    "type": "key",
    "target": cell_door,
}


#### Item definition and variable creation in Dinning Hall

dinning_hall = {
    "name": "dinning hall",
    "type" : "room",
}

dinning_table = {
    "name" : "dinning table",
    "type" : "furniture",
}

laundry_window = {
    "name" : "window",
    "type" : "door",
}
security_door = {
    "name" : "door to security",
    "type" : "door", 
}

prison_guard = {
    "name": "prison guard",
    "type": "door",
}


table_leg = {
    "name" : "table leg",
    "type" : "key",
    "target" : laundry_window,
}

laundry_room = {
    "name" : "laundry room",
}

security_room = {
    "name" : "security room",
}

#### Item definition and variable creation in Laundry Room

laundry_room = {
    "name" : "laundry room",
    "type" : "room",
}

washing_machine = {
    "name" : "washing machine", 
    "type" : "furniture",
}
laundry_basket = {

    "name" : "laundry basket",
    "type" : "furniture",
}
steel_door = {
    "name" : "reinforced steel door",
    "type" : "furniture",
}
key_to_security = {
    "name" : "key to security room",
    "type" : "key", 
    "target" : security_door,
}

security_room = {
    "name" : "security room",
    "type" : "room"
}

#### Item definition and variable creation in Security Room

door_of_freedom = {
    "name": "door of freedom",
    "type": "door",
}

prison_keys_locker = {
    "name": "prison keys locker",
    "type": "furniture",
}

prison_keys = {
    "name": "prison keys",
    "type": "key",
    "target": door_of_freedom,
}

outside_world = {
    "name" : "outside world",
}


all_rooms = [prison_cell, dinning_hall, laundry_room, security_room, outside_world]

all_doors = [cell_door, laundry_window, security_door, prison_guard, door_of_freedom]


# define which items/rooms are related

object_relations = {
    "prison cell": [old_calendar, toilet, cell_bed, cell_door],
    "old calendar": [lockpick],
    "cell door": [prison_cell, dinning_hall],
    "dinning hall" : [cell_door, dinning_table, laundry_window, security_door],
    "dinning table" : [table_leg],
    "window" : [dinning_hall, laundry_room],
    "door to security" : [dinning_hall, security_room],
    "laundry room" : [washing_machine, laundry_basket, steel_door, laundry_window],
    "washing machine" : [key_to_security],
    "security room" : [prison_keys_locker, door_of_freedom],
    "prison keys locker": [prison_keys],
    "door of freedom" : [security_room, outside_world],
    "outside world" : [door_of_freedom]
}


#filepath = "C:/Users/udaya/Desktop/Bootcamp/Project/python-project/"
door_sound = pygame.mixer.Sound("door_sound.mp3")
outside_door_sound = pygame.mixer.Sound("door_to_freedom.mp3")
window_sound = pygame.mixer.Sound("window_sound.mp3")
volume_door = door_sound.get_volume()
door_sound.set_volume(volume_door * 1)
volume_window = window_sound.get_volume()
door_sound.set_volume(volume_window * 1)
"""table_sound = pygame.mixer.Sound("table_break.mp3")
volume_table = table_sound.get_volume()
table_sound.set_volume(volume_table * 1)"""
game_music = pygame.mixer.Sound("game_music.mp3")

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": prison_cell,
    "keys_collected": [],
    "target_room": outside_world,
}



def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    game_music.play()    
    print("The morning alarm rings in your ears.")
    time.sleep(1)
    print("Once again you open your eyes in your cold, damp and grey cell.")
    time.sleep(1)
    print("The only sign that there's a world outside those four walls is your cell door.")
    time.sleep(1)
    print("All of the sudden, you really miss your dog. A grey pitbull called Butcher.")
    time.sleep(1)
    print("Your desire to be reunited with your four-legged best friend is now too great to fathom.")
    time.sleep(1)
    print("You make the ultimate decision.")
    time.sleep(1)
    print("To escape from this damn prison.")
    time.sleep(1)
    play_room(game_state["current_room"])


def display_image(image_path):
    
    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    pygame.display.flip()   



def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped prison and can now be forever ever happily with your dog Butcher!\nWho you found out died 2 weeks after you got arrested.\nGAME OVER")
        display_image("game_over.jpg")
        outside_door_sound.play()
        time.sleep(4)
        pygame.quit()
    
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'look around' or 'examine'?").strip()
        if intended_action == "look around":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'look around' or 'examine'.")
            play_room(room)
        linebreak()


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You take a look around the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room
        


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You get through it with your pure genius, some brute strength and pure luck. Nice work."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "You need something to help you get through this."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    if item_found != table_leg:
                        # table_sound.play()
                        output += "You find " + item_found["name"] + "."
                    else:
                        output += "You broke the " + item_found["name"] + "." 
                else:
                    output += "This won't help you reunite with your beloved dog, Butcher."
            print(output)
            break

    if(output is None):
        print("You don't think this will help you right now.")
    
    if(next_room and input("Let's get out of this hell hole? Enter 'yes' or 'no'").strip() == 'yes'):
        if next_room == game_state["target_room"]:
            pass  
        elif next_room ==  laundry_room:
            window_sound.play()    
        elif next_room == dinning_hall and current_room == laundry_room:
            pass 
        else:
            door_sound.play()
        play_room(next_room)
    else:
        play_room(current_room)


game_state = INIT_GAME_STATE.copy()

start_game()