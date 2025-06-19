class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")
    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is not an adult.")
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.\n\n\n")

# Create an object
student1 = Student("Tayyab", 17)
student1.introduce()
student1.is_adult()
student1.birthday()


#creating cricket team class

class CrickeTeam:
    def __init__(self, p_name,t_name,wickets,c_wickets):
        self.name = p_name
        self.team = t_name
        self.wickets = wickets 
        self.inn_wickets = c_wickets


    def introduce(self):
        print(f"Player 1 is {self.name} and He's playing from {self.team}")
    def take_wickets(self):
        self.wickets += 1
        print(f"{self.name} took {self.wickets} wicket in last Over")
    def status(self):
        self.inn_wickets += 4
        print(f"{self.name} took total {self.inn_wickets} wickets in innings\n\n\n ")

# creating objects

team_member1 = CrickeTeam("Tayyab", "Al-Ahmad-XIs",0,0)
team_member1.introduce()
team_member1.take_wickets()
team_member1.status()


# inheritance class with cricket team members 

class cricketers:
    def __init__(self,name,team):
        self.name = name
        self.team = team
    def intro (self):
        print(f"I am {self.name} and I paly for {self.team}")    

class Bowler(cricketers):
    def __init__(self, name, team,wickets,economy):
        super().__init__(name, team)
        self.wickets = wickets
        self.economy = economy
    def show_status(self):
        print(f"{self.name} has takes {self.wickets} wickets with the economy of {self.economy}")   

class Batsman(cricketers):
    def __init__(self, name, team,score,strick_rate):
        super().__init__(name, team)
        self.score = score
        self.strick_rate = strick_rate
    def show_status(self):
        print(f"{self.name} has scored {self.score} runs with the strick rate of {self.strick_rate}")



bowler1 = Bowler("Muhammad Tayyab","Al-Ahmad-XIs",4,8.74)
bowler1.intro()
bowler1.show_status()
batsman1 = Batsman("Kaleem Ullah", "Al-Ahmad-XIs",18,71.4)
batsman1.intro()
batsman1.show_status()


print(CrickeTeam.__doc__)
print(CrickeTeam.__dict__)
print(CrickeTeam.__name__)
