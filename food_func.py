# !/usr/local/bin/python3
#  _*_ coding:utf8 _*_

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

#might not be needed, determine if canteens are open
import time

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)


#============= calculation of the nearest canteen ===============
# by comparing the distance between current location and different canteens
# function parameter: coordinate of current location
# function return: index of the nearest canteen, list mz be written in foodbot.
def Nearest_Canteen(x,y):
    dis=99999999
    n=0
    if (pow(x-1.346736,2)+pow(y-103.686092,2) < dis):#can 1
        dis = pow(x-1.346736,2)+pow(y-103.686092,2)
        n=0   	
    if (pow(x-1.348329,2)+pow(y-103.685547,2) < dis):#can 2
        dis = pow(x-1.348329,2)+pow(y-103.685547,2) 
        n=1
    if (pow(x-1.344169,2)+pow(y-103.685429,2) < dis):#can 4
        dis = pow(x-1.344169,2)+pow(y-103.685429,2)
        n=2
    if (pow(x-1.352216,2)+pow(y-103.685265,2) < dis):#can 9
        dis = pow(x-1.352216,2)+pow(y-103.685265,2)
        n=3
    if (pow(x-1.354903,2)+pow(y-103.686477,2) < dis):#can 11
        dis = pow(x-1.354903,2)+pow(y-103.686477,2)
        n=4
    if (pow(x-1.351722,2)+pow(y-103.681100,2) < dis):#can 13
        dis = pow(x-1.351722,2)+pow(y-103.681100,2)
        n=5
    if (pow(x-1.352648,2)+pow(y-103.682108,2) < dis):#can 14
        dis = pow(x-1.352648,2)+pow(y-103.682108,2)
        n=6
    if (pow(x-1.350299,2)+pow(y-103.680917,2) < dis):#can 16
        dis = pow(x-1.350299,2)+pow(y-103.680917,2)
        n=7
    if (pow(x-1.352648,2)+pow(y-103.682108,2) < dis):#north hill canteen
        dis = pow(x-1.352648,2)+pow(y-103.682108,2)
        n=8        
    if (pow(x-1.354395,2)+pow(y-103.680253,2) < dis):#north spine canteen
        dis = pow(x-1.354395,2)+pow(y-103.680253,2)
        n=9        
    if (pow(x-1.342459,2)+pow(y-103.682426,2) < dis):#south spine canteen koufu
        dis = pow(x-1.342459,2)+pow(y-103.682426,2)
        n=10        
    if (pow(x-1.348750,2)+pow(y-103.677611,2) < dis):#nie canteen
        dis = pow(x-1.348750,2)+pow(y-103.677611,2)
        n=11
        
    return n


# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service
def Welcome_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Get_Location', request_location=True)],
    [KeyboardButton(text = 'Halal Preference')],
    [KeyboardButton(text = 'Vegetarian')],
    [KeyboardButton(text = 'No Preference')]
    ],
    one_time_keyboard=True
    )
    return tmp

def Food_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Halal Preference')],
    [KeyboardButton(text = 'Vegetarian')],
    [KeyboardButton(text = 'No Preference')]
    ],
    one_time_keyboard=True
    )
    return tmp

def Vegetarian_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = ' North Spine Canteen (V)')],
    [KeyboardButton(text = ' South Spine Canteen (V)')],
    [KeyboardButton(text = ' NIE Canteen (V)')],
    ])
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
    ])
    return tmp

def Halal1_Preference_Keyboard(): ##Can remove
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 1 (H) Japanese')],
    [KeyboardButton(text = 'Canteen 1 (H) Chinese')],
    [KeyboardButton(text = 'Canteen 1 (H) Western')],
    [KeyboardButton(text = 'Canteen 1 (H) Malay')],
    [KeyboardButton(text = 'Canteen 1 (H) Indian')],
    [KeyboardButton(text = 'Canteen 1 (H) Vietnamese')]
    ])
    return tmp

def Halal2_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 2 (H) Malay')],
    ])
    return tmp

def Halal14_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 14 (H) Malay')],
    ])
    return tmp

def Halal16_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Canteen 16 (H) Indian')],
    ])
    return tmp

def HalalNH_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Hill Canteen (H) Chinese')],
    [KeyboardButton(text = 'North Hill Canteen (H) Malay')],
    [KeyboardButton(text = 'North Hill Canteen (H) Indian')],
    ])
    return tmp

def HalalNS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'North Spine Canteen (H) Chinese')],
    [KeyboardButton(text = 'North Spine Canteen (H) Malay')],
    [KeyboardButton(text = 'North Spine Canteen (H) Indian')],
    ])
    return tmp

def HalalSS_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'South Spine Canteen (H) Chinese')],
    [KeyboardButton(text = 'South Spine Canteen (H) Malay')],
    [KeyboardButton(text = 'South Spine Canteen (H) Indian')],
    ])
    return tmp

def HalalNIE_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'NIE Canteen (H) Chinese')],
    [KeyboardButton(text = 'NIE Canteen (H) Western')],
    [KeyboardButton(text = 'NIE Canteen (H) Malay')],
    ])
    return tmp

#============= No Preference Keyboards ===============

def No_Preference_Keyboard():
    tmp = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Canteen 1', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 2', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 4', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 9', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 11', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 13', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 14', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'Canteen 16', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'North Hill Canteen', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'North Spine Canteen', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'South Spine Canteen', callback_data = 'nil')],
    [InlineKeyboardButton(text = 'NIE Canteen', callback_data = 'nil')]
    ])
    return tmp

