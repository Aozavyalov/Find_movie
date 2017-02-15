# Find_movie

This project is an example of using The Movie DB(TMDB) API. To use is you need to have a key, to get it sign up in https://www.themoviedb.org/.

Saw2_budget.py sends a request to TMDB with movie number(215), your API key, and get json data(dictionary in Python). So it's easy to print budget of saw 2.

Download_1000_films_to_json.py checks the file 'films.json'. If there are 1000 lines, nothing will happend. Else it will download 1000 json string and write to the file. 

Find_films_by_name.py uses previous .py file for getting 1000 films, after that it search all films with titles and original titles, containing a string or a substring, you entered.

Find_films_by_film.py also uses Download_1000_films_to_json.py to get 1000 films. It search a film with a title you entered, and make a rating of films, which have the same parameters. Belonging to one collection adds 20 points, every same genre adds 10 points, differens between average votes multiplies by 10 and adds to rating. Then it print 10 films with max rating.
