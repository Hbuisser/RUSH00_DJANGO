import requests, json, sys
from django.conf import settings
from django.shortcuts import render
import pickle
import random

class Data():
    def __init__(self, movebals=None, p_names=None, info=None, pos_l=0, pos_c=0, out_of_range=False):
        self.size = [10, 10]
        self.movebals = movebals
        self.pos_l = pos_l
        self.pos_c = pos_c
        self.out_of_range = out_of_range
        self.p_names = p_names
        self.info = info


class Big_one():
    def __init__(self, d=None, my_list=None):
        self.my_list = settings.MOVIE_LIST

    def dump(self):
        f = open("pickle", "rb")
        res = pickle.load(f)
        return res
    
    def get_random_movie(self):
        res = self.dump()
        i = random.randint(0, 9)
        if self.my_list[i] in res.p_names:
            return self.get_random_movie()
        return self.my_list[i]

    def load(self, request):
        col = range(settings.GRID_SIZE[0])
        line = range(settings.GRID_SIZE[1])
        col_file = settings.GRID_SIZE[0]
        line_file = settings.GRID_SIZE[1]
        res = self.dump()
        end = False
        # try:
            
        # except:
        #     print("Wrong file ")
        button = request.GET.get('button', None)
        if button == "right":
            print(res.pos_c)
            print(res.pos_l)
            if (res.pos_c >= 0 and res.pos_c < col_file - 1):
                res.pos_c = res.pos_c + 1
        # else:
        #     res.out_of_range = True
        elif button == "left":
            print(res.pos_c)
            print(res.pos_l)
            if (res.pos_c >= 0 and res.pos_c < col_file - 1):
                res.pos_c = res.pos_c - 1
        elif button == "up":
            if (res.pos_l >= 0 and res.pos_l < line_file - 1):
                res.pos_l = res.pos_l - 1
        elif button == "down":
            if (res.pos_l >= 0 and res.pos_l < line_file - 1):
                res.pos_l = res.pos_l + 1
        #create_file(res.pos_l, res.pos_c, res.out_of_range)
        self.save(res)
        context = {
            'col': col,
            'line': line,
            'pos_l': res.pos_l,
            'pos_c': res.pos_c
        }
        return render(request, 'base.html', context)

    def create_file(self, pos_l, pos_c, out_of_range):
         data = Data(5, ["lol", "kek"], None, pos_l, pos_c, out_of_range)
         fi = open("pickle", "wb")
         pickle.dump(data, fi)

    def save(self, data):
        fi = open("pickle", "wb")
        pickle.dump(data, fi)

    def load_default_settings(self, request):
        col = range(settings.GRID_SIZE[0])
        line = range(settings.GRID_SIZE[1])
        col_file = settings.GRID_SIZE[0]
        line_file = settings.GRID_SIZE[1]

        start = settings.START_POINT
        start_c = start[1]
        start_l = start[0]

        pos_c = start_c
        pos_l = start_l
        context = {
            'col': col,
            'line': line,
            'pos_l': pos_l,
            'pos_c': pos_c
        }
        out_of_range = False
        self.create_file(pos_l, pos_c, out_of_range)
        return render(request, 'base.html', context)

    class Movemone():
        def __init__(self, name=None):
            data = self.get_movie(self.my_list[self.index])
            strength = self.get_movemone_strength()
            print(strength)

    def get_movemone_strength(self, film):
        tmp = self.get_movie(film)["Ratings"]
        print(tmp)
        i = tmp[1]["Value"]
        return i
    
    def get_strength(self, data):
        return len(data.p_names)

    def get_movie(self, arg):
        self.d = dict()
        response = requests.get("http://www.omdbapi.com/?t={}&apikey=23bea02c&type=movie&r=json&".format(arg))
        t = response.json()
        for key in t.items():
            self.d[key[0]] = key[1]
        return self.d
    
    def get_all_moviemons(self):
        all_movies = dict()
        for i in settings.MOVIE_LIST:
            all_movies[i] = self.get_movie(i)
        return all_movies 
    
# def test(arg):
#     a = Big_one()
#     data = Data(0, ["King Kong", "Godzilla", "Alien", "Venom",
#         "The Meg", "Mummy", "Piranha 3dd", "Dracula",
#         "The Invisible Man"], a.get_movie(arg[0]))
#     fi = open("pickle", "wb")
#     pickle.dump(data, fi)
    
#     k = a.get_movie(arg[0])
#     fi.close()
#     new_data = a.dump()
#     print(a.get_random_movie())
    