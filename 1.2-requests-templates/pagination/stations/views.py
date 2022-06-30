from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations_list = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stations_dict = {}
            bus_stations_dict['Name'] = row['Name']
            bus_stations_dict['Street'] = row['Street']
            bus_stations_dict['District'] = row['District']
            bus_stations_list.append(bus_stations_dict)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': paginator.page(page_number),
        'page': page,
    }
    return render(request, 'stations/index.html', context)
