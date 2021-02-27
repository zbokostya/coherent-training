class Film:
    def __init__(self, genre='', name='', year=-1, rating_sum=0, rating_count=0):
        self.genre = genre
        self.name = name
        self.year = year
        self.rating_sum = rating_sum
        self.rating_count = rating_count

    def get_rating(self):
        return self.rating_sum / self.rating_count if self.rating_count else 0

    def __str__(self):
        return '{},"{}",{},{:.2f}'.format(self.genre, self.name, self.year, self.get_rating())
