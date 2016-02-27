#!/usr/bin/python3
#Crime.py

#The Crime object has the fields shared by both known crimes (from train.csv)
#and mystery crimes (from test.csv).  They are:
#    -dates
#    -dayofweek
#    -pddistrict
#    -address
#    -x (longitude)
#    -y (latitude)
    
class Crime:
    def __init__(self,dates,dayofweek,pddistrict,address,x,y):

        self.dates = dates
        self.dayofweek = dayofweek
        self.pddistrict = pddistrict
        self.address = address
        self.x = x
        self.y = y

    def get_coordinates(self):
        #return list of floats
        return [float(i) for i in [self.y,self.x]]
        

#test case; only runs when ./Crime.py is called from command line
if __name__ == "__main__":
    stabbin = Crime(
            "2016-01-01 00:00:01",
            "Wednesday",
            "Mission",
            "100 Valencia Ave",
            "-122.39958770418998",
            "37.7350510103906")

    killin = Crime(
            "2016-01-02 00:00:01",
            "Wednesday",
            "Mission",
            "VANNESS AV",
            "-122.42436302145",
            "37.8004143219856")

    print("Stabbin coords are",stabbin.get_coordinates())
    print("Killin coords are",killin.get_coordinates())

