import operator

class Passanger:
    def __init__(self):
        self.person = 'Random person with no name'
    
    def set_name(self, name):
        self.person = name
    
    def get_name(self, name):
        return self.person

    def say(self, phrase):
        return f"{self.person} says {phrase}"
    
    def sit(self, place):
        assert type(place) == int
        return f"{self.person} took place number {place}"

class Train:

    def wagon(self, passengers):
        pass

    def runs(self, speed):
        pass

    def estimate_travel_time(self, source, destination):
        pass

if __name__ == "__main__":
    pomorzanin = Train()
    pasazer_wojtek = Passanger()
    pasazer_wojtek.set_name('wojtek')
    wojtek_says = pasazer_wojtek.say('hello')
    print(wojtek_says)

    encourage_to_say = operator.attrgetter('say')
    wojteks_cue = encourage_to_say(pasazer_wojtek)("ENGLISH MOTHERFUCKER DO YOU SPEAK IT")
    print(wojteks_cue)
    
