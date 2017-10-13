import telepot

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

# list of sum of all ratings for each stall
rating_num = [130, 88, 46, 71, 96, 85, 69, 95, 70, 124, 65,
              136, 56, 21, 68, 135, 175, 125, 52, 21, 120,
              90, 95, 112, 117, 125, 31, 85, 125, 70, 90,
              125, 117, 21, 70, 90, 51, 46, 94, 95, 97,
              90, 55, 57, 115, 45, 69, 90, 71, 57, 79,
              43, 95, 68, 193, 158, 217, 160, 152, 103, 214,
              275, 105, 255, 290, 157, 119, 172, 103, 51, 250,
              191, 325, 280, 218, 159, 217, 227, 159, 180, 239,
              215, 159, 165, 98, 125, 69, 69, 41, 21, 95,
              95, 44, 68, 45]

# list of total ratings given for each stall
rating_div = [26, 29, 22, 23, 24, 21, 23, 24, 23, 31, 32,
              34, 28, 21, 23, 34, 35, 25, 26, 19, 24,
              30, 24, 28, 29, 25, 31, 28, 25, 23, 18,
              25, 29, 21, 23, 30, 25, 23, 31, 24, 24,
              30, 27, 29, 29, 22, 23, 30, 23, 28, 26,
              22, 24, 23, 48, 53, 54, 53, 51, 52, 54,
              55, 52, 64, 58, 53, 59, 57, 52, 51, 50,
              63, 65, 56, 54, 53, 54, 57, 53, 60, 59,
              54, 53, 55, 24, 25, 23, 17, 20, 21, 19,
              24, 22, 23, 22]

# list of average rating for each stall
rating_avg = [5, 3.03, 2.09, 3.09, 4, 4.05, 3, 3.96, 3.04, 4, 2.03,
              4, 2, 1, 2.96, 3.97, 5, 5, 2, 1.10, 5,
              3, 3.96, 4, 4.03, 5, 1, 3.04, 5, 3.04, 5,
              5, 4.03, 1, 3.04, 3, 2.04, 2, 3.03, 3.96, 4.04,
              3, 2.04, 1.97, 3.97, 2.05, 3, 3, 3.09, 2.04, 3.04,
              1.95, 3.96, 2.96, 4.02, 2.98, 4.02, 3.02, 2.98, 1.98, 3.96,
              5, 2.02, 3.98, 5, 2.96, 2.02, 3.02, 1.98, 1, 5,
              3.03, 5, 5, 4.04, 3, 4.02, 3.98, 3, 3, 4.05,
              3.98, 3, 3, 4.08, 5, 3, 4.06, 2.05, 1, 5,
              3.96, 2, 2.96, 2.05]

# ============= calculation of the nearest canteen ===============
# by comparing the distance between current location and different canteens
# function parameter: coordinate of current location
# function return: index(n) of the nearest canteen, list mz be written in foodbot.
#lat & long are the positions of the latitudes and longtudes of the canteens in the lists
def Nearest_Canteen(x, y):
    dis = 99999999
    n = lat = long = 0

    while lat < 12:
        if (pow(x - lat_list[lat], 2) + pow(y - long_list[long], 2) < dis):  # can 1
            dis = pow(x - lat_list[lat], 2) + pow(y - long_list[long], 2)
            n = lat
        lat += 1
        long += 1
    return n

# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose, using a dictionary to store the button's text

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service

menu = {
    'Halal Preference': {
        'Canteen 2': {
            'Halal': ('Store(s) Available: \nAyam Penyet\nI hope I helped you!!!')
        },
        'Canteen 14': {
            'Halal': ('Store(s) Available: \nMuslim Malay\nI hope I helped you!!!')
        },
        'Canteen 16': {
            'Halal': ('Store(s) Available: \nIndian Food\nI hope I helped you!!!')
        },
        'North Hill Canteen': {
            'Chinese': ('Store(s) Available: \nChicken Rice\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang And Indian Cuisine\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nNasi Padang And Indian Cuisine\nI hope I helped you!!!')
        },
        'North Spine Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian Food\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMalay BBQ\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Chinese': ('Store(s) Available: \nBan Mian Fish Soup\nYong Tau Foo\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang\nMuslim Food\nI hope I helped you!!!')
        }
    },
    'Vegetarian Preference': {
        'North Spine Canteen': {
            'Vegetarian': ('Store(s) Available: \nVegetarian Food\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Vegetarian': ('Stall(s) Available:\nVegetarian\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Vegetarian': ('Store(s) Available: \nVegetarian\nI hope I helped you!!!')
        }

    },
    'No Preference': {
        'Canteen 1': {
            'Japanese': ('Store(s) Available: \nMenya Takashi\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMala Talk\nHandmade Noodle\nBraised Rice And Noodle\nChinese Cuisine\nEconomical Rice\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Cuisine\nI hope I helped you!!!')
        },
        'Canteen 2': {
            'Korean': ('Store(s) Available: \nKorean Cuisine\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nChicken Rice\nXiao Long Bao\nYong Tau Foo\nSichuan Cuisine\nShandong Big Bao\
            \nEconomical Rice\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nKath’s Bakery\nThe Oven\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nAyam Penyet\nI hope I helped you!!!')
        },
        'Canteen 4': {
            'Chinese': ('Store(s) Available: \nZi Char / Fried Rice\nLa Mian\nI hope I helped you!!!')
        },
        'Canteen 9': {
            'Chinese': ('Store(s) Available: \nJiu Li Xiang Chuan Cai\nChinese Cuisine\nXian Noodles\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian\nI hope I helped you!!!')
        },
        'Canteen 11': {
            'Korean': ('Store(s) Available: \nKorean Food\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \n7 Fukijin Japanese Food\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMixed Veg Rice\nSi Chuan Mei Shi\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWaffles & Pastries\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Food\nI hope I helped you!!!')
        },
        'Canteen 13': {
            'Korean': ('Store(s) Available: \nKorean Cuisine\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \nJapanese Cuisine\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nNoodle Delight\nChinese Cuisine\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food\nI hope I helped you!!!')
        },
        'Canteen 14': {
            'Chinese': ('Store(s) Available: \nTaiwan\nSi Chuan\nAsian Food Delights\nBan Mian-Fish Soup\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMuslim Malay\nI hope I helped you!!!')
        },
        'Canteen 16': {
            'Japanese': ('Store(s) Available: \nJapanese Food\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nChinese Ramen\nSignature Dishes With Rice\nMala Hot Pot\nEconomical Rice\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Food\nI hope I helped you!!!')
        },
        'North Hill Canteen': {
            'Chinese': ('Store(s) Available: \nMixed Veg Rice\nTraditional Dough Fritters And Miniwok\nTraditional Handmade Fish Ball Noodle\
            \nChicken Rice\nAh Boon’s Fish Soup\nClaypot & Porridge\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Cuisine\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang And Indian Cuisine\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nNasi Padang And Indian Cuisine\nI hope I helped you!!!')
        },
        'North Spine Canteen': {
            'Korean': ('Store(s) Available: \nJapanese Korean Delight\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \nJapanese Korean Delight\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMini Wok\nYong Tau Foo\nChicken Rice\nHand-Made Noodles\nMixed Rice\
            \nCantonese Roast Duck\nSoup Delight\nVegetarian Food\nTaiwanese Cuisine\nXian Cuisine\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food\nBBQ Delight\nItalian Pasta\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMalay BBQ\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine\nI hope I helped you!!!'),
            'Vietnamese': ('Store(s) Available: \nVietnamese Cuisine\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Japanese': ('Store(s) Available: \nJapanese Cuisine\nSalad And Bento Express\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nVegetarian\nMixed Veg Rice\nDim Sum\nChinese Cuisine\nBan Mian Fish Soup\
            \nYong Tau Foo\nChicken Rice\nKoka Mee Express\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nPasta Express\nSalad And Bento Express\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian\nChicken Rice\nBan Mian & Fish Soup\nNoodle\nA-La-Carte\nChinese Food\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nSandwiches & Salad Bar\nWestern Food\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang\nMuslim Food\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian\nI hope I helped you!!!')
        }
    },
    'Give/Check stall rating': {
        'Canteen 1': {
            'Menya Takashi': 0,
            'Mala Talk': 1,
            'Handmade Noodle': 2,
            'Braised Rice And Noodle': 3,
            'Chinese Cuisine': 4,
            'Economical Rice': 5,
            'Western Cuisine': 6
        },
        'Canteen 2': {
            'Korean Cuisine': 7,
            'Chicken Rice': 8,
            'Xiao Long Bao': 9,
            'Yong Tau Foo': 10,
            'Sichuan Cuisine': 11,
            'Shandong Big Bao': 12,
            'Economical Rice': 13,
            'Kath’s Bakery': 14,
            'The Oven': 15,
            'Ayam Penyet': 16
        },
        'Canteen 4': {
            'Zi Char / Fried Rice': 17,
            'La Mian': 18
        },
        'Canteen 9': {
            'Jiu Li Xiang Chuan Cai': 19,
            'Chinese Cuisine': 20,
            'Xian Noodles': 21,
            'Western': 22,
            'Indian': 23
        },
        'Canteen 11': {
            'Korean Food': 24,
            '7 Fukijin Japanese Food': 25,
            'Mixed Veg Rice': 26,
            'Si Chuan Mei Shi': 27,
            'Waffles & Pastries': 28,
            'Indian Food': 29
        },
        'Canteen 13': {
            'Korean Cuisine': 30,
            'Japanese Cuisine': 31,
            'Noodle Delight': 32,
            'Chinese Cuisine': 33,
            'Western Food': 34
        },
        'Canteen 14': {
            'Taiwan': 35,
            'Si Chuan': 36,
            'Asian Food Delights': 37,
            'Ban Mian-Fish Soup': 38,
            'Muslim Malay': 39
        },
        'Canteen 16': {
            'Japanese Food': 40,
            'Chinese Ramen': 41,
            'Signature Dishes With Rice': 42,
            'Mala Hot Pot': 43,
            'Economical Rice': 44,
            'Indian Food': 45
        },
        'North Hill Canteen': {
            'Mixed Veg Rice': 46,
            'Traditional Dough Fritters And Miniwok': 47,
            'Traditional Handmade Fish Ball Noodle': 48,
            'Chicken Rice': 49,
            'Ah Boon’s Fish Soup': 50,
            'Claypot & Porridge': 51,
            'Western Cuisine': 52,
            'Nasi Padang And Indian Cuisine': 53
        },
        'North Spine Canteen': {
            'Japanese Korean Delight': 54,
            'Mini Wok': 55,
            'Yong Tau Foo': 56,
            'Chicken Rice': 57,
            'Hand-Made Noodles': 58,
            'Mixed Rice': 59,
            'Cantonese Roast Duck': 60,
            'Soup Delight': 61,
            'Vegetarian Food': 62,
            'Taiwanese Cuisine': 63,
            'Xian Cuisine': 64,
            'Western Food': 65,
            'BBQ Delight': 66,
            'Italian Pasta': 67,
            'Malay BBQ': 68,
            'Indian Cuisine': 69,
            'Vietnamese Cuisine': 70
        },
        'South Spine Canteen': {
            'Japanese Cuisine': 71,
            'Salad And Bento Express': 72,
            'Vegetarian': 73,
            'Mixed Veg Rice': 74,
            'Dim Sum': 75,
            'Chinese Cuisine': 76,
            'Ban Mian Fish Soup': 77,
            'Yong Tau Foo': 78,
            'Chicken Rice': 79,
            'Koka Mee Express': 80,
            'Pasta Express': 81,
            'Nasi Padang': 82,
            'Indian Cuisine': 83
        },
        'NIE Canteen': {
            'Vegetarian': 84,
            'Chicken Rice': 85,
            'Ban Mian & Fish Soup': 86,
            'Noodle': 87,
            'A-La-Carte': 88,
            'Chinese Food': 89,
            'Sandwiches & Salad Bar': 90,
            'Western Food': 91,
            'Nasi Padang': 92,
            'Muslim Food': 93,
            'Indian': 94
        }
    }
}
