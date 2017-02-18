import  media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

batman = media.Movie("Batman",
                        "A story about a guy in a costume saving the city ",
                        "https://thegeekintel.files.wordpress.com/2013/02/batman-the-dark-knight-3_00448943.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")
Bond = media.Movie("James Bond",
                     "A story about a guy who works as a secert agent",
                     "https://s-media-cache-ak0.pinimg.com/originals/95/8d/a6/958da6795b2bd8cf1224636a44b93604.jpg",
                     "https://www.youtube.com/watch?v=7GqClqvlObY")
Agent47 = media.Movie("Agent47",
                   "A story about a guy who works as a secert agent",
                   "http://s3.foxmovies.com/foxmovies/production/films/72/images/posters/379-film-page-large.jpg",
                   "https://www.youtube.com/watch?v=Pv7lgQ8hiz0")

Serendipity  = media.Movie("Serendipity",
                      "A story about a guy who likes this girl that believes in fate",
                      "https://upload.wikimedia.org/wikipedia/en/a/a5/Serendipity_poster.jpg",
                      "https://www.youtube.com/watch?v=Pv7lgQ8hiz0")

Arrow = media.Movie("Arrow",
                          "A story about a guy who kicks as under a hood",
                          "https://cdn.cloudpix.co/images/stephen-amell/arrow-arrow-cw-tv-405d75945172940fce6a4c655ab0cb61-large-162017.jpg",
                          "https://www.youtube.com/watch?v=Pv7lgQ8hiz0")
movie =[toy_story,batman,Bond,Agent47,Serendipity,Arrow]
#fresh_tomatoes.open_movies_page(movie)
#print(media.Movie.valid_rating);
#print(media.Movie.__doc__);

#print(media.Movie.__module__);

#print(media.Movie.__name__);


#print(batman.storyLine)
#https://www.youtube.com/watch?v=MIxIk6TVZVE
#batman.show_trailer()
#toy_story.show_trailer()
