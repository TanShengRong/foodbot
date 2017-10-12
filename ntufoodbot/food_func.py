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
            'Halal': ('Store(s) Available: \nAyam Penyet ' + str(rating_avg[16]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 14': {
            'Halal': ('Store(s) Available: \nMuslim Malay ' + str(rating_avg[39]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 16': {
            'Halal': ('Store(s) Available: \nIndian Food ' + str(rating_avg[45]) + '⭐\nI hope I helped you!!!')
        },
        'North Hill Canteen': {
            'Chinese': ('Store(s) Available: \nChicken Rice ' + str(rating_avg[49]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang And Indian Cuisine ' + str(rating_avg[53]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nNasi Padang And Indian Cuisine ' + str(rating_avg[53]) + '⭐\nI hope I helped you!!!')
        },
        'North Spine Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian Food ' + str(rating_avg[62]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMalay BBQ ' + str(rating_avg[68]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine ' + str(rating_avg[69]) + '⭐\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Chinese': ('Store(s) Available: \nBan Mian Fish Soup ' + str(rating_avg[77]) + '⭐\nYong Tau Foo '
                        + str(rating_avg[78]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang ' + str(rating_avg[82]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine ' + str(rating_avg[83]) + '⭐\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian ' + str(rating_avg[84]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food ' + str(rating_avg[91]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang ' + str(rating_avg[92]) + '⭐\nMuslim Food ' + str(rating_avg[93]) + '⭐\nI hope I helped you!!!')
        }
    },
    'Vegetarian Preference': {
        'North Spine Canteen': {
            'Vegetarian': ('Store(s) Available: \nVegetarian Food ' + str(rating_avg[62]) + '⭐\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Vegetarian': ('Stall(s) Available:\nVegetarian ' + str(rating_avg[73]) + '⭐\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Vegetarian': ('Store(s) Available: \nVegetarian ' + str(rating_avg[84]) + '⭐\nI hope I helped you!!!')
        }

    },
    'No Preference': {
        'Canteen 1': {
            'Japanese': ('Store(s) Available: \nMenya Takashi ' + str(rating_avg[0]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMala Talk ' + str(rating_avg[1]) + '⭐\nHandmade Noodle ' + str(rating_avg[2]) +
                        '⭐\nBraised Rice And Noodle ' + str(rating_avg[3]) + '⭐\nChinese Cuisine ' + str(rating_avg[4]) +
                        '⭐\nEconomical Rice ' + str(rating_avg[5]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Cuisine ' + str(rating_avg[6]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 2': {
            'Korean': ('Store(s) Available: \nKorean Cuisine ' + str(rating_avg[7]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nChicken Rice ' + str(rating_avg[8]) + '⭐\nXiao Long Bao ' + str(rating_avg[9]) +
                        '⭐\nYong Tau Foo ' + str(rating_avg[10]) + '⭐\nSichuan Cuisine ' + str(rating_avg[11]) +
                        '⭐\nShandong Big Bao ' + str(rating_avg[12]) + '⭐\nEconomical Rice ' + str(rating_avg[13]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nKath’s Bakery ' + str(rating_avg[14]) + '⭐\nThe Oven ' + str(rating_avg[15]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nAyam Penyet ' + str(rating_avg[16]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 4': {
            'Chinese': ('Store(s) Available: \nZi Char / Fried Rice ' + str(rating_avg[17]) + '⭐\nLa Mian '
                        + str(rating_avg[18]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 9': {
            'Chinese': ('Store(s) Available: \nJiu Li Xiang Chuan Cai ' + str(rating_avg[19]) + '⭐\nChinese Cuisine '
                         + str(rating_avg[20]) + '⭐\nXian Noodles ' + str(rating_avg[21]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern ' + str(rating_avg[22]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian ' + str(rating_avg[23]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 11': {
            'Korean': ('Store(s) Available: \nKorean Food ' + str(rating_avg[24]) + '⭐\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \n7 Fukijin Japanese Food ' + str(rating_avg[25]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMixed Veg Rice ' + str(rating_avg[26]) + '⭐\nSi Chuan Mei Shi '
                        + str(rating_avg[27]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWaffles & Pastries ' + str(rating_avg[28]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Food ' + str(rating_avg[29]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 13': {
            'Korean': ('Store(s) Available: \nKorean Cuisine ' + str(rating_avg[30]) + '⭐\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \nJapanese Cuisine ' + str(rating_avg[31]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nNoodle Delight ' + str(rating_avg[32]) + '⭐\nChinese Cuisine '
                        + str(rating_avg[33]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food ' + str(rating_avg[34]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 14': {
            'Chinese': ('Store(s) Available: \nTaiwan ' + str(rating_avg[35]) + '⭐\nSi Chuan ' + str(rating_avg[36])
                        + '⭐\nAsian Food Delights ' + str(rating_avg[37]) + '⭐\nBan Mian-Fish Soup ' + str(rating_avg[38])
                        + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMuslim Malay ' + str(rating_avg[39]) + '⭐\nI hope I helped you!!!')
        },
        'Canteen 16': {
            'Japanese': ('Store(s) Available: \nJapanese Food ' + str(rating_avg[40]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nChinese Ramen ' + str(rating_avg[41]) + '⭐\nSignature Dishes With Rice '
                        + str(rating_avg[42]) + '⭐\nMala Hot Pot ' + str(rating_avg[43]) + '⭐\nEconomical Rice '
                        + str(rating_avg[44]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Food ' + str(rating_avg[45]) + '⭐\nI hope I helped you!!!')
        },
        'North Hill Canteen': {
            'Chinese': ('Store(s) Available: \nMixed Veg Rice ' + str(rating_avg[46]) + '⭐\nTraditional Dough Fritters And Miniwok '
                        + str(rating_avg[47]) + '⭐\nTraditional Handmade Fish Ball Noodle ' + str(rating_avg[48])
                        + '⭐\nChicken Rice ' + str(rating_avg[49]) + '⭐\nAh Boon’s Fish Soup ' + str(rating_avg[50])
                        + '⭐\nClaypot & Porridge ' + str(rating_avg[51]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Cuisine ' + str(rating_avg[52]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang And Indian Cuisine ' + str(rating_avg[53]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nNasi Padang And Indian Cuisine ' + str(rating_avg[53]) + '⭐\nI hope I helped you!!!')
        },
        'North Spine Canteen': {
            'Korean': ('Store(s) Available: \nJapanese Korean Delight ' + str(rating_avg[54]) + '⭐\nI hope I helped you!!!'),
            'Japanese': ('Store(s) Available: \nJapanese Korean Delight ' + str(rating_avg[54]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nMini Wok ' + str(rating_avg[55]) + '⭐\nYong Tau Foo ' + str(rating_avg[56])
                        + '⭐\nChicken Rice ' + str(rating_avg[57]) + '⭐\nHand-Made Noodles ' + str(rating_avg[58])
                        + '⭐\nMixed Rice ' + str(rating_avg[59]) + '⭐\nCantonese Roast Duck ' + str(rating_avg[60])
                        + '⭐\nSoup Delight ' + str(rating_avg[61]) + '⭐\nVegetarian Food ' + str(rating_avg[62])
                        + '⭐\nTaiwanese Cuisine ' + str(rating_avg[63]) + '⭐\nXian Cuisine ' + str(rating_avg[64]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nWestern Food ' + str(rating_avg[65]) + '⭐\nBBQ Delight ' + str(rating_avg[66])
                        + '⭐\nItalian Pasta ' + str(rating_avg[67]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nMalay BBQ ' + str(rating_avg[68]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine ' + str(rating_avg[69]) + '⭐\nI hope I helped you!!!'),
            'Vietnamese': ('Store(s) Available: \nVietnamese Cuisine ' + str(rating_avg[70]) + '⭐\nI hope I helped you!!!')
        },
        'South Spine Canteen': {
            'Japanese': ('Store(s) Available: \nJapanese Cuisine ' + str(rating_avg[71]) + '⭐\nSalad And Bento Express '
                         + str(rating_avg[72]) + '⭐\nI hope I helped you!!!'),
            'Chinese': ('Store(s) Available: \nVegetarian ' + str(rating_avg[73]) + '⭐\nMixed Veg Rice ' + str(rating_avg[74])
                        + '⭐\nDim Sum ' + str(rating_avg[75]) + '⭐\nChinese Cuisine ' + str(rating_avg[76])
                        + '⭐\nBan Mian Fish Soup ' + str(rating_avg[77]) + '⭐\nYong Tau Foo ' + str(rating_avg[78])
                        + '⭐\nChicken Rice ' + str(rating_avg[79]) + '⭐\nKoka Mee Express ' + str(rating_avg[80]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nPasta Express ' + str(rating_avg[81]) + '⭐\nSalad And Bento Express '
                        + str(rating_avg[72]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang ' + str(rating_avg[82]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian Cuisine ' + str(rating_avg[83]) + '⭐\nI hope I helped you!!!')
        },
        'NIE Canteen': {
            'Chinese': ('Store(s) Available: \nVegetarian ' + str(rating_avg[84]) + '⭐\nChicken Rice ' + str(rating_avg[85])
                        + '⭐\nBan Mian & Fish Soup ' + str(rating_avg[86]) + '⭐\nNoodle ' + str(rating_avg[87]) + '⭐\nA-La-Carte '
                        + str(rating_avg[88]) + '⭐\nChinese Food ' + str(rating_avg[89]) + '⭐\nI hope I helped you!!!'),
            'Western': ('Store(s) Available: \nSandwiches & Salad Bar ' + str(rating_avg[90])
                        + '⭐\nWestern Food ' + str(rating_avg[91]) + '⭐\nI hope I helped you!!!'),
            'Malay': ('Store(s) Available: \nNasi Padang ' + str(rating_avg[92])
                      + '⭐\nMuslim Food ' + str(rating_avg[93]) + '⭐\nI hope I helped you!!!'),
            'Indian': ('Store(s) Available: \nIndian ' + str(rating_avg[94]) + '⭐\nI hope I helped you!!!')
        }
    },
    'Give my Review': {
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
