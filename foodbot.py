import time
import sys
import telepot
import math
from telepot.loop import MessageLoop
from food_func import Welcome_Keyboard, Halal_Preference_Keyboard, Halal2_Preference_Keyboard, Halal14_Preference_Keyboard, Halal16_Preference_Keyboard, HalalNS_Preference_Keyboard, HalalSS_Preference_Keyboard, HalalNH_Preference_Keyboard, HalalNIE_Preference_Keyboard, No_Preference_Keyboard, Vegetarian_Preference_Keyboard, Food_Preference_Keyboard, Nearest_Canteen

#start message

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
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Halal_Preference_Keyboard())

                elif msg['text'] == 'No Preference':
                        #================== No halal preference ============
                        #================== Same as above ==================
                        print("I don't care haha")
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = No_Preference_Keyboard())

                elif msg['text'] == 'Vegetarian Preference':
			#============== I prefer Vegeterian ================
			#================== Same as above ==================
                        print("I'm a fuckin Vegetarian")
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Vegetarian_Preference_Keyboard())


                #=================sub branching for food preference ...======
                elif '(H)' in msg['text'] :
                        #================= canteen preferences.....==========
                        if 'Canteen 2' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nAyam Penyet')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal2_Preference_Keyboard())

                        if 'Canteen 14' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMuslim Malay')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal14_Preference_Keyboard())

                        if 'Canteen 16' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Food')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = Halal16_Preference_Keyboard())

                        if 'North Hill Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nChicken Rice')
                                        sys.exit()
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine')
                                        sys.exit()
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang And Indian Cuisine')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNH_Preference_Keyboard())

                        if 'North Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian Food')
                                        sys.exit()
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nMalay BBQ')
                                        sys.exit()
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNS_Preference_Keyboard())

                        if 'South Spine Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nBan Mian Fish Soup \nYong Tau Foo')
                                        sys.exit()
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang')
                                        sys.exit()
                                if 'Indian' in msg['text']:
                                        print('GIMME THE Indian FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nIndian Cuisine')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalSS_Preference_Keyboard())

                        if 'NIE Canteen' in msg['text']:
                                #================= if type of food has been determined... =======
                                if 'Chinese' in msg['text']:
                                        print('GIMME THE Chinese FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nVegetarian')
                                        sys.exit()
                                if 'Western' in msg['text']:
                                        print('GIMME THE Western FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nWestern Food')
                                        sys.exit()
                                if 'Malay' in msg['text']:
                                        print('GIMME THE Malay FOOD REVIEW OH MY GOD')
                                        bot.sendMessage(chat_id, 'Store(s) Available: \nNasi Padang \nMuslim Food')
                                        sys.exit()
                                #================= if type of food not determined ===============
                                else:
                                        bot.sendMessage(chat_id, 'What food type?', reply_markup = HalalNIE_Preference_Keyboard())
                #================== same as above=====================
                elif '(V)' in msg['text'] :
                        print('vegetarian food')
                        #================= canteen preferences.....==========
                        if 'North Spine Canteen' in msg['text']:
                                print('NORTH SPINEZ')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian Food')
                                sys.exit()
                        elif 'South Spine Canteen' in msg['text']:
                                print('SOUTH SPINEZ')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian')
                                sys.exit()
                        elif 'NIE Canteen' in msg['text']:
                                print('NIE')
                                bot.sendMessage(chat_id, 'Stall(s) Available:\nVegetarian')
                                sys.exit()
			#================== if canteen preference not determined ==================
                        else:
                                print("I'm a fuckin Vegetarian")
                                bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Vegetarian_Preference_Keyboard())
                #================== welcome message====================
                else :
                        bot.sendMessage(chat_id, 'Welcome to NTU Food Bot, \nWhat can I do for you?', reply_markup = Welcome_Keyboard())
        #=============== determine nearest canteen and let user decide ======
        elif content_type == 'location':
                print("Do location stuff here")

                n = Nearest_Canteen(msg['location']['latitude'],msg['location']['longitude'])
                print(n)
                
                bot.sendMessage(chat_id, 'The nearest is '+canfood[n]+', do keep that in mind.\nChoose your food preference', reply_markup = Food_Preference_Keyboard())
                

#============================== IF ALL GOES CALL BACK QUERY THIS SHOULD NOT BE RUNNED =======================
def on_callback_query(msg):
        query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, data)

        bot.answerCallbackQuery(query_id, text='Got it, please wait a fuckin moment... ')

        if data =='hl':
                print('yes! halal - looking up the database....')
                bot.sendMessage(from_id, 'No Preference')#, reply_markup = No_Preference_Keyboard())
                #bot.answerCallbackQuery(query_id, 'Whpls let this inline kb work', reply_markup = No_Preference_Keyboard())
                
        if data =='nil':
                print('yes! no pref - looking up the database....')
        if data =='veg':
                print('yes! vegetarian - looking up the database....')

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)

#let it auto receive msg
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
