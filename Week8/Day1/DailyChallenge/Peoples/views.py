from django.shortcuts import render

# Create your views here.

Persons = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


def peoples(request):
    context = {
        "Persons": Persons,
    }
    return render(request, 'peoples.html', context)


def people(request, id):
    context = {
        "Persons": Persons,
        "id": id,
    }
    return render(request, 'people.html', context)
