from datetime import datetime
import time

import googlemaps


gmaps = googlemaps.Client(key='AIzaSyChyx38fw6qtO12-FC99wEyK3u9gcgcXj8')



def GetAllDistance_Canteen(origins, destinations):
 #   origins = [x,y]
#destinations = [[1.346736,103.686092],[1.352216,103.685265],"ntu", "nus"]
    matrix_distance = gmaps.distance_matrix(origins, destinations, mode = 'walking')
    return_list = []
#    di0=matrix_distance['rows'][0]['elements'][0]['distance']['text']
#    du0=matrix_distance['rows'][0]['elements'][0]['duration']['text']
#    di1=matrix_distance['rows'][0]['elements'][1]['distance']['text']
#    du1=matrix_distance['rows'][0]['elements'][1]['duration']['text']   
#    di2=matrix_distance['rows'][0]['elements'][2]['distance']['text']
#    du2=matrix_distance['rows'][0]['elements'][2]['duration']['text']   
#    di3=matrix_distance['rows'][0]['elements'][3]['distance']['text']
#    du3=matrix_distance['rows'][0]['elements'][3]['duration']['text']
#    di4=matrix_distance['rows'][0]['elements'][4]['distance']['text']
#    du4=matrix_distance['rows'][0]['elements'][4]['duration']['text']   
#    di5=matrix_distance['rows'][0]['elements'][5]['distance']['text']
#    du5=matrix_distance['rows'][0]['elements'][5]['duration']['text']   
#    di6=matrix_distance['rows'][0]['elements'][6]['distance']['text']
#    du6=matrix_distance['rows'][0]['elements'][6]['duration']['text']   
#    di7=matrix_distance['rows'][0]['elements'][7]['distance']['text']
#    du7=matrix_distance['rows'][0]['elements'][7]['duration']['text']   
#    di8=matrix_distance['rows'][0]['elements'][8]['distance']['text']
#    du8=matrix_distance['rows'][0]['elements'][8]['duration']['text']   
#    di9=matrix_distance['rows'][0]['elements'][9]['distance']['text']
#    du9=matrix_distance['rows'][0]['elements'][9]['duration']['text']   
#    di10=matrix_distance['rows'][0]['elements'][10]['distance']['text']
#    du10=matrix_distance['rows'][0]['elements'][10]['duration']['text']   
#    di11=matrix_distance['rows'][0]['elements'][11]['distance']['text']
#    du11=matrix_distance['rows'][0]['elements'][11]['duration']['text']   

    
    for key in matrix_distance['rows'][0]['elements']:
        tmpObj = [key['distance']['text'],key['duration']['text']]
        return_list.insert(0,tmpObj)

    return return_list
    #CREATEA  LIST THEN RETURN I91
