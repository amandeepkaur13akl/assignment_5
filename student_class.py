class Student:

    def getName(self):
        return self.name
        
    def setName(self,name):
        self.name = name
        
    def getRollNumber(self):
        return self.rollno
        
    def setRollNumber(self,rollno):
        self.rollno = rollno
student = Student()
name=input('Enter the name of student: ')
rollno=input('Enter the roll no of student: ')
student.setName(name)
student.setRollNumber(rollno)

print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())
        