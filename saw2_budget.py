import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def get_saw_2_budget(api_key):
    movie_num = '215'
    print(make_tmdb_api_request(method='/movie/'+movie_num, api_key=api_key)['budget'])

if __name__ == "__main__":
    print("Input your api key:")
    my_api_key = input()
    get_saw_2_budget(api_key=my_api_key)
