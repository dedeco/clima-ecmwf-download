#!/usr/bin/env python
import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
 
def retrieve_interim_sfc():
    """      
       A function to demonstrate how to iterate efficiently over several years and months etc    
       for a particular interim_request.     
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month. (eg "interim_daily_201510.nc")
    """
    yearStart = 2007
    yearEnd = 2016
    months = [1,2,3,10,11,12]
    for year in list(range(yearStart, yearEnd + 1)):
        for month in months:
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "_interim_daily_grid_075_sfc_%04d%02d.nc" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            interim_request(requestDates, target)
 
def interim_request(requestDates, target):
    """      
        An ERA interim request for analysis surface level data.
    """
    server.retrieve({   
        server.retrieve({
            "class": "ei",
            "stream": "oper",
            "type": "an",
            "dataset": "interim",
            "date": requestDates,
            "expver": "1",
            "step": "0",
            "levtype": "sfc",
            "area": "0/-60/-30/0",
            "param": "31.128/32.128/33.128/34.128/35.128/36.128/37.128/38.128/39.128/40.128/41.128/42.128/53.162/54.162/55.162/56.162/57.162/58.162/59.162/60.162/61.162/62.162/63.162/64.162/65.162/66.162/67.162/68.162/69.162/70.162/71.162/72.162/73.162/74.162/75.162/76.162/77.162/78.162/79.162/80.162/81.162/82.162/83.162/84.162/85.162/86.162/87.162/88.162/89.162/90.162/91.162/92.162/134.128/136.128/137.128/139.128/141.128/148.128/151.128/164.128/165.128/166.128/167.128/168.128/170.128/173.128/174.128/183.128/186.128/187.128/188.128/198.128/206.128/234.128/235.128/236.128/238.128",
            "format": "netcdf",
            "target": target,
            "time": "00/06/12/18",
            "grid": "0.75/0.75"
        })
        
if __name__ == '__main__':
    retrieve_interim_sfc()