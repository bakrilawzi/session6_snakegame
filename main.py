class Student:
    def __init__(self,scorephy,scoremath,scorePython):
        self.scorePython = scorePython
        self.scorephy = scorephy
        self.scoremath = scoremath
    def calculategpa(self):
        gpa = 5*self.scorephy+5*self.scoremath+10*self.scorePython
        return gpa
    def passed(self):
        if self.calculategpa()>50:
            return "Passed"
        else:
            return "not Passed"
