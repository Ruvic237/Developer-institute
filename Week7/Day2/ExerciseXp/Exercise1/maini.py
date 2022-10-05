import json


def load_data(file_name):
     with open(file_name,"r") as show:
         store = json.load(show)
     return  store












