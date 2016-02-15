summary(train)

train <- dfCharToFact(train)

library(dismo)
# https://cran.r-project.org/doc/contrib/intro-spatial-rl.pdf
library(rgdal)
library(ggmap)
library(rgeos)
library(maptools)
library(tmap)


mymap <- gmap("France")  # choose whatever country
plot(mymap)
