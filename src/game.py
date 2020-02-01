import sys
import csv
import json
import cus_exception as ce

genre_list = ["RPG", "ACT", "AVG", "AAVG", "VN",
    "Strategy", "FTG", "STG", "Simulator", "PUZ", "Sport"]


class Game:
    def __init__(self, title, release_date, genres, publishers, developers, nationality, score=0):

        if not title:
            raise ce.InputError("game must have title")
        self.title = title

        release_date_list = release_date.split('-')
        if len(release_date_list) == 1:
            self.month = '-'
            self.date = '-'
            if not release_date_list[0]:
                self.year = '-'
            else:
                self.year = release_date_list[0]
        elif len(release_date_list) == 2:
            self.year = release_date_list[0]
            self.month = release_date_list[1]
            self.date = '-'
        else:
            self.year = release_date_list[0]
            self.month = release_date_list[1]
            self.date = release_date_list[2]
        if self.year != '-':
            year = int(self.year)
            if year < 1900 or year > 2100:
                raise ce.InputError("release year error for game: " + title)
        if self.month != '-':
            month = int(self.month)
            if month < 1 or month > 12:
                raise ce.InputError("release month error for game: " + title)
        if self.date != '-':
            date = int(self.date)
            if date < 1 or date > 31:
                raise ce.InputError("release date error for game: " + title)

        self.genres = genres.split(', ')
        for genre in self.genres:
            if genre not in genre_list:
                raise ce.InputError("genre error for game: " + title)

        self.publishers = publishers.split(', ')

        self.developers = developers.split(', ')

        self.nationality = nationality

        self.score = score



def deserialization_game(line):
    dic = json.loads(line)

    genres = ""
    for genre in dic['genres']:
        genres = genres + genre + ", "
    genres = genres[:-2]

    publishers = ""
    for publisher in dic['publisher']:
        publishers = publishers + publisher + ", "
    publishers = publishers[:-2]

    developers = ""
    for developer in dic['developer']:
        developers = developers + developer + ", "
    developers = developers[:-2]

    release_date = ""
    if dic['year'] == '-':
        release_date = '-'
    elif dic['month'] == '-':
        release_date = dic['year']
    elif dic['date'] == '-':
        release_date = dic['year'] + '-' + dic['month']
    else:
        release_date = dic['year'] + '-' + dic['month'] + '-' + dic['date']

    return Game(dic['title'], release_date, genres, publishers, developers, dic['nationality'], dic['score'])


