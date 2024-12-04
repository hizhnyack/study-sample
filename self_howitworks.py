from symbol import star_expr


class human():
    def __init__(self,age=0,gender='?'):
        self.age = age
        self.gender = gender
    def speak(self):
        print('I am a', self.gender, 'and I', self.age,'years old')


Jane = human(24, 'woman')
John = human(22, 'man')

Jane.speak()
John.speak()
# print(speak(Jane), 'and', speak(John))
