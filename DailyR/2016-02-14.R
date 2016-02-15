summary(train)

train <- dfCharToFact(train)

library(dismo)
library(rgdal)
library(ggmap)
library(rgeos)
library(maptools)
library(tmap)


mymap <- gmap("France")  # choose whatever country
plot(mymap)
