import random

class Template:
    def __init__(self, title, publising_year, genre):
        self.title = title
        self.publishing_year = publising_year
        self.genre = genre

        #variables
        self.plays_number = 0

    def play(self):
        self.plays_number += 1

class Films(Template):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.title} ({self.publishing_year})"

class Series(Template):
    def __init__(self, title, publising_year, genre, episode_number, season_number):
        super().__init__(title, publising_year, genre)
        self.episode_number = episode_number
        self.season_number = season_number

    def __repr__(self):
        return f"{self.title} S{self.number_format(self.season_number)}E{self.number_format(self.episode_number)}"

    def number_format(self, numer):
        return str(numer).zfill(2)
        
films_series = [
    Films("Pulp Fiction", 1994, "dramat"),
    Films("Incepcja", 2010, "sci-fi"),
    Series("Breaking Bad", 2008, "dramat", 1, 1),
    Series("The Simpsons", 1989, "animowany", 1, 5),
    Films("Interstellar", 2014, "sci-fi"),
    Series("Friends", 1994, "komedia", 2, 1)
]
#Get movies from list
def get_movies(films_series):
    return sorted([media for media in films_series if isinstance(media, Films)], key=lambda x: x.title)

#Get series from list
def get_series(film_series):
    return sorted([media for media in films_series if isinstance(media, Series)], key=lambda x: x.title)

#Search for specific title
def search(films_series, title):
    search_list = []
    for item in films_series:
        if item.title.lower() == title.lower():
            search_list.append(item)
    if len(search_list) == 0:
        print("Wrong title!")
        exit(1)
    return search_list

#Generate views
def generate_views(films_series):
    element = random.choice(films_series)
    views = random.randint(1, 100)
    element.play()
    element.plays_number += views

#generate_views 10x
def run_generate_views(films_series, number):
    for _ in range(number):
        generate_views(films_series)

#top_titles
def top_titles(films_series, num_titles):
    sorted_media = sorted(films_series, key=lambda x: x.plays_number, reverse=True)
    top = sorted_media[:num_titles]
    return [media for media in top]


if __name__ == "__main__":
    #Show movies info
    print("Films available on the library: ")
    movies = get_movies(films_series)
    for movie in movies:
        print(movie)

    #Show series info
    print("\nSeries available on the library: ")
    series = get_series(films_series)
    for serie in series:
        print(serie)
    
    #Search
    search_title = input("\nSearch for the title you are interested in: ")
    search_result = search(films_series, search_title)
    for result in search_result:
        print(result)

    #Run generate_views 10x
    run_generate_views(films_series, 10)

    #Shows the most popular titles
    print("\nShows the most popular titles: ")
    num_top_titles = 3
    top_titles_list = top_titles(films_series, num_top_titles)
    for item in top_titles_list:
        print(f"{item}, number of plays: {item.plays_number}")

