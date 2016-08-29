# FIT1008 Class
# Very Very Useful Python Class Method
class FIT1008:
    def __init__(self):
        pass                            #not recommended by pass, all

    def __repr__(self):
        return "This is FIT1008"        #return basic function call

    def quality(self):
        return "Fun"                    #return quality

    def lecturer(self):
        return "Phil"

    def wordOfDay(self):
        return "hello"

    def checkInt(self,num):
        try:
            int(num)
            return True
        except TypeError:
            return False

    def randomquest(self,num):
        assert FIT1008().checkInt(num), "Invalid Type"
        if num == 1:
            return "Are unicorns real"
        elif num == 2:
            return "Why are we doing this"
        elif num == 3:
            return "How much do you like me"
        elif num == 4:
            return "If you are at a wedding between 4pm and 8pm, how much food would you expect? \nA)nothing \nB)Some \nC)3 course meal \nD)Infinite Buffet"
        elif num == 5:
            return "why are there few students in this lecture"
        elif num == 6:
            return "Should we build a death star"
        elif num == 7:
            return "Sith or Jedi? \nA)Sith \nB)Jedi \nC)Both \nD)I'm dissapointed in myself for not watching Star Wars \n"
        elif num == 8:
            return "Who would you vote for, Donald Trump, Tony Abbott or Adolf Hitler?"
        else:
            return "No Questions today, NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"


from random import randint

num = randint(0,10)
print(FIT1008().quality())
print(FIT1008().randomquest("test"))
print()
print(FIT1008().lecturer())


