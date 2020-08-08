from matching.games import StableRoommates
from person import Person
from preferencelist import PreferenceList
from utils import getKeys
import csv


class PlatePals:

    def __init__(self, data):
        self.data = data
        self.preferences = self.__create_preference_list(self.data)
        self.pals = self.__assign()

    def __create_preference_list(self, df):
        preferences = PreferenceList()
        for i in range(df.shape[0]):
            people = preferences.getPeople()
            name = df.loc[i][0]
            if people and name in people:
                person = preferences.getPerson(name)
            else:
                person = Person(name)
                preferences.addPerson(person)
            for j in range(i + 1, df.shape[0]):
                nextName = df.loc[j][0]
                if people and nextName in people:
                    nextPerson = preferences.getPerson(nextName)
                else:
                    nextPerson = Person(nextName)
                    preferences.addPerson(nextPerson)
                score = self.__calculate_score(i, j, df)
                person.addPreference(nextPerson.name, score)
                nextPerson.addPreference(person.name, score)
        return preferences

    def __calculate_score(self, i, j, df):
        score = 0
        without_personality = df.drop(['name', 'personality'], axis=1)
        score += sum(without_personality.loc[i] == without_personality.loc[j])
        score += self.__personality_score(i, j, df)
        return score

    def __personality_score(self, i, j, df):
        count = 0
        first = df['personality'].loc[i]
        second = df['personality'].loc[j]
        for k in range(len(first)):
            if first[k] == second[k]:
                count += 1
        return count

    def __stable_roommate(self, d):
        game = StableRoommates.create_from_dictionary(d)
        return game.solve()

    def __assign(self):
        preferences = self.preferences.getDict()
        return self.__stable_roommate(preferences)

    def matches(self):
        return self.pals

    def write_to_csv(self, file_name):
        file_name = file_name + '.csv'
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for key, value in self.pals.items():
                writer.writerow([key, value])



