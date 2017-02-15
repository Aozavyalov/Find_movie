import urllib.request
import urllib.parse
import json
import time


def try_to_get_film(film_number, api_key):
    films_file = open("films.json", 'a')
    url = 'https://api.themoviedb.org/3/movie/%s?api_key=%s&language=ru' % (str(film_number), api_key)
    try:
        film = urllib.request.urlopen(url).read().decode('utf-8')
        films_file.write(film + '\n')
        films_file.close()
        print('Film number %d saved' % film_number)
        return json.loads(film)
    except:
        print('Can`t save film #%d' % film_number)
        films_file.close()
        return {}


def sleep_if_no_10_secs(time_of_cycle, num):    # sleep, if too much requests in 10 secs
    if time.time() - time_of_cycle < 10 and num % 40 == 0:
        time.sleep(10 - (time.time() - time_of_cycle))
    return time.time()


def file_check():
    try:
        films_file = open("films.json", 'r')
        len_of_file = 0
        for line in films_file:
            len_of_file += 1
        films_file.close()
        if len_of_file >= 1000:
            return True
        else:
            return False
    except:
        return False


def write_films_from_file_to_list(films):
    films_file = open("films.json", 'r')
    for film in films_file:
        films.append(json.loads(film))
    films_file.close()


def get_1000_films():
    films_base = []
    if not file_check():
        print('Input your api key:')
        api_key = input()
        time_of_cycle = time.time()
        film_number = 1
        while len(films_base) != 1000:
            time_of_cycle = sleep_if_no_10_secs(time_of_cycle=time_of_cycle, num=film_number)
            film = try_to_get_film(film_number, api_key)
            if film != {}:
                films_base.append(film)
            film_number += 1
    else:
        write_films_from_file_to_list(films=films_base)
        print('There are %d films in file' % len(films_base))
    return films_base


if __name__ == "__main__":
    get_1000_films()
