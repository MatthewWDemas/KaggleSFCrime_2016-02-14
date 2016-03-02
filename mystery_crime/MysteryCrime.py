#!/usr/bin/python3
#MysteryCrime.py

#MysteryCrime object has fields: Id, dates, x (longitude), y (latitude),
#categories (dict).  categories is a dictionary with elements of "type:
#likelihood", which the number likelihood describes the probability that its
#corresponding "type" of crime (traffic violation, grand theft, etc).

class MysteryCrime:

    def __init__(self,Id,dates,x,y,categories_list):

        #'I' in 'Id' is capitalized because 'id' a reserved Python word
        self.Id = Id
        self.dates = dates
        self.x = x
        self.y = y
        self.categories = dict.fromkeys(categories_list,0) #init each to 0

    def likelihood_from_known_crime(self, crime):
        
