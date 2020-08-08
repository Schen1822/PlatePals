class PreferenceList:

    def __init__(self):
        self.people = []

    def getPerson(self, name):
        for person in self.people:
            if person.name == name:
                return person
        return None

    def getPeople(self):
        return self.getDict().keys()

    def addPerson(self, person):
        self.people.append(person)

    def getDict(self):
        dict = {}
        for person in self.people:
            dict[person.name] = person.getPreferences()
        return dict
