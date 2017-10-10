# !/usr/local/bin/python3
#  _*_ coding:utf8 _*_

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

#might not be needed, determine if canteens are open
import time

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)

#list of latitudes of canteens
lat_list = [1.346628, 1.348363, 1.344189, 1.352270, 1.354908,
            1.351721, 1.352692, 1.350299, 1.354395, 1.347029,
            1.342459, 1.348746]

#list of longitudes of canteens
long_list = [103.686028, 103.685482, 103.685439, 103.685298, 103.686477,
             103.681082, 103.682108, 103.680914, 103.688173, 103.680254,
             103.682427, 103.677614]


# ============= calculation of the nearest canteen ===============
# by comparing the distance between current location and different canteens
# function parameter: coordinate of current location
# function return: index(n) of the nearest canteen, list mz be written in foodbot.
#lat & long are the positions of the latitudes and longtudes of the canteens in the lists
def Nearest_Canteen(x, y):
    dis = 99999999
    n = 0
    lat = 0
    long = 0

    while lat < 12:
        if (pow(x - lat_list[lat], 2) + pow(y - long_list[long], 2) < dis):  # can 1
            dis = pow(x - lat_list[lat], 2) + pow(y - long_list[long], 2)
            n = lat
        lat = lat + 1
        long = long + 1
    return n


# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service
def Welcome_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Find Nearest Canteen', request_location=True)],
    [KeyboardButton(text = 'Halal Preference')],
    [KeyboardButton(text = 'Vegetarian Preference')],
    [KeyboardButton(text = 'No Preference')]
    ],
    one_time_keyboard=True
    )
    return tmp

def Food_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Halal Preference')],
    [KeyboardButton(text = 'Vegetarian Preference')],
    [KeyboardButton(text = 'No Preference')]
    ],
    one_time_keyboard=True
    )
    return tmp


#any canteens without halal/veg? will have to remove


def Vegetarian_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = ' North Spine Canteen (V)')],
    [KeyboardButton(text = ' South Spine Canteen (V)')],
    [KeyboardButton(text = ' NIE Canteen (V)')],
    ],
    one_time_keyboard=True
    )
    return tmp


#============= Halal Preference Keyboards ===============

def Halal_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = ' Canteen 2 (H)')],
    [KeyboardButton(text = ' Canteen 14 (H)')],
    [KeyboardButton(text = ' Canteen 16 (H)')],
    [KeyboardButton(text = ' North Hill Canteen (H)')],
    [KeyboardButton(text = ' North Spine Canteen (H)')],
    [KeyboardButton(text = ' South Spine Canteen (H)')],
    [KeyboardButton(text = ' NIE Canteen (H)')],
    ],
    one_time_keyboard=True
    )
    return tmp

def Halal1_Preference_Keyboard(): ##Can remove
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 1 (H) Japanese')],
    [KeyboardButton(text = 'Canteen 1 (H) Chinese')],
    [KeyboardButton(text = 'Canteen 1 (H) Western')],
    [KeyboardButton(text = 'Canteen 1 (H) Malay')],
    [KeyboardButton(text = 'Canteen 1 (H) Indian')],
    [KeyboardButton(text = 'Canteen 1 (H) Vietnamese')]
    ],
    one_time_keyboard=True
    )
    return tmp

def Halal2_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 2 (H) Malay')],
    ],
    one_time_keyboard=True
    )
    return tmp

def Halal14_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 14 (H) Malay')],
    ],
    one_time_keyboard=True
    )
    return tmp

def Halal16_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 16 (H) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def HalalNH_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Hill Canteen (H) Chinese')],
    [KeyboardButton(text = 'North Hill Canteen (H) Malay')],
    [KeyboardButton(text = 'North Hill Canteen (H) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def HalalNS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Spine Canteen (H) Chinese')],
    [KeyboardButton(text = 'North Spine Canteen (H) Malay')],
    [KeyboardButton(text = 'North Spine Canteen (H) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def HalalSS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'South Spine Canteen (H) Chinese')],
    [KeyboardButton(text = 'South Spine Canteen (H) Malay')],
    [KeyboardButton(text = 'South Spine Canteen (H) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def HalalNIE_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'NIE Canteen (H) Chinese')],
    [KeyboardButton(text = 'NIE Canteen (H) Western')],
    [KeyboardButton(text = 'NIE Canteen (H) Malay')],
    ],
    one_time_keyboard=True
    )
    return tmp

#============= No Preference Keyboards ===============

def No_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 1 (N)')],
    [KeyboardButton(text = 'Canteen 2 (N)')],
    [KeyboardButton(text = 'Canteen 4 (N)')],
    [KeyboardButton(text = 'Canteen 9 (N)')],
    [KeyboardButton(text = 'Canteen 11 (N)')],
    [KeyboardButton(text = 'Canteen 13 (N)')],
    [KeyboardButton(text = 'Canteen 14 (N)')],
    [KeyboardButton(text = 'Canteen 16 (N)')],
    [KeyboardButton(text = 'North Hill Canteen (N)')],
    [KeyboardButton(text = 'North Spine Canteen (N)')],
    [KeyboardButton(text = 'South Spine Canteen (N)')],
    [KeyboardButton(text = 'NIE Canteen (N)')]
    ],
    one_time_keyboard=True
    )
    return tmp

def No1_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 1 (N) Japanese')],
    [KeyboardButton(text = 'Canteen 1 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 1 (N) Western')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No2_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 2 (N) Korean')],
    [KeyboardButton(text = 'Canteen 2 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 2 (N) Western')],
    [KeyboardButton(text = 'Canteen 2 (N) Malay')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No4_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 4 (N) Chinese')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No9_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 9 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 9 (N) Western')],
    [KeyboardButton(text = 'Canteen 9 (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No11_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 11 (N) Korean')],
    [KeyboardButton(text = 'Canteen 11 (N) Japanese')],
    [KeyboardButton(text = 'Canteen 11 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 11 (N) Western')],
    [KeyboardButton(text = 'Canteen 11 (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No13_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 13 (N) Korean')],
    [KeyboardButton(text = 'Canteen 13 (N) Japanese')],
    [KeyboardButton(text = 'Canteen 13 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 13 (N) Western')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No14_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 14 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 14 (N) Malay')],
    ],
    one_time_keyboard=True
    )
    return tmp

def No16_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 16 (N) Japanese')],
    [KeyboardButton(text = 'Canteen 16 (N) Chinese')],
    [KeyboardButton(text = 'Canteen 16 (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def NoNH_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Hill Canteen (N) Chinese')],
    [KeyboardButton(text = 'North Hill Canteen (N) Western')],
    [KeyboardButton(text = 'North Hill Canteen (N) Malay')],
    [KeyboardButton(text = 'North Hill Canteen (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def NoNS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Spine Canteen (N) Korean')],
    [KeyboardButton(text = 'North Spine Canteen (N) Japanese')],
    [KeyboardButton(text = 'North Spine Canteen (N) Chinese')],
    [KeyboardButton(text = 'North Spine Canteen (N) Western')],
    [KeyboardButton(text = 'North Spine Canteen (N) Malay')],
    [KeyboardButton(text = 'North Spine Canteen (N) Indian')],
    [KeyboardButton(text = 'North Spine Canteen (N) Vietnamese')],
    ],
    one_time_keyboard=True
    )
    return tmp

def NoSS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'South Spine Canteen (N) Japanese')],
    [KeyboardButton(text = 'South Spine Canteen (N) Chinese')],
    [KeyboardButton(text = 'South Spine Canteen (N) Western')],
    [KeyboardButton(text = 'South Spine Canteen (N) Malay')],
    [KeyboardButton(text = 'South Spine Canteen (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp

def NoNIE_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'NIE Canteen (N) Chinese')],
    [KeyboardButton(text = 'NIE Canteen (N) Western')],
    [KeyboardButton(text = 'NIE Canteen (N) Malay')],
    [KeyboardButton(text = 'NIE Canteen (N) Indian')],
    ],
    one_time_keyboard=True
    )
    return tmp
