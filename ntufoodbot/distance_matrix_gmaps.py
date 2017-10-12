from datetime import datetime
import time

import googlemaps

#===required for using google api
gmaps = googlemaps.Client(key='AIzaSyChyx38fw6qtO12-FC99wEyK3u9gcgcXj8')

def GetAllDistance_Canteen(origins, destinations):
    
    matrix_distance = gmaps.distance_matrix(origins, destinations, mode = 'walking')
    return_list = []
    #===generate list of distance and duration for all destinations
    for key in matrix_distance['rows'][0]['elements']:
        tmpObj = [key['distance']['text'],key['duration']['text']]
        return_list.append(tmpObj)
    return return_list
