from django.shortcuts import render
from django.conf import settings

def create_file(col, line, start_c, start_l)
    with open(settings.LOG_FILE_PATH, 'a+') as f:

def base(request):
    col = range(settings.GRID_SIZE[0])
    line = range(settings.GRID_SIZE[1])
    start = settings.START_POINT
    start_c = start[1]
    start_l = start[0]
    create_file(col, line, start_c, start_l)
    context = {
        'col': col,
        'line': line,
        'start_l': start_l,
        'start_c': start_c
    }
    return render(request, 'base.html', context)