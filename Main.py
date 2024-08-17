def new_wizard():
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone number: ")
    core = input("Wand's core: ")
    wood = input("Wand's wood: ")
    length = input("Wand's length: ")
    house = input("House: ")
    wizard=WizardOrWitch(name,email,phone_number,core,wood,length,house)
    MagicalContactBook.add_contact(wizard) 
def new_creature():
    name = input("Name: ")
    email = input("Email: ")
    phone_number = input("Phone number: ")
    species=input('Specie: ')
    is_tame=input('Is it tamed?(Yes/no): ')
    creature=MagicalCreature(name,email,phone_number,species,is_tame)
    MagicalContactBook.add_contact(creature) 
    
from MagicalCreature import MagicalCreature
from WitchAndWizard import WizardOrWitch
from MagicalContactBook import MagicalContactBook

while True:
    print('Enter action(new wizard or witch/new creature/show the Magical Contact Book/search for a contact/exit )')
    action=input()
    if action == "new wizard or witch":
        new_wizard()
    elif action == "new creature":
        new_creature()
    elif action == "show the Magical Contact Book":
        MagicalContactBook.list_contacts()
    elif action == 'search for a contact':
        contact = input('Enter contact name: ')
        MagicalContactBook.find_contact(contact)
    elif action == 'exit':
        print('Exiting....')
        break
    else:
        print('Invalid input. Try again')