import sys
import csv
import json
import release as re
import game as ga
import cus_exception as ce

class Gamelist:
    def __init__(self, filename):
        
        self.modified = False
        self.game_dict = {}
        self.game_title_set = set()
        self.developer_dict = {}
        self.publisher_dict = {}
        self.nationality_dict = {}

        with open(filename, 'r') as f:
            games = f.readlines()

        for line in games:
            game = ga.deserialization_game(line)
            self.add_game_record(game)
    


    def add_game_record(self, game):

        self.game_dict[game.title] = game

        self.game_title_set.add(game.title)
        
        self.add_publisher(game.publishers, game.title)

        self.add_developer(game.developers, game.title)

        self.add_notionality(game.nationality, game.title)

    def add_publisher(self, publishers, title):

        for publisher in publishers:
            if publisher not in self.developer_dict:
                self.publisher_dict[publisher] = set(title)
            else:
                self.publisher_dict[publisher].add(title)
    
    def add_developer(self, developers, title):
        for developer in developers:
            if developer not in self.developer_dict:
                self.developer_dict[developer] = set(title)
            else:
                self.developer_dict[developer].add(title)

    def add_notionality(self, nationality, title):
        if nationality not in self.nationality_dict:
            self.nationality_dict[nationality] = set(title)
        else:
            self.nationality_dict[nationality].add(title)

    def reorder(self, compare):
        return sorted(self.game_dict.items(), key=compare)
    
    def genre_collection(self, genres):
        game_genre = set()
        for key, game in self.game_dict.items():
            for genre in game.genres:
                if genre in genres:
                    game_genre.add(game)
        return game_genre

    def work_by_publishers(self, publishers):
        works = set()
        for publisher in publishers:
            works = works.union(self.publisher_dict[publisher])
        return works
    
    def work_by_developers(self, developers):
        works = set()
        for developer in developers:
            works = works.union(self.developer_dict[developer])
        return works
    
    def update_database(self, filename):
        s = ""
        if self.modified:
            for key, game in self.game_dict.items():
                s = s + serialization(game) + "\n"
            with open(filename, 'w') as f:
                f.write(s)
            
    def add_game(self, title, release_date, genres, publishers, developers, nationality, score=0):
        
        if title in self.game_title_set:
            raise ce.InputError(title + " already exists in database")
        
        self.add_game_record(ga.Game(title, release_date, genres, publishers, developers, nationality, score))
        self.modified = True

    def remove_game(self, title):
        try:
            self.game_title_set.remove(title)
        except KeyError:
            raise ce.InputError(title + " does not exist")


def game_release_date_compare(game1, game2):
    if game1.year < game2.year:
        return -1
    elif game1.year > game2.year:
        return 1
    else:
        if game1.month < game2.month:
            return -1
        elif game1.month > game2.month:
            return 1
        else:
            if game1.date < game2.date:
                return -1
            else:
                return 1

def game_score_compare(game1, game2):
    if game1.score < game2.score:
        return -1
    else:
        return 1

def serialization(obj):
    return json.dumps(obj.__dict__)


    

if __name__ == "__main__":
    """
    three_houses = ga.Game("three houses", "2019-07-26", "RPG, Strategy", "Nintendo", "Intelligent Systems, Koei Tecmo", "Japan", 2)
    three_houses_release = re.Release("three houses", "three houses", "Switch", "2019-07-26", "Chinese", "Nintendo", "Intelligent Systems, Koei Tecmo", "2", complete_date = "2019-08-04", audio="Japanese")
    with open("a.json", "w") as f:
        f.write(serialization(three_houses))

    with open('a.json', 'r') as f:
        distros_dict = f.readlines()

    games = []
    for distro in distros_dict:
        games.append(ga.deserialization_game(distro))
    
    for game in games:
        print(game.title)
    """

    gamelist = Gamelist("data\data.txt")
    gamelist.add_game("missed messages", "2019-05-20", "AVG", "Angela He", "Angela He", "the U.S.", 2)
    gamelist.update_database("data\data.txt")

