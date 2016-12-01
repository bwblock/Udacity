#! /usr/bin/env python
import webbrowser

class Movie():                          # Class

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):        #constructor

        self.title = movie_title        #  instance variable
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showtrailer(self):              # instance method
        webbrowser.open(self.trailer_youtube_url)





