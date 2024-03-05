class Movie:
    def __init__(self,title,rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating

    @property
    def rating(self):
        return self._rating 
    
    @rating.setter
    def rating(self,new_rating):
        if 1.0 <= new_rating<= 5.0:
            self._rating = new_rating
        else: 
            print("Please enter a valid rating")


my_movie = Movie("Cars",5.0)
my_movie.rating = 5.1
print(f'My movie rating: {my_movie.rating}')

