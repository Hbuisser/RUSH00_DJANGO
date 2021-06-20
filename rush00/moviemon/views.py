from django.shortcuts import render
from django.conf import settings
import pickle
from . import imdb_skrap

def create_file(self, bals_nbr, pos_l, pos_c, out_right, out_left, out_up, out_down, bals_pos, movie_pos):
        data = Data(bals_nbr, ["lol", "kek"], None, pos_l, pos_c, out_right, out_left, out_up, out_down, bals_pos, movie_pos)
        fi = open("pickle", "wb")
        pickle.dump(data, fi)

def begin(request):
    main = imdb_skrap.Big_one()
    button = request.GET.get('button', None)
    if button == None:
        return main.load_default_settings(request)
    else:
        return main.load(request)

def title_page(request):
    return render(request, 'title.html')

def battle(request, id, name):
    a = imdb_skrap.Big_one()
    # tmp = a.get_random_movie()
    # id = res.all_movies[tmp]["imdbID"]
    if id == None:
        a.load()
    dic = a.dump()
    full = dic.all_movies
    print(full[name]["Poster"])
    id = full[name]["imdbID"]
    l = a.get_movemone_strength(name)
    context = {
            'Poster': full[name]["Poster"],
            'strength' : a.get_movemone_strength(name),
            'moveballs' : dic.bals_nbr,
            'power' : a.get_strength(dic),
            'chanse' : 50 - (int(l.split(".")[0]) * 10) + (a.get_strength(dic) * 5)
        }
    return render(request, 'battle.html', context)

def select(request):
    return render(request, 'select.html')

def start(request):
    return render(request, 'start.html')
