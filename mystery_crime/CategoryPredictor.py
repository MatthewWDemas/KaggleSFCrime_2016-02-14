#!/usr/bin/python3
#CategoryPredictor.py

from Crime import Crime
import geo
import mysql.connector

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

        #known_crimes is list of Crime objects to compare to mystery_crime
        self.known_crimes = []

    #takes two crime objects and returns the distance between them
    #verify correect distance with http://www.gpsvisualizer.com/calculators
    def dist_between_crimes(self,crime1,crime2):
        coord1 = crime1.get_coordinates()
        coord2 = crime2.get_coordinates()

        #splat operator * turns fnctn(['p','p']) into fnctn('p1','p2')
        dist = geo.distance(geo.xyz(*coord1),geo.xyz(*coord2))

        #avoid 1/r^2 singularities with 100 m min dist
        return dist if dist > 100 else 100

    def crimes_from_query(self,query):
        #initialize DB connector
        cnx = mysql.connector.connect(user='root', database='kaggle_sf')
        cursor = cnx.cursor()

        #test query
        query = "SELECT id,dates,category,dayofweek,pddistrict,address,x,y FROM train WHERE pddistrict = '%s'"%self.mystery_crime.pddistrict

        #submit query
        try:
            #super dangerous!!  never expose this API to the public!
            cursor.execute(query) 
        except mysql.connector.Error as err:
            print("Mysql query error: {}".format(err))
            exit(1)

        return [Crime(*c) for c in cursor]
        
#test case; only runs when ./Crime.py is called from command line
if __name__ == "__main__":
    #get crime from test.csv (dummy crime below simulates that)
    killin = Crime(
            -1,
            "2012-07-27 19:00:00",
            "DOMESTIC VIOLENCE",
            "Sunday",
            "MISSION",
            "2900 Block of 16TH ST",
            "-122.411093822635",
            "37.7610475742041")

    category_predictor = CategoryPredictor(killin)
    category_predictor.known_crimes = category_predictor.crimes_from_query("null")

    #calc prob dist array
    for known_crime in category_predictor.known_crimes:
        r = category_predictor.dist_between_crimes(killin,known_crime)
        category_predictor.category_probabilities[known_crime.category]+=1/(r*r)

    for key, value in category_predictor.category_probabilities.items():
        print(value, key)
