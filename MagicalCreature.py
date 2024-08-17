from MagicalContact import MagicalContact

class MagicalCreature (MagicalContact):
    def __init__(self,name,email,phone_number,species ,is_tame ):
        super().__init__(name,email,phone_number)
        self.__species=species
        self.__is_tame=is_tame
    def get_species(self):
        print(self.__species)
    def get_is_tame(self):
        print(self.__is_tame)
    def describe(self):
        return super().describe(), print(f'species = {self.__species}, is tame? {self.__is_tame}')


# contact1 = MagicalCreature('Hedwig', 'owl@example.com', '0987654321', 'Owl', True)
# contact1.get_species()
# contact1.get_is_tame()
# contact1.describe()