import sys
import telepot
import googlemaps
import time
import math
from telepot.loop import MessageLoop
from food_func import Welcome_Keyboard, Halal_Preference_Keyboard, Halal2_Preference_Keyboard, Halal14_Preference_Keyboard, Halal16_Preference_Keyboard, HalalNS_Preference_Keyboard, HalalSS_Preference_Keyboard, HalalNH_Preference_Keyboard, HalalNIE_Preference_Keyboard, No_Preference_Keyboard, No1_Preference_Keyboard, No2_Preference_Keyboard, No4_Preference_Keyboard, No9_Preference_Keyboard, No11_Preference_Keyboard, No13_Preference_Keyboard, No14_Preference_Keyboard, No16_Preference_Keyboard, NoNH_Preference_Keyboard, NoNS_Preference_Keyboard, NoSS_Preference_Keyboard, NoNIE_Preference_Keyboard, Vegetarian_Preference_Keyboard, Food_Preference_Keyboard, Nearest_Canteen
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton
from distance_matrix_gmaps import GetAllDistance_Canteen

#start message
gmaps = googlemaps.Client(key='AIzaSyChyx38fw6qtO12-FC99wEyK3u9gcgcXj8')
canfood=['canteen 1','canteen 2','canteen 4','canteen 9','canteen 11','canteen 13','canteen 14','canteen 16','north hill canteen','north spine canteen','south spine canteen','nie canteen']

def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type =='text':        
                #==================food preferences replies=======
                if msg['text'] == 'Halal Preference':
                        #================== This means its a Halal reply ============
                        #==================
                        # 1. Choose canteen
                        # 2. Food type
                        print("I prefer Halal lol")
                        bot.sendMessage(chat_id, 'Which canteen would you like to go to?', reply_markup = Halal_Preference_Keyboard())

                elif msg['text'] == 'No Preference':
                        #================== No halal preference ============
                        #================== Same as above ==================
                        print("I don't care haha")
                        bot.sendMessage(chat_id, 'Which canteen would you like to go to?', reply_markup = No_Preference_Keyboard())

                elif msg['text'] == 'Vegetarian Preference':
			#============== I prefer Vegeterian ================
			#================== Same as above ==================
                        print("I'm a Vegetarian")
                        bot.sendMessage(chat_id, 'Which canteen would you like to go to?', reply_markup = Vegetarian_Preference_Keyboard())


                #=================sub branching for food preference ...======
                elif '(H)' in msg['text'] :
                        #================= canteen preferences.....==========
                        if 'Canteen 2' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nAyam Penyet ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal2_Preference_Keyboard())

                        if 'Canteen 14' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMuslim Malay ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal14_Preference_Keyboard())

                        if 'Canteen 16' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Food ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal16_Preference_Keyboard())

                        if 'North Hill Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nChicken Rice ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNH_Preference_Keyboard())

                        if 'North Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian Food ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMalay BBQ ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine ⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNS_Preference_Keyboard())

                        if 'South Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nBan Mian Fish Soup ⭐⭐⭐⭐\nYong Tau Foo ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalSS_Preference_Keyboard())

                        if 'NIE Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Food ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang ⭐⭐\nMuslim Food ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNIE_Preference_Keyboard())


                #================== same as above=====================
                elif '(V)' in msg['text'] :
                        print('vegetarian food')
                        #================= canteen preferences.....==========
                        if 'North Spine Canteen' in msg['text']:
                                print('NORTH SPINEZ')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian Food ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                        elif 'South Spine Canteen' in msg['text']:
                                print('SOUTH SPINEZ')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                        elif 'NIE Canteen' in msg['text']:
                                print('NIE')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
			#================== if canteen preference not determined ==================
                        else:
                                print("I'm a fuckin Vegetarian")
                                bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Vegetarian_Preference_Keyboard())

                #=================sub branching for food preference ...======
                elif '(N)' in msg['text'] :
                        #================= canteen preferences.....==========
                        if 'Canteen 1' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMenya Takashi ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMala Talk ⭐⭐⭐\nHandmade Noodle ⭐⭐\nBraised Rice And Noodle ⭐⭐⭐\nChinese Cuisine ⭐⭐⭐⭐\nEconomical Rice ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No1_Preference_Keyboard())

                        if 'Canteen 2' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Korean' in msg['text']:
                                        print('GIMME THE Korean FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nKorean Cuisine ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nChicken Rice ⭐⭐⭐\nXiao Long Bao ⭐⭐⭐⭐\nYong Tau Foo ⭐⭐\nSichuan Cuisine ⭐⭐⭐⭐\nShandong Big Bao ⭐⭐\nEconomical Rice ⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nKath’s Bakery ⭐⭐⭐\nThe Oven ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nAyam Penyet ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No2_Preference_Keyboard())

                        if 'Canteen 4' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nZi Char / Fried Rice ⭐⭐⭐⭐⭐\nLa Mian ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No4_Preference_Keyboard())

                        if 'Canteen 9' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJiu Li Xiang Chuan Cai ⭐\nChinese Cuisine ⭐⭐⭐⭐⭐\nXian Noodles ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No9_Preference_Keyboard())

                        if 'Canteen 11' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Korean' in msg['text']:
                                        print('GIMME THE Korean FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nKorean Food ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \n7 Fukijin Japanese Food ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMixed Veg Rice ⭐\nSi Chuan Mei Shi ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWaffles & Pastries ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Food ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No11_Preference_Keyboard())

                        if 'Canteen 13' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Korean' in msg['text']:
                                        print('GIMME THE Korean FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nKorean Cuisine ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJapanese Cuisine ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNoodle Delight ⭐⭐⭐⭐\nChinese Cuisine ⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Food ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No13_Preference_Keyboard())

                        if 'Canteen 14' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nTaiwan ⭐⭐⭐\nSi Chuan ⭐⭐\nAsian Food Delights ⭐⭐\nBan Mian-Fish Soup ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMuslim Malay ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No14_Preference_Keyboard())

                        if 'Canteen 16' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJapanese Food ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nChinese Ramen ⭐⭐⭐\nSignature Dishes With Rice ⭐⭐\nMala Hot Pot ⭐⭐\nEconomical Rice ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Food ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = No16_Preference_Keyboard())

                        if 'North Hill Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMixed Veg Rice ⭐⭐⭐\nTraditional Dough Fritters And Miniwok ⭐⭐⭐\nTraditional Handmade Fish Ball Noodle ⭐⭐⭐\nChicken Rice ⭐⭐\nAh Boon’s Fish Soup ⭐⭐⭐\nClaypot & Porridge ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Cuisine ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = NoNH_Preference_Keyboard())

                        if 'North Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Korean' in msg['text']:
                                        print('GIMME THE Korean FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJapanese Korean Delight ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJapanese Korean Delight ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMini Wok ⭐⭐⭐\nYong Tau Foo ⭐⭐⭐⭐\nChicken Rice ⭐⭐⭐\nHand-Made Noodles ⭐⭐⭐\nMixed Rice ⭐⭐\nCantonese Roast Duck ⭐⭐⭐⭐\nSoup Delight ⭐⭐⭐⭐⭐\nVegetarian Food ⭐⭐\nTaiwanese Cuisine ⭐⭐⭐⭐\nXian Cuisine ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
        
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Food ⭐⭐⭐\nBBQ Delight ⭐⭐\nItalian Pasta ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMalay BBQ ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine ⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Vietnamese' in msg['text']:
                                        print('GIMME THE Vietnamese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVietnamese Cuisine ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = NoNS_Preference_Keyboard())

                        if 'South Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Japanese' in msg['text']:
                                        print('GIMME THE Japanese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nJapanese Cuisine ⭐⭐⭐\nSalad And Bento Express ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian ⭐⭐⭐⭐⭐\nMixed Veg Rice ⭐⭐⭐⭐\nDim Sum ⭐⭐⭐\nChinese Cuisine ⭐⭐⭐⭐\nBan Mian Fish Soup ⭐⭐⭐⭐\nYong Tau Foo ⭐⭐⭐\nChicken Rice ⭐⭐⭐\nKoka Mee Express ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nPasta Express ⭐⭐⭐⭐\nSalad And Bento Express ⭐⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = NoSS_Preference_Keyboard())

                        if 'NIE Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian ⭐⭐⭐⭐\nChicken Rice ⭐⭐⭐⭐⭐\nBan Mian & Fish Soup ⭐⭐⭐\nNoodle ⭐⭐⭐⭐\nA-La-Carte ⭐⭐\nChinese Food ⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nSandwiches & Salad Bar ⭐⭐⭐⭐⭐\nWestern Food ⭐⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())

                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang ⭐⭐\nMuslim Food ⭐⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian ⭐⭐\nI hope I helped you!!!',reply_markup = Welcome_Keyboard())
                                                                                                        
                                        #================= if type of food not determined ===============
                        else:
                                        bot.sendMessage(chat_id, 'What type of food would you like to eat?', reply_markup = NoNIE_Preference_Keyboard())
                                        

                #================== welcome message====================
                else :
                        bot.sendMessage(chat_id, 'Welcome to NTU Food Bot!\nFood decisions are very personal,\nso I will only work in private chats!!\nWhat can I do for you?', reply_markup = Welcome_Keyboard())
                        
        #=============== determine nearest canteen and let user decide ======
        elif content_type == 'location':
                print("Do location stuff here")
                x = msg['location']['latitude']
                y = msg['location']['longitude']
                origins = [[x,y]]
                destinations = ['ntu canteen 1', 'ntu food court 2', 'ntu canteen 4', 'ntu canteen 9', 'ntu canteen 11', 'ntu food court 13', '34 Nanyang Cres, Singapore 637634', '50 Nanyang Walk, Singapore 637658', '636959, 64 Nanyang Cres', 'ntu food court north spine', 'ntu koufu south spine', 'ntu nie canteen']
                n = Nearest_Canteen(x,y)
                print(n)
                listz = (GetAllDistance_Canteen(origins,destinations))
                distance_timetowalk=listz[n]
                print(distance_timetowalk[0])
                bot.sendMessage(chat_id, 'The nearest food location is '+canfood[n]+'.\nIt is approximately '+distance_timetowalk[0]+' away\nWhich is about '+distance_timetowalk[1]+' if you walk. \nPlease choose your food preference', reply_markup = Food_Preference_Keyboard())
                

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)

#let it auto receive msg
MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
