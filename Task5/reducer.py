import sys


def split_line(line):
    genre, movie = line.split(sep='\t')
    year = movie[-6:-2]
    title = movie[2:-9]
    return genre, title, year


def get_json_movies(genre, genre_movies):
    json_movies = ''
    for value in genre_movies[genre]:
        title, year = value
        json_movies += '{{"title":"{0}","year":"{1}"}},'.format(title, year)
    return json_movies[:-1]


def main():
    movies = dict()
    for line in sys.stdin:
        genre, title, year = split_line(line)
        if genre not in movies:
            movies[genre] = []
        movies[genre].append((title, year))

    for key in movies:
        print('{"genre":"' + key + '","movies":[', end='')
        print(get_json_movies(key, movies), end='')
        print(']}\n')


if __name__ == '__main__':
    main()
