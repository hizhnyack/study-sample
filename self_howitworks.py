from symbol import star_expr



class human():

    def __init__(self,name = '', age=0,gender='?'):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print('I am a', self.name,',',self.__class__.__name__, self.gender, 'and I', self.age,'years old')

    def chage(self,person):
        temp = human('',0,'')
        temp.age = self.age
        self.age = person.age
        person.age = temp.age
        return self, person


jane = human('Jane',24, 'female')
john = human('Jane',22, 'male')

# Jane.speak()
# John.speak()
# print(speak(Jane), 'and', speak(John))
