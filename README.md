#TODO Complete and review the documentation
Analyzing the flights data set from hack reduce

This project is a collection of scripts to present various statistics on https://github.com/hackreduce/Hackathon specifically https://github.com/hackreduce/Hackathon/tree/master/datasets/flights
The intent of the project is to take this data and calculate the mean, media, variance and standard deviation from the flight data and then plot it on a graph.

This will help a user to look into the past data and visualize the trends from the past that can help him predict a future model.


USAGE 

#YET WIP

Currently you can run this as 
python flightsMapperTemp.py 1304622575112 1304883936090 'KOA' | sort | python flightsReducer.py

-> First argument is the start time since epoch
-> Second argument is the end time since epoch
-> Third argument is the airport code 

These scripts currently calculates the flighs that were there during this time period and calculate the sum of fares of all these flights


-)) Next step to do is calculate the mean, median, variance etc
