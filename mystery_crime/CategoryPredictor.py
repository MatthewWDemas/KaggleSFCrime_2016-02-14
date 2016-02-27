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
        return geo.distance(geo.xyz(*coord1),geo.xyz(*coord2))

    def crimes_from_query(self,query):
        #initialize DB connector
        cnx = mysql.connector.connect(user='root', database='kaggle_sf')
        cursor = cnx.cursor()

        #test query
        query = "SELECT id,dates,dayofweek,pddistrict,address,x,y FROM train WHERE pddistrict = '%s'"%self.mystery_crime.pddistrict

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
            -4,
            "2015-05-10 23:10:00",
            "Sunday",
            "MISSION",
            "2900 Block of 16TH ST",
            "-122.418700097043",
            "37.7651649409646")

    print("Killin coords are",killin.get_coordinates())

    category_predictor = CategoryPredictor(killin)
    category_predictor.known_crimes = category_predictor.crimes_from_query("null")
    for crime in category_predictor.known_crimes:
        print("Distance between crimes %d and %d is %f m."%(crime.Id,killin.Id,category_predictor.dist_between_crimes(killin,crime)))
