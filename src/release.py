import sys
import csv
import json
import cus_exception as ce

platform_list = ['PC Engine', 'DOS', 'PC', 'FC', 'MD', 'GB', 
'SFC', 'PS', 'Saturn', 'N64', 'GBC', 'DC', 'PS2', 'GBA', 'GC',
'Xbox', 'DS', 'PSP', 'Xbox 360', 'Wii', 'PS3', 'IOS', '3DS', 
'PSV','WiiU', 'PS4', 'Xbox One', 'Switch', 'Android']

class Release:
    def __init__(self, title, release_title, platform, release_date, text, publisher, developer, score, complete_date="", audio="", translator="", playtime="", note="", platform_note=""):

        if not title:
            raise ce.InputError("release must have title")
        self.title = title

        if not release_title:
            raise ce.InputError("release must have release title")
        self.release_title = release_title

        if not platform:
            raise ce.InputError("release must have platform")
        self.platform = platform

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
                raise ce.InputError("release year error for release: " + release_title)
        if self.month != '-':
            month = int(self.month)
            if month < 1 or month > 12:
                raise ce.InputError("release month error for release: " + release_title)
        if self.date != '-':
            date = int(self.date)
            if date < 1 or date > 31:
                raise ce.InputError("release date error for release: " + release_title)

        self.text = text

        self.publisher = publisher.split(', ')

        self.developer = developer.split(', ')

        self.platform = platform
        if platform not in platform_list:
            raise ce.InputError("release date error for release: " + release_title)

        try:
            self.score = int(score)
        except:
            raise ce.InputError("score error for release: " + release_title)
        if self.score < 1 or self.score > 4:
            raise ce.InputError("score error for release: " + release_title)
        

        if complete_date:
            complete_date_list = complete_date.split('-')
            self.complete_year = complete_date_list[0]
            self.complete_month = complete_date_list[1]
            self.complete_date = complete_date_list[2]
        else:
            self.complete_year = '-'
            self.complete_month = '-'
            self.complete_date = '-'
        
        self.audio = audio

        self.translator = translator

        self.note = note

        self.platform_note = platform_note

        self.playtime = playtime



def deserialization_release(line):

    dic = json.loads(line)

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
    
    complete_date = ""
    if dic['complete_year'] != '-':
        complete_date = dic['complete_year'] + '-' + dic['complete_month'] + '-' + dic['complete_date']

    return Release(dic['title'], dic['release_title'], dic['platform'], release_date, dic['text'], publishers, developers, str(dic['score']), complete_date, dic['audio'], dic['translator'], dic['playtime'], dic['note'], dic['platform_note'])

