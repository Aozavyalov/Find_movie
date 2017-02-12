import urllib.request
import urllib.parse
import json
import time

films_base = []
api_key = '216472dda059242061bbeb827a5bdaa4'
films_file = open("films.json", 'w')
# add films to base
time_of_cycle = time.time()
amount_of_films = 1000
film_number = 1
while film_number != amount_of_films + 1:

    if time.time() - time_of_cycle < 10 and film_number % 40 == 0:
        time.sleep(10 - (time.time() - time_of_cycle))
        time_of_cycle = time.time()

    url = 'https://api.themoviedb.org/3/movie/' + str(film_number) + '?api_key=' + api_key + '&language=ru'
    try:
        film = urllib.request.urlopen(url).read().decode('utf-8')
        films_base.append(json.loads(film))
        films_file.write(film + '\n')
        print('Film number %d saved' % film_number)
    except:
        amount_of_films += 1
    film_number += 1
