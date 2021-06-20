from django.shortcuts import render
from django.conf import settings
import pickle
from . import imdb_skrap

def create_file(pos_l, pos_c, out_of_range):
    data = Data(0, ["lol", "kek"], None, pos_l, pos_c, out_of_range)
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

def battle(request, id):
    a = imdb_skrap.Big_one()
    m = a.get_random_movie()
    full = a.get_all_moviemons()
    print(full[m]["Poster"])
    id = full[m]["imdbID"]
    print(id)
    context = {
            'Poster': full[m]["Poster"],
        }
    return render(request, 'battle.html', context)
