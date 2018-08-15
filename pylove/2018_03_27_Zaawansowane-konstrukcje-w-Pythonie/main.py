#!/usr/bin/pyton3
# encoding: utf-8

from collections import namedtuple
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from collections import defaultdict, Counter

if __name__ == "__main__":
    jakis_tam_set = set()
    jakis_tam_set = {'a', 'b', 'c'}

    # Read

    jakis_tam_set = {'a', 'b', 'c'}
    for el in jakis_tam_set:
        print(el)

    # Update

    a = {'a', 'b', 'c'}
    a.add('a')
    a.add('d')
    assert len(a) == 4

    # Delete
    #1
    a = {'a', 'b', 'c'}
    a.clear()
    assert a == set()

    #2 remove - usun jesli jest, jesli nie - error
    a = {'a', 'b', 'c'}
    # a.remove('d')
    # a.remove('a')
    # assert 'a' not in a

    #3 discard - usun jesli jest, jesli nie - nic
    a = {'a', 'b', 'c'}
    a.discard('d')
    a.discard('a')
    assert 'a' not in a

    #4 pop - usun i zwroc element wyrzucony (wyrzucony losowy element, bo to set)
    a = {'a', 'b', 'c'}
    b = a.pop()
    assert b not in a
    a = {'a', 'b', 'c'}
    a.update({'g', 'f'})
    a.update(['z', 'x'])
    a.update(('p', 'o'))
    a.update({'u': '1', 't': '2'})

    # sprawdzanie braku części wspólnej
    a = {'a', 'b', 'c'}
    b = {'c', 'd', 'e'}
    assert a.isdisjoint(b) == False

    # sprawdzanie czy zbiór jest podzbiorem innego zbioru
    a = {'a', 'b', 'c', 'd'}
    b = {'c', 'd'}
    assert b.issubset(a) == True

    # sprawdzanie czy zbiór jest nadzbiorem innego zbioru
    assert a.issuperset(b) == True


    a = {'a', 'b', 'c'}
    b = {'c', 'd', 'e'} # {'a', 'b'}

    a.difference(b) # {'a', 'b'} - {'b', 'a'}


    a.intersection(b) # {'c'}


    a.symmetric_difference(b) # {'b', 'a', 'd', 'e'}


    a.union(b) # {'b', 'd', 'a', 'c', 'e'}

    # date

    a_date = date(day=12, month=8, year=2009)
    today = date.today()

    today.day
    today.month
    today.year
    today.weekday()  # 0 = poniedzialek, 6 = niedziela
    today = today.replace(day=12, year=2009, month=8)

    date.fromtimestamp(1)  # epoh (1970, 1, 1)
    date.fromtimestamp(1234123141)  # (2009, 2, 8)

    today - a_date

    # time

    a_time = time(minute=12, second=13, hour=4)
    a_time.hour
    a_time.minute
    a_time.microsecond

    # datetime

    a_date = datetime(2017, 3, 26, 23, 41, 45, 620822)
    str(a_date)
    start = datetime.now()
    diff = datetime.now() - start

    # timedelta

    td = timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    a_date = datetime(2017, 3, 26, 23, 41, 45, 620822)
    a_date += td
    a_date
    i = td

    # defaultdict

    a = defaultdict(list)
    a['x'].append('1')

    b = defaultdict(str)
    b['b'] += 'ma kota'
    b['b'] += 'ma kota'

    a = defaultdict(dict)
    a = defaultdict(int)

    # counter - dict / defaultdict, operuje na roznych typach danych

    # count elements from a string
    c = Counter('abcdeabcdabcaba')
    # count elements from a list
    c = Counter(['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b', 'a'])
    c.most_common()  # most common elements
    c.most_common(3)  # three most common elements
    sum(c.values())  # suma wszystkich elementow

    # namedtuple - tupla, ktorej wartosci mozna pozyskac po kluczu zamiast po wspolrzednych, optymalna pamieciowo