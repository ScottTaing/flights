#TODO Complete and review the documentation
Analyzing the flights data set from hack reduce

This project is a collection of scripts to present various statistics on https://github.com/hackreduce/Hackathon specifically https://github.com/hackreduce/Hackathon/tree/master/datasets/flights
The intent of the project is to take this data and calculate the mean, media, variance and standard deviation from the flight data and then plot it on a graph.

This will help a user to look into the past data and visualize the trends from the past that can help him predict a future model.


USAGE 

# WIP

This project is still a WIP. You can run the following scenarios currently:

---------------------------------------------------------
Finding a count of flights between a given time interval.
---------------------------------------------------------

You can currently achieve this by running either the following command

cat flights-1000.csv | ./flightsMapper.py | sort | ./flightsReducer.py 

or, running these scripts as a streaming job in map reduce. 

Currently the time range and the final destination airport code are hardcode in the flightsMapper.py

for record in sys.stdin:                                                       
     compareTime(record, 1304622575112, 1304883936090, 'KOA') 

You can modify this as per your requirement.

-> First argument is the start time since epoch -> 1304622575112
-> Second argument is the end time since epoch -> 1304883936090
-> Third argument is the airport code -> KOA

This should output something similar to 

KOA  (96489.56999999979, 163)

---------------------------------------------------------
Finding a count of flights for each of the desination airport
---------------------------------------------------------
> cat flights-1000.csv | ./flightsMapperGeneric.py | sort | ./flightsReducerGeneric.py 

This should output something similar to 

ACE  (3895.6000000000004, 2)
FUE	(43745.6, 15)
IBZ	(168029.5, 99)
KOA	(177437.78, 266)
MAD	(91238.39999999994, 59)
MAH	(749580.4999999994, 185)
MJV	(45405.69999999998, 19)
NAS	(119698.90000000023, 99)
SVQ	(255953.80000000002, 45)
TFN	(592324.7999999999, 198)
XRY	(26908.700000000004, 13)

Again, you can run the above via map reduce job

---------------------------------------------------------
Yet to be implemented
---------------------------------------------------------
-> Drawing graps from this showing deviation, median, mean 
Basically enabling the end user to look at these charts and make a decision whats the range and most suitable time to buy a ticket.