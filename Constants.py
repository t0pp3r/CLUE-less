# Colors
YELLOW = "Yellow"
RED = "Red"
PURPLE = "Purple"
GREEN = "Green"
WHITE = "White"
BLUE = "Blue"

# Character names
COLONEL_MUSTARD = "Colonel Mustard"
MISS_SCARLET = "Miss Scarlet"
PROFESSOR_PLUM = "Professor Plum"
MR_GREEN = "Mr. Green"
MRS_WHITE = "Mrs. White"
MRS_PEACOCK = "Mrs. Peacock"

# Weapons
CANDLESTICK = "Candlestick"
KNIFE = "Knife"
LEAD_PIPE = "Lead Pipe"
REVOLVER = "Revolver"
ROPE = "Rope"
WRENCH = "Wrench"

# Rooms
STUDY = "Study"
HALL = "Hall"
LOUNGE = "Lounge"
LIBRARY = "Library"
BILLIARD_ROOM = "Billiard Room"
DINING_ROOM = "Dining Room"
CONSERVATORY = "Conservatory"
BALLROOM = "Ballroom"
KITCHEN = "Kitchen"

#Hallways
H1 = "Hallway 1"
H2 = "Hallway 2"
H3 = "Hallway 3"
H4 = "Hallway 4"
H5 = "Hallway 5"
H6 = "Hallway 6"
H7 = "Hallway 7"
H8 = "Hallway 8"
H9 = "Hallway 9"
H10 = "Hallway 10"
H11 = "Hallway 11"
H12 = "Hallway 12"

# Card/Location types
WEAPON = "Weapon"
PERSON = "Person"
ROOM = "Room"
START = "Start"
HALLWAY = "Hallway"

# Names in order of play
NAMES = { COLONEL_MUSTARD : YELLOW, 
		  MISS_SCARLET : RED, 
		  PROFESSOR_PLUM : PURPLE, 
		  MR_GREEN : GREEN, 
		  MRS_WHITE : WHITE, 
		  MRS_PEACOCK : BLUE }
		  
# Card mappings
CARDS = { WEAPON : [CANDLESTICK, KNIFE, LEAD_PIPE, REVOLVER, ROPE, WRENCH],
		  PERSON : [COLONEL_MUSTARD, MISS_SCARLET, PROFESSOR_PLUM, MR_GREEN, MRS_WHITE, MRS_PEACOCK],
		  ROOM : [STUDY, HALL, LOUNGE, LIBRARY, BILLIARD_ROOM, DINING_ROOM, CONSERVATORY, BALLROOM, KITCHEN] }

# Port numbers for server and listener
PORT_SERVER = 8123
PORT_LISTENER = 8124

# Games States
CONNECTION_STATE = "Connection State"

# Message Descriptions
MAKE_SUGGESTION = "Make suggestion"
MOVE_PLAYER = "Move player"
MAKE_CORRECT_ACCUSATION = "Make correct accusation"
MAKE_WRONG_ACCUSATION = "Make wrong accusation"
SUGGESTION_DISPROVED = "Suggestion disproved"
SUGGESTION_NOT_DISPROVED = "Suggestion not disproved"
END_TURN = "End turn"
SEND_PLAYER_ORDER = "Send player order"
SEND_PLAYER_CARDS = "Send player cards"
SEND_MURDER_CARDS = "Send murder cards"
START_GAME = "Start game"
JOIN_GAME = "Join game"

# XML Tags
DESCRIPTION_TAG = 'description'
MESSAGE_TAG = 'message'
ROOM_TAG = 'room'
PLAYER_TAG = 'player'
CHARACTER_TAG = 'character'
WEAPON_TAG = 'weapon'
CHOICE_TAG = 'choice'
CARDTYPE_TAG = 'type'
NAME_TAG = 'name'


