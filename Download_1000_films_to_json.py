import urllib.request
import urllib.parse
import urllib.error
import json
import time


def write_films_to_file(films_list, filename):
    with open(filename, 'w') as file:
        for film in films_list:
            file.write(json.dumps(film) + '\n')


def try_to_get_film(film_number, api_key):
    url = 'https://api.themoviedb.org/3/movie/%d?api_key=%s&language=ru' % (film_number, api_key)
    try:
        film = urllib.request.urlopen(url).read().decode('utf-8')
        print('Film number %d saved' % film_number)
        return json.loads(film)
    except urllib.error.HTTPError:
        print('Can`t save film #%d' % film_number)
        return {}


def sleep_if_too_much_requests(time_of_cycle, max_time_of_requests, count_of_requests, max_requests_in_time):
    if time.time() - time_of_cycle < max_time_of_requests and count_of_requests % max_requests_in_time == 0:
        time.sleep(10 - (time.time() - time_of_cycle))
        return time.time()
    else:
        return time_of_cycle


def file_check(filename):
    try:
        len_of_file = 0
        with open(filename, 'r') as films_file:
            for line in films_file:
                len_of_file += 1
        return len_of_file >= 1000
    except FileNotFoundError:
        return False


def write_films_from_file_to_list(films, filename):
    with open(filename, 'r') as films_file:
        for film in films_file:
            films.append(json.loads(film))


def get_1000_films():
    films_base = []
    file = 'films.json'
    if not file_check(file):
        print('Input your api key:')
        api_key = input()
        time_of_cycle = time.time()
        film_number = 1
        while len(films_base) != 1000:
            time_of_cycle = sleep_if_too_much_requests(time_of_cycle, 10, film_number, 40)
            film = try_to_get_film(film_number, api_key)
            if film != {}:
                films_base.append(film)
            film_number += 1
        write_films_to_file(films_base, file)
    else:
        write_films_from_file_to_list(films_base, file)
        if __name__ == "__main__":
            print('There are %d films in file' % len(films_base))
    return films_base


if __name__ == "__main__":
    get_1000_films()
