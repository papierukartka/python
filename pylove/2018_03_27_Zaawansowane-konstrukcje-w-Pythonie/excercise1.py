#!/usr/bin/pyton3
# encoding: utf-8

import requests
from collections import namedtuple
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from collections import defaultdict, Counter
import string

def measure_time(func):
    '''
    Dekorator mierzacy czas wykonania funkcji, pretty cool i'd say
    '''
    def wrapped(*args, **kwargs):
        start = datetime.now()
        print(start)
        resp = func(*args, **kwargs)
        end = datetime.now()
        print(end)
        print(end - start)
        return resp
    return wrapped

@measure_time
def z191():
    '''
    Pobierz losowe dane z https://pylove.org/exercise/1_19_1 i ułóż hasło tylko z unikalnych słów.
    '''
    wynik = []
    data = requests.get('https://pylove.org/exercise/1_19_1')
    data = set(data.json())
    for d in data:
        wynik.append(d)

    return (' '.join(wynik))

def z192():
    '''
    Pobierz losowe dane z https://pylove.org/exercise/1_19_2 i
    znajdź hasło, na które złoży się 6 najpopularniejszych
    liter w kolejności malejącej według wystąpień. Rozwiaz za pomoca defaultdict
    '''
    start = datetime.now()
    print(f"start: {start}")
    data = requests.get('https://pylove.org/exercise/1_19_1').json()

    zliczacz = defaultdict(int)

    for let in data:
        zliczacz[let] += 1

    slowo = ''
    for _ in range(6):
        a_max = 0
        a_let = ''
        for k, v in zliczacz.items():
            if v > a_max:
                a_max = v
                a_let = k
        del zliczacz[a_let]
        slowo += a_let

    stop = datetime.now()
    print(f"stop: {stop}")
    print(f"trwalo: {stop-start}")
    return zliczacz

def z194():
    '''
    Pobierz losowe dane z https://pylove.org/exercise/1_19_2 i
    znajdź hasło, na które złoży się 6 najpopularniejszych
    liter w kolejności malejącej według wystąpień. Rozwiaz za pomoca Counter
    '''

    data = requests.get('https://pylove.org/exercise/1_19_1').json()
    counter = Counter(data)
    slowo = ''
    for let in counter.most_common(6):
        pass

    return slowo


if __name__ == "__main__":
    # previous_date = datetime.now()
    # pierwsze = getWords()
    # drugie = defaultdict(str)
    # trzecie = getwords_defaultdict()
    czwarte = z194()
    print(czwarte)
    # counter = Counter()

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=22)
    # namedtuple jest rownowazne:
    # class Ojciec:
    #     def __init__(self, x,y):

