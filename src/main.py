import sys
import csv
import json
import release as re
import game as ga

class Gamelist:
    def __init__(self, filename):
        
        self.game_list = []
        self.game_title_set = {}
        self.developer_dict = {}
        self.publisher_dict = {}
        self.nationality_dict = {}

        with open(filename, 'r') as f:
            games = f.readlines()

        for i in games:
            game = ga.deserialization_game(i)

            game_list.append(game)

            game_title_set.add(game.title)

            for developer in game.developers:
                if developer not in developer_sict:
                    developer_list[developer] = set(game.title)
                else:
                    developer_list[developer].add(game.title)

            for publisher in game.publishers:
                if publisher not in publisher_dict:
                    publisher_list[publisher] = set(game.title)
                else:
                    publisher_list[publisher].add(game.title)

            if game.nationality not in nationality_dict:
                nationality_list[nationality] = set(game.title)
            else:
                nationality_list[nationality].add(game.title)

    def release_date_order(self):
        self.game_list.sort(key=game_release_date_compare)
    
    def genre_collection(self, genres):
        game_genre = {}
        for game in self.game_list:
            for genre in game.genres:
                if genre in genres:
                    game_genre.add(game)
        return game_genre

    def work_by_publishers(self, publishers):
        works = {}
        for publisher in publishers:
            works = works.union(self.publisher_dict[publisher])
        return works
    
    def work_by_developers(self, developers):
        works = {}
        for developer in developers:
            works = works.union(self.developer_dict[developer])
        return works


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

        

def serialization(obj):
    return json.dumps(obj.__dict__)


def insert_release(release, release_list, game_list):
    

if __name__ == "__main__":
    three_houses = ga.Game("three houses", "2019-07-26", "RPG, Strategy", "Nintendo", "Intelligent Systems, Koei Tecmo", "Japan")
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