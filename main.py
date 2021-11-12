from math import *
from time import daylight
from geopy.geocoders import Nominatim
from datetime import datetime, date

def day_length(lat, dia):
    declination = 23.45*sin(radians(360/365*(284+dia)))

    that_product = -tan(radians(lat))*tan(radians(declination))
    duration = 2*degrees(acos(that_product))/15

    return duration

place = str(input("Onde você está? "))
loc = Nominatim(user_agent='GetLoc')
location = loc.geocode(place)



latitude = location.latitude
day = datetime.now().timetuple().tm_yday

duration_in_hours = day_length(latitude, day)

print(f'{int(duration_in_hours)}h{round(60*(duration_in_hours-int(duration_in_hours)))}min')
