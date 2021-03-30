class Movie:
    def __init__(self, genre='', name='', year=-1, rating=0):
        self.genre = genre
        self.name = name
        self.year = year
        self.rating = rating

    def get_rating(self):
        return self.rating

    def get_genre(self):
        return self.genre

    def __str__(self):
        return '{},"{}",{},{:.2f}'.format(self.genre, self.name, self.year, self.get_rating())

    def __lt__(self, other):
        return self.rating < other.rating
