# Megicians

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for items in magician_names:
        print(items)
# show_magicians(magician_names)

def make_great(magician_names):
    magician_names.append("the great")
    
make_great(magician_names)
show_magicians(magician_names)


