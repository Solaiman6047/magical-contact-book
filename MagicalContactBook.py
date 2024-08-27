from MagicalContact import MagicalContact
from MagicalCreature import MagicalCreature
from WitchAndWizard import WizardOrWitch
class MagicalContactBook:
    _contacts = []  

    @classmethod
    def add_contact(cls, contact):
        cls._contacts.append(contact)

    @classmethod
    def list_contacts(cls):
        for contact in cls._contacts:
            print(f'[{contact}: {contact.describe()}]')

    @classmethod
    def find_contact(cls, contact):
        if contact in cls._contacts:
            print(contact.describe())
        else:
            print('Contact not found')
