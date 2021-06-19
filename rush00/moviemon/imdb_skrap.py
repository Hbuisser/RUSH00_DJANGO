import requests, json, sys

class Big_one():
    def __init__(self, d=None, my_list=None):
        self.index=0
        self.my_list = ["King Kong", "Godzilla", "Alien", "Venom",
        "The Meg", "Mummy", "Piranha 3dd", "Frankenstien", "Dracula",
        "The Invisible Man"]
    # class Data_for_one:
    #     return
    class Movemone():
        def __init__(self, name=None):
            data = self.get_movie(self.my_list[self.index])
            strength = self.get_strenght()
            print(strength)

    def get_strength(self):
        self.json.loads(self.d))

    def get_movie(self, arg):
        self.d = dict()
        response = requests.get("http://www.omdbapi.com/?t={}&apikey=23bea02c&type=movie&r=json&".format(arg))
        t = response.json()
        for key in t.items():
            self.d[key[0]] = key[1]
        index += 1
        return self.d
    
    # def load(self, name):

def test(arg):
    a = Big_one()
    k = a.get_strength()
    print(k.d["Ratings"])




if __name__ == '__main__':
    test(sys.argv[1:])