import webbrowser
class Movie():
    """This class provides blueprint for movies"""
    valid_rating = ["G","PG","PG-13","R"]
    def __init__(self,movie_title, movie_story_line, movie_poster_img, movie_url):
        self.title =movie_title
        self.storyLine =movie_story_line
        self.poster_image_url  =movie_poster_img
        self.trailer_youtube_url=movie_url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)