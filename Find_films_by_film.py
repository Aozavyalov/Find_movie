import json

films = []
in_file = open("films.json", 'r')
for str_json in in_file:
    films.append(json.loads(str_json))
print('Введите точное название фильма, который вам нравится:')
name = input()
i = 0
my_film = {}
# ищем наш фильм в бд
while i < len(films) and my_film == {}:
    if name.lower() == films[i]['title'].lower() or name.lower() == films[i]['original_title'].lower():
        my_film = films[i]
    i += 1
if my_film != {}:
    # подбираем наиболее подходящие фильмы из списка
    rates = {} # сделаем рейтинг фильмов, которые наиболее похожи на наш
    for film in films:
        rate = 0
        if my_film['title'] != film['title']:
            if film['belongs_to_collection'] == my_film['belongs_to_collection']:
                    rate += 20
            genres = set()
            for genre in film['genres']:
                for my_genre in my_film['genres']:
                    if genre['name'] == my_genre['name'] and genre['name'] not in genres:
                        genres.add(genre['name'])
            rate += len(genres)*10
            rate += 10 * abs(10 - (my_film['vote_average'] - film['vote_average']))
            rates[rate] = film

    i = 0
    for rate in sorted(rates, reverse=True):
        print(rates[rate]['title'])
        if i == 9:
            break
        i += 1
else:
    print('К сожалению, такого фильма в базе данных нет(')