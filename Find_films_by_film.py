import Download_1000_films_to_json


def find_main_film(films):
    print('Введите точное название фильма, который вам нравится:')
    name = input()
    founded_film = {}
    for i in range(len(films)):
        if name.lower() == films[i]['title'].lower() or name.lower() == films[i]['original_title'].lower():
            founded_film = films[i]
            break
    return founded_film


def print_founded_films(rates):
    for num, rate in enumerate(sorted(rates, reverse=True)):
        print(num + 1, rates[rate]['title'])
        if num == 9:
            break


def find_film_by_film():
    films = Download_1000_films_to_json.get_1000_films()
    film_by_searching = find_main_film(films)
    # ищем наш фильм в бд
    if film_by_searching != {}:
        # подбираем наиболее подходящие фильмы из списка
        rates = {}  # сделаем рейтинг фильмов, которые наиболее похожи на наш
        for film in films:
            rate = 0
            rate_if_in_collection = 20
            rate_if_same_genre = 10
            if film_by_searching['title'] != film['title']:
                if film['belongs_to_collection'] == film_by_searching['belongs_to_collection']:
                    rate += rate_if_in_collection
                genres = set()
                for genre in film['genres']:
                    for my_genre in film_by_searching['genres']:
                        if genre['name'] == my_genre['name'] and genre['name'] not in genres:
                            genres.add(genre['name'])
                rate += len(genres) * rate_if_same_genre
                diff_between_votes = abs(10 - (film_by_searching['vote_average'] - film['vote_average']))
                rate += 10 * diff_between_votes
                rates[rate] = film
        print_founded_films(rates)
    else:
        print('К сожалению, такого фильма в базе данных нет(')

if __name__ == '__main__':
    find_film_by_film()
