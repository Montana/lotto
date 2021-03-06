class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (11, 22, 33, 44, 55, 66)

    def total(self):
        return sum(self.numbers)

# each player has the assigned numbers, to change that just assign new numbers
player_one = LotteryPlayer('Montana')
player_two = LotteryPlayer('Jake')
player_three = LotteryPlayer('Travis')

# this is assuming assigning player_one new numbers. We are deleting the init self tuple and just creating a new one for that instance.
player_one.numbers = (2, 4, 6, 8, 10, 12)

# ---------------------

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls): # you pass in cls, instead of self.
        print('I am going to generic template school.') # ONLY WHEN you declare it a @classmethod can you remove self and pass in cls
        print('I am a {}'.format(cls))

    @staticmethod # gets no 1st argument
    def go_to_eat():
        print('FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD FOOD')


# when this method is called IT ALWAYS passes self in automatically, as an argument. So you have to declare it a classmethod(cls)
wolfe = Student('Montana', 'USL')
wolfe.go_to_school()
wolfe.go_to_eat()


# Montana = ('Montana', Engineer')
# montana.marks.append(88)
# montana.marks.append(44)
# montana.marks.append(99)
# montana.marks.append(66)
# montana.marks.append(77)
# montana.marks.append(60)
# print(montana.marks)
# print (montana.average())
