import Download_1000_films_to_json


def find_film_by_name():
    films = Download_1000_films_to_json.get_1000_films()
    print('Input a word from a film`s title:')
    name = input()
    for film in films:
        if film['title'].lower().find(name.lower()) != -1 or film['original_title'].lower().find(name.lower()) != -1:
            print(film['title'])


if __name__ == '__main__':
    find_film_by_name()
