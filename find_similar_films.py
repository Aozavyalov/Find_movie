import download_1000_films_to_json
import find_films_by_name


def find_film_with_same_title(films):
    print('Input the exact title of the movie, you like:')
    title = input()
    founded_films = find_films_by_name.find_films_by_name(title, films)
    for film in founded_films:
        if title == film['title']:
            return film
    return {}


def print_founded_films(rates, count_of_films):
    for num, rate in enumerate(sorted(rates, reverse=True)):
        print(num + 1, rates[rate]['title'])
        if num == count_of_films-1:
            break


def rate_film(film, film_with_which_compare):
    rating_of_film = 0
    rate_if_in_collection = 100
    rate_if_same_genre = 10
    max_vote = 10
    multiplier_of_diff_between_votes = 10
    if film['belongs_to_collection'] == film_with_which_compare['belongs_to_collection']:
        rating_of_film += rate_if_in_collection
    genres = set()
    for genre in film['genres']:
        for my_genre in film_with_which_compare['genres']:
            if genre['name'] == my_genre['name'] and genre['name'] not in genres:
                genres.add(genre['name'])

    rating_of_film += len(genres) * rate_if_same_genre
    diff_between_votes = abs(max_vote - (film_with_which_compare['vote_average'] - film['vote_average']))
    rating_of_film += multiplier_of_diff_between_votes * diff_between_votes
    return rating_of_film


def find_similar_films():
    films = download_1000_films_to_json.get_1000_films()
    film_with_input_title = find_film_with_same_title(films)

    if film_with_input_title != {}:
        rating_of_all_films = {}
        for film in films:
            if film_with_input_title['title'] != film['title']:
                rating_of_one_film = rate_film(film, film_with_input_title)
                rating_of_all_films[rating_of_one_film] = film
        print_founded_films(rating_of_all_films, 10)
    else:
        print('There is no this film in base(')

if __name__ == '__main__':
    find_similar_films()
