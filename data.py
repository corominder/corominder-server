import populartimes 
import datetime
from math import sqrt


place_types = []
class MapData():
    api_key = None
    def __init__(self, api_key):
        self.api_key = api_key
    

    def get(self, location, threshold, search_radius):
        data = populartimes.get(self.api_key, place_types, (location[0]-search_radius, location[1] - search_radius), (location[0]+search_radius, location[1] + search_radius), radius=1000)
        day = datetime.datetime.today().weekday()
        hour = datetime.datetime.today().hour

        result = []
        for place in data:
            popularity = place['populartimes'][day]['data'][hour]
            if popularity >= threshold:
                coordinates = place['coordinates']
                result.append({'coordinates' : coordinates, 'radius' : popularity})

        return result

