import download_1000_films_to_json


def find_films_by_name(film_title, all_films):
    founded_films = []
    for film in all_films:
        if film['title'].lower().find(film_title.lower()) != -1 or film['original_title'].lower().find(film_title.lower()) != -1:
            founded_films.append(film)
    return founded_films


def print_founded_films(founded_films, film_title):
    for film in founded_films:
        if film_title.lower() == film['title'].lower():
            print('There is film with the same title: %s )' % film['title'])
        else:
            print(film['title'])

if __name__ == '__main__':
    films = download_1000_films_to_json.get_1000_films()
    print('Input a word from a film`s title:')
    name = input()
    films = find_films_by_name(name, films)
    print_founded_films(films, name)
