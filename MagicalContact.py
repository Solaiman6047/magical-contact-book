class MagicalContact:
    def __init__(self,name,email,phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
    def get_name(self):
        print(self.name)
    def get_email(self):
        print(self.email)
    def get_phone_number(self):
        print(self.phone_number)
    def set_email(self,new_email):
        self.email=new_email
    def set_phone_number(self,new_phone_number):
        self.phone_number = new_phone_number
    def describe(self):
        print(f'name = {self.name}, email = {self.email}, phone number = {self.phone_number}')

# contact1=MagicalContact('Harry','harry@gmail.com','0122345')
# contact1.get_name()
# contact1.get_email()
# contact1.get_phone_number()
# contact1.describe()
# contact1.set_email('HARRY@gmail.com')
# contact1.set_phone_number('012287878')
# contact1.get_email()
# contact1.get_phone_number()
# contact1.describe()