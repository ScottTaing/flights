import time
import sys
import logging as log
import json

#def readRecord():
#    """Reads each record, where each record can be a json entry or in current
#    case a line from the CSV file"""
    

log.basicConfig(level=log.ERROR)

def compareTime(record, startTime, endTime, dest):
    """Compares whether a record falls within a time range or not"""

    #Since we know that currently the record is a string separated by commas and are stored as strings
    tokenizedRecord = record.rsplit(',')

    start = int(tokenizedRecord[2])
    end = int(tokenizedRecord[3])
    log.info('starting time %d and endtime %d'% (start,end))
    #log.info("Comparison starting time %d and endtime %d", startTime,endTime)
    if( tokenizedRecord[1] == dest):
        #printing out the record for the reducer with key as destination
        print '%s\t%s' %(tokenizedRecord[1], json.dumps(tokenizedRecord))
        return True
    else:
        return False

#TEST FUNCTIONS
def readRecord():
    """ Utility for generating the date from epoch mentioned in flight data file"""
    flightFile = open('flights-1000.csv')
    counter = 1
    for record in flightFile:
        tokenizedRecord = record.rsplit(',')
        start = int(tokenizedRecord[2])
        end = int(tokenizedRecord[3])
        log.info (counter, time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(start)), time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime(end))) 
        counter = counter + 1


def testFromCmdLine():
    flightFile = open('flights-1000.csv')
    if len(sys.argv) == 4:
        for record in flightFile:
            log.info (compareTime(record, int(sys.argv[1]),int(sys.argv[2]), sys.argv[3]))
            #log.info compareTime(record, 1304622575112, 1304883936090, 'KOA')
    else:
        log.info ("usage python flights.py <starttime> <endtime> dest")



if __name__ == '__main__':
    testFromCmdLine()
    #readRecord()
