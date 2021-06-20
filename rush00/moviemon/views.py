from django.shortcuts import render
from django.conf import settings
import pickle
from . import imdb_skrap

def create_file(pos_l, pos_c, out_of_range):
    data = Data(0, ["lol", "kek"], None, pos_l, pos_c, out_of_range)
    fi = open("pickle", "wb")
    pickle.dump(data, fi)

class Data():
    def __init__(self, movebals=None, p_names=None, info=None, pos_l=0, pos_c=0, out_of_range=False):
        self.size = [10, 10]
        self.pos_l = pos_l
        self.pos_c = pos_c
        self.out_of_range = out_of_range
        self.movebals = movebals
        self.p_names = p_names
        self.info = info

def load(request):
    col = range(settings.GRID_SIZE[0])
    line = range(settings.GRID_SIZE[1])
    col_file = settings.GRID_SIZE[0]
    line_file = settings.GRID_SIZE[1]
    res = ""
    end = False
    try:
        f = open("pickle", "rb")
        res = pickle.load(f)
        f.close()
    except:
        print("Wrong file ")
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
    create_file(res.pos_l, res.pos_c, res.out_of_range)
    context = {
        'col': col,
        'line': line,
        'pos_l': res.pos_l,
        'pos_c': res.pos_c
    }
    return render(request, 'moviemon/base.html', context)

def load_default_settings(request):
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
    create_file(pos_l, pos_c, out_of_range)
    return render(request, 'moviemon/base.html', context)

def begin(request):
    main = imdb_skrap.Big_one()
    
    button = request.GET.get('button', None)
    if button == None:
        return main.load_default_settings(request)
    else:
        return main.load(request)