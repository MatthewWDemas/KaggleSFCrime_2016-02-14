#!/usr/bin/python3
#distances_between_crimes.py

#for a given crime, find the distance to other crimes
#geo.py from http://hoegners.de/Maxi/geo/
import geo

#crimeA id=100 in table train
crimeA = geo.xyz(37.7641020287178,-122.435318423327)

#crimeB id=200 in table train
crimeB = geo.xyz(37.74394327043071,-122.422672192368)

print(geo.distance(crimeA,crimeB))
