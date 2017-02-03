from django.shortcuts import render, redirect

import unicodecsv as csv
import datetime
#Models
from .models import Etykieta, TA, Zamowienia

def index(request):
    return render(request, 'tasma/index.html', {'dane': TA.objects.all})

def import_data(request):
    with open('tasma/dane.txt', 'rb') as f:   
        tresc = csv.reader(f, delimiter=';')
        for row in tresc:
            T, created = TA.objects.get_or_create(nr=int(row[6]),
                data=datetime.datetime.strptime(row[1], '%Y%m%d'),
                grupa=str(row[10]),
                )
            E, created = Etykieta.objects.get_or_create(nr=int(row[9]),
                ta=T,
                pozycja=int(row[7]),                
                element=str(row[12])
                )
        return redirect('/tasma')

def dodaj(request, *args, **kwargs):
    if request.POST:
        etykieta = request.POST['etykieta']
        kod = request.POST['kod']
        try:
            etykieta = Etykieta.objects.get(nr=etykieta)
            Zamowienia.objects.get_or_create(etykieta=etykieta,
                kod=kod)
        except Exception as e:
            return False


