import json

films = []
in_file = open("films.json", 'r')
for str_json in in_file:
    films.append(json.loads(str_json))
print('Введите слово, которое содержится в названии фильма:')
name = input()
for film in films:
    if film['title'].lower().find(name.lower()) != -1 or film['original_title'].lower().find(name.lower()) != -1:
        print(film['title'])
