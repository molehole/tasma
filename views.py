from django.shortcuts import render, redirect
import unicodecsv as csv
# Create your views here.

def index(request):
    return render(request, 'tasma/index.html', {})

def import_data(request):
    rows = {}
    with open('dane.txt', 'rb') as f:
        tresc = csv.reader(f, delimiter=';')
        for row in tresc:
            a = row.split(';')
            rows.append(a)
    return render(request, 'tasma/index.html', {'dane': rows})