import xml.etree.ElementTree as ET
from Constants import *

def parseData(data):
	root = ET.fromstring(data)
	data_dict = {}
	for child in root:
		data_dict[child.tag] = child.text
	return data_dict
	
def formatData(description, player=None, room=None, character=None,
	       weapon=None, choice=None, cardType=None, name=None):
	
	message = ET.Element(MESSAGE_TAG)
	
	if description != None:
		d = ET.SubElement(message, DESCRIPTION_TAG)
		d.text = description
	if player != None:
		p = ET.SubElement(message, PLAYER_TAG)
		p.text = player
	if room != None:
		r = ET.SubElement(message, ROOM_TAG)
		r.text = room
	if character != None:
		c = ET.SubElement(message, CHARACTER_TAG)
		c.text = character
	if weapon != None:
		w = ET.SubElement(message, WEAPON_TAG)
		w.text = weapon
	if choice != None:
		c = ET.SubElement(message, CHOICE_TAG)
		c.text = choice
	if cardType != None:
		ct = ET.SubElement(message, CARDTYPE_TAG)
		ct.text = cardType
	if name != None:
		n = ET.SubElement(message, NAME_TAG)
		n.text = name
	
	return ET.tostring(message)

def main():
        print (formatData("description", "player","room",choice="True"))

if __name__ == "__main__":
        main()
