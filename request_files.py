#!/usr/bin/env python
import calendar
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
 

import os
import collections

def getfiles(type='sfc'):
    regs = {}
    for y in range(2006,2016+1):
        regs[y] = []
    for file in os.listdir("./"):
        if file.endswith(".nc"):
            x = file.split('_')
            if x[5] == type:
                year = int(x[6].split('.')[0][:4])
                mo = int(x[6].split('.')[0][4:])
                if regs.get(year,0):
                    regs[year].append(mo)
                else:
                    regs[year] = []
                    regs[year].append(mo)
    d = collections.OrderedDict(sorted(regs.items()))
    for k,v in d.items():
        v.sort()
        d[k] = [i for i in range(1,13) if i not in v]
    print (d)
    return d



def retrieve_interim_sfc():
    """
       A function to demonstrate how to iterate efficiently over several years and months etc    
       for a particular interim_request.     
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month. (eg "interim_daily_201510.nc")
    """
    params = "31.128/32.128/33.128/34.128/35.128/36.128/37.128/38.128/39.128/40.128/41.128/42.128/53.162/54.162/55.162/56.162/57.162/58.162/59.162/60.162/61.162/62.162/63.162/64.162/65.162/66.162/67.162/68.162/69.162/70.162/71.162/72.162/73.162/74.162/75.162/76.162/77.162/78.162/79.162/80.162/81.162/82.162/83.162/84.162/85.162/86.162/87.162/88.162/89.162/90.162/91.162/92.162/134.128/136.128/137.128/139.128/141.128/148.128/151.128/164.128/165.128/166.128/167.128/168.128/170.128/173.128/174.128/183.128/186.128/187.128/188.128/198.128/206.128/234.128/235.128/236.128/238.128"
    time = "00/06/12/18"
    step = "0"
    yearStart = 2014
    yearEnd = 2014
    months = [1,2,3,4,5,6,7,8,9,10,11,12] 

    year_mo = getfiles('sfc')

    #for year in list(range(yearStart, yearEnd + 1)):
    #    for month in months:
    for year, months in year_mo.items():
        for month in months:
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "_interim_daily_grid_050_sfc_%04d%02d.nc" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            interim_request(requestDates, target,"sfc",params, time, step, None)

def retrieve_interim_pl():
    """
       A function to demonstrate how to iterate efficiently over several years and months etc    
       for a particular interim_request.     
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month. (eg "interim_daily_201510.nc")
    """
    params = "60.128/129.128/130.128/131.128/132.128/133.128/135.128/138.128/155.128/157.128/203.128/246.128/247.128/248.128"
    time = "00/06/12/18"
    step = None
    yearStart = 2016
    yearEnd = 2016
    months = [1,2,3,4,5,6,7,8,9,10,11,12] 
    levelist = "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000"

    year_mo = getfiles('pl')

    for year, months in year_mo.items():
        for month in months:
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "_interim_daily_grid_050_pl_%04d%02d.nc" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            interim_request(requestDates, target,"pl",params, time, None, levelist)


def interim_request(requestDates, target, levtype, params, time, step=None, levelist=None, ttype='an'):
    """
        An ERA interim request for analysis surface level data.
    """
    d = {
        "class": "ei",
        "stream": "oper",
        "type": ttype,               # analysis (versus forecast, fc)
        "dataset": "interim",
        "date": requestDates,       # dates, set automatically from above
        "expver": "1",
        "levtype": levtype,         # pressure level data (versus surface, sfc, and model level, ml)
        "area": "0/-60/-30/0",      # Optional. Subset (clip) to an area. Specify as N/W/S/E in Geographic lat/long degrees. Southern latitudes and western longitudes must be given as negative numbers. Requires "grid" to be set to a regular grid, e.g. "0.25/0.25".
        "param": params,            # here: Geopotential (z), Specific humidity (q), Relative humidity (r), Fraction of cloud cover (cc); see http://apps.ecmwf.int/codes/grib/param-db
        "format": "netcdf",         # Optional. Output in NetCDF format. Requires that you also specify 'grid'. If not set, data is delivered in GRIB format, as archived.
        "target": target,           # output file name, set automatically from above
        "time": time,               # times of analysis (with type:an), or initialization time of forecast (with type:fc)
        "grid": "0.50/0.50"         #Optional for GRIB, required for NetCDF. The horizontal resolution in decimal degrees. If not set, the archived grid as specified in the data documentation is used.
    }

    if step:
        d["step"] = step             # The ERA-Interim dataset contains analyses (four times per day, at 00:00, 06:00, 12:00 and 18:00), as well as forecasts (from 00:00 and 12:00, with 3, 6, 9, and 12-hour steps, and more, into the future), as shown below.

    if levelist:
        d["levelist"] = levelist    # levels, required only with levtype:pl and levtype:ml 

    #print(d)

    server.retrieve(d)


def retrieve_dly_tot_prcp():

    """
       A function to demonstrate how to iterate efficiently over several years and months etc    
       for a particular interim_request.     
       Change the variables below to adapt the iteration to your needs.
       You can use the variable 'target' to organise the requested data in files as you wish.
       In the example below the data are organised in files per month. (eg "interim_daily_201510.nc")
    """
    params = "228.128"
    time = "00/12"
    step = "12"

    year_mo = getfiles('sfc')

    for year, months in year_mo.items():
        for month in months:
            startDate = '%04d%02d%02d' % (year, month, 1)
            numberOfDays = calendar.monthrange(year, month)[1]
            lastDate = '%04d%02d%02d' % (year, month, numberOfDays)
            target = "dly_tot_prcp_grid_050_sfc_%04d%02d.nc" % (year, month)
            requestDates = (startDate + "/TO/" + lastDate)
            interim_request(requestDates, target,"sfc",params, time, step, None, ttype='fc')   

if __name__ == '__main__':
    #retrieve_interim_sfc()
    retrieve_interim_pl()
    #retrieve_dly_tot_prcp()
