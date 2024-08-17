from MagicalContact import MagicalContact

class WizardOrWitch (MagicalContact):
    def __init__(self,name,email,phone_number,core,wood,length,house):
        super().__init__(name,email,phone_number)
        self.core : core
        self.wood : wood
        self.length : length
        self.__wand ={
            'core': core,
            'wood':wood,
            'length':length
        }
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house in valid_houses:
            self.house = house
        else:
            print('Invalid house, please enter a valid house.')
            self.house = None   
    def get_wand(self):
        print(self.__wand)
    def get_house(self):
        print(self.house)
    def describe(self):
        return super().describe(), print(f'__wand = {self.__wand}, house = {self.house}')

# contact1 = WizardOrWitch('Harry', 'email@example.com', '1234567890', 'Phoenix Feather', 'Elder', 11, 'Ravenclaw')
# contact1.get___wand()
# contact1.get_house()
# contact1.describe()
# contact1 = WizardOrWitch('Harry', 'email@example.com', '1234567890', 'Phoenix Feather', 'Elder', 11, 'house')
# contact1.get_house()
# contact1.describe()