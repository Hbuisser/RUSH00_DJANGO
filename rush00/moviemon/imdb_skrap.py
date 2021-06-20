import requests, json, sys
from django.conf import settings
from django.shortcuts import render
import pickle
import random

class Data():
    def __init__(self, bals_nbr=0, p_names=None, info=None, pos_l=0, pos_c=0, out_right=False, out_left=False, out_up=False, out_down=False, bals_pos=None, movie_pos=None):
        self.size = [10, 10]
        self.bals_nbr = bals_nbr
        self.pos_l = pos_l
        self.pos_c = pos_c
        self.out_right = out_right
        self.out_left = out_left
        self.out_up = out_up
        self.out_down = out_down
        self.p_names = p_names
        self.info = info
        self.bals_pos = bals_pos
        self.movie_pos = movie_pos

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

        button = request.GET.get('button', None)
        if button == "right":
            if res.out_right == False:
                res.pos_c = res.pos_c + 1
                res.out_left = False
            if res.pos_c == col_file - 1:
                res.out_right = True
        elif button == "left":
            if res.out_left == False:
                res.pos_c = res.pos_c - 1
                res.out_right = False
            if res.pos_c == 0:
                res.out_left = True
        elif button == "up":
            if res.out_up == False:
                res.pos_l = res.pos_l - 1
                res.out_down = False
            if res.pos_l == 0:
                res.out_up = True
        elif button == "down":
            if res.out_down == False:
                res.pos_l = res.pos_l + 1
                res.out_up = False
            if res.pos_l == line_file - 1:
                res.out_down = True
        for i in res.bals_pos:
            if i[0] == res.pos_c and i[1] == res.pos_l:
                res.bals_nbr = res.bals_nbr + 1
                print(res.bals_nbr)
        for j in res.movie_pos:
            if j[0] == res.pos_c and j[1] == res.pos_l:
                print(self.get_random_movie())

        self.save(res)
        context = {
            'col': col,
            'line': line,
            'pos_l': res.pos_l,
            'pos_c': res.pos_c
        }
        return render(request, 'moviemon/base.html', context)

    def create_file(self, bals_nbr, pos_l, pos_c, out_right, out_left, out_up, out_down, bals_pos, movie_pos):
        data = Data(bals_nbr, ["lol", "kek"], None, pos_l, pos_c, out_right, out_left, out_up, out_down, bals_pos, movie_pos)
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
        out_right = False
        out_left = False
        out_up = False
        out_down = False
        bals_pos = self.create_moviebals_pos()
        bals_nbr = 0
        movie_pos = self.create_movie_pos(bals_pos)
        context = {
            'col': col,
            'line': line,
            'pos_l': pos_l,
            'pos_c': pos_c
        }
        self.create_file(bals_nbr, pos_l, pos_c, out_right, out_left, out_up, out_down, bals_pos, movie_pos)
        return render(request, 'moviemon/base.html', context)

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
    
    def create_moviebals_pos(self):
        tab = []
        col_nbr = settings.GRID_SIZE[0]
        line_nbr = settings.GRID_SIZE[1]
        nbr = (col_nbr * line_nbr) / 3
        while (len(tab) != nbr):
            i = [random.randint(0, col_nbr), random.randint(0, line_nbr)]
            if i not in tab:
                tab.append(i)
        tab.sort()
        return (tab)

    def create_movie_pos(self, bals_pos):
        movies = settings.MOVIE_LIST
        pos = []
        col_nbr = settings.GRID_SIZE[0]
        line_nbr = settings.GRID_SIZE[1]
        nbr = (col_nbr * line_nbr) / 3
        while (len(pos) != nbr):
            j = [random.randint(0, col_nbr), random.randint(0, line_nbr)]
            if j not in pos and j not in bals_pos:
                pos.append(j)
        pos.sort()
        return pos

    
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
    