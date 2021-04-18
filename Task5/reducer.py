import sys


def split_line(line):
    genre, movie = line.split(sep='\t')
    year = movie[-6:-2]
    title = movie[2:-9]
    return genre, title, year


def sort_movies(genre, genre_movies):
    genre_movies[genre] = sorted(genre_movies[genre], key=lambda x: (-int(x[1]), x[0]))


def get_json_movies(genre, genre_movies, count_n):
    json_movies = ''
    for value in genre_movies[genre][:count_n]:
        title, year = value
        json_movies += '{{"title":"{0}","year":"{1}"}},'.format(title, year)
    return json_movies[:-1]


def main():
    count_n = parse_arg()
    movies = dict()
    for line in sys.stdin:
        genre, title, year = split_line(line)
        if genre not in movies:
            movies[genre] = []
        movies[genre].append((title, year))

    for key in movies:
        sort_movies(key, movies)
        print('{"genre":"' + key + '","movies":[', end='')
        print(get_json_movies(key, movies, count_n), end='')
        print(']}\n')


def parse_arg():
    count_n = sys.argv[1]
    if count_n == '':
        count_n = None
    else:
        count_n = int(count_n.split('=')[1])
    return count_n


if __name__ == '__main__':
    main()
