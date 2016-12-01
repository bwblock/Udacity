#! /usr/bin/env python

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


bad_boys = media.Movie("Bad Boys",
                       "Marcus Burnett (Martin Lawrence) and Mike Lowrey (Will Smith) are best friends and detectives in the narcotics division of the Miami Police Department. ",
                       "https://upload.wikimedia.org/wikipedia/en/a/a8/Bad_Boys.jpg",
                       "https://www.youtube.com/watch?v=ty8eBdHaf1c")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "The film tells the story of Lloyd Christmas and Harry Dunne, two unintelligent friends from Providence, Rhode Island",
                              "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
                              "https://www.youtube.com/watch?v=T1uQZhQzQAI")

good_bad_ugly = media.Movie("The Good, The Bad, and The Ugly",
                            "The plot revolves around three gunslingers competing to find fortune in a buried cache of Confederate gold",
                            "https://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                            "https://www.youtube.com/watch?v=WCN5JJY_wiA")


#print avatar.storyline

#avatar.showtrailer()

movies = [toy_story,avatar,good_bad_ugly]

fresh_tomatoes.open_movies_page(movies)

