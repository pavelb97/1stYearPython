##### ////// people.py - First OOP lab \\\\\ #####
"""
First attempt at Object Oriented Programming with python (and in general).
Based on CS1117 - Introduction to programming lab.

Basic OOP principles covered:
    - Defining a class (and constructor)
    - Defining methods and attributes
    - Using private/protected decelerations
    - Getter & setter methods
"""

class Person:
    def __init__(self, fname, lname, phoneNum, email, PPSno, dob):
        self.firstname = fname
        self.lastname = lname
        self.phonenumber = phoneNum
        self.email = email
        self.__PPS = PPSno
        self.__DOB = dob

    def getPPS(self):
        print(self.__PPS)
    def setPPS(self, newPPS):
        self.__PPS = newPPS
    def getDOB(self):
        print(self.__DOB)
    def setDOB(self, newDOB):
        self.__DOB = newDOB

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.phonenumber + " " + self.email

    def formatEmailAddress(self):
        self.emailUsername = self.email.split("@")
        print(self.emailUsername[0])
