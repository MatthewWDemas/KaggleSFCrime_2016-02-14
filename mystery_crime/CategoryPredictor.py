#!/usr/bin/python3
#CategoryPredictor.py

from Crime import Crime
import geo

#CategoryPredictor object is initalized with a crime of unknown category and
#builds an array of probabilities for each category
    
class CategoryPredictor:
    def __init__(self,mystery_crime):
        self.mystery_crime = mystery_crime
        
        crime_categories = ['ARSON',
                            'ASSAULT',
                            'BAD CHECKS',
                            'BRIBERY',
                            'BURGLARY',
                            'DISORDERLY CONDUCT',
                            'DRIVING UNDER THE INFLUENCE',
                            'DRUG/NARCOTIC',
                            'DRUNKENNESS',
                            'EMBEZZLEMENT',
                            'EXTORTION',
                            'FAMILY OFFENSES',
                            'FORGERY/COUNTERFEITING',
                            'FRAUD',
                            'GAMBLING',
                            'KIDNAPPING',
                            'LARCENY/THEFT',
                            'LIQUOR LAWS',
                            'LOITERING',
                            'MISSING PERSON',
                            'NON-CRIMINAL',
                            'OTHER OFFENSES',
                            'PORNOGRAPHY/OBSCENE MAT',
                            'PROSTITUTION',
                            'RECOVERED VEHICLE',
                            'ROBBERY',
                            'RUNAWAY',
                            'SECONDARY CODES',
                            'SEX OFFENSES FORCIBLE',
                            'SEX OFFENSES NON FORCIBLE',
                            'STOLEN PROPERTY',
                            'SUICIDE',
                            'SUSPICIOUS OCC',
                            'TREA',
                            'TRESPASS',
                            'VANDALISM',
                            'VEHICLE THEFT',
                            'WARRANTS',
                            'WEAPON LAWS']

        #make dictionary initialized to zero of all crime categories, e.g.:
        #        'ARSON'     :0,
        #        'ASSAULT'   :0,
        #        'BAD CHECKS':0,
        #        'BRIBERY'   :0,
        #        ...
#http://stackoverflow.com/a/2244026/1717828
        self.category_probabilities = {cat: 0 for cat in crime_categories}        

    #takes two crime objects and returns the distance between them
    #verify correect distance with http://www.gpsvisualizer.com/calculators
    def dist_between_crimes(self,crime1,crime2):
        coord1 = crime1.get_coordinates()
        coord2 = crime2.get_coordinates()

        #splat operator * turns fnctn(['p','p']) into fnctn('p1','p2')
        return geo.distance(geo.xyz(*coord1),geo.xyz(*coord2))
        
#test case; only runs when ./Crime.py is called from command line
if __name__ == "__main__":
    stabbin = Crime(
            "2016-01-01 00:00:01",
            "Wednesday",
            "Mission",
            "100 Valencia Ave",
            "-122.407532192495",
            "37.7781942181426")

    killin = Crime(
            "2016-01-02 00:00:01",
            "Wednesday",
            "Mission",
            "VANNESS AV",
            "-122.485073656871",
            "37.72399838089769")

    print("Stabbin coords are",stabbin.get_coordinates())
    print("Killin coords are",killin.get_coordinates())

    category_predictor = CategoryPredictor(stabbin)
    print("Distance between crimes is",category_predictor.dist_between_crimes(killin,stabbin))
