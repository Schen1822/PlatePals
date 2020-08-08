from CSVWriter import getKeys

class Person:

    def __init__(self, name):
        self.name = name
        self.preferences = {}

    def addPreference(self, name, score):
        self.preferences[name] = score

    def getPreferences(self):
        list = sorted(self.preferences, key=lambda z: self.preferences[z], reverse = True)
        return list