import telepot
import googlemaps
import time
from telepot.loop import MessageLoop
from telepot import DelegatorBot
from telepot.delegate import pave_event_space, per_chat_id, create_open
from food_func import menu, Nearest_Canteen, rating_num, rating_div, rating_avg
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from distance_matrix_gmaps import GetAllDistance_Canteen

# start message
gmaps = googlemaps.Client(key='AIzaSyChyx38fw6qtO12-FC99wEyK3u9gcgcXj8')
canfood = ['Canteen 1', 'Canteen 2', 'Canteen 4', 'Canteen 9', 'Canteen 11', 'Canteen 13', 'Canteen 14', 'Canteen 16',
           'North Hill Canteen', 'North Spine Canteen', 'South Spine Canteen', 'NIE Canteen']

choose_first_button = 0
choose_second_button = 1
choose_third_button = 2
list_stalls = 3
review_stall_button = 4
review_give_ratings = 5
review_get_rating = 6

class FoodBot(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(FoodBot, self).__init__(include_callback_query=True, *args, **kwargs)
        self.state = choose_first_button
        self.pref = None
        self.can = None
        self.type = None
        self.stall = None
        self.rating = None
        self.stallkey = None

    def on_chat_message(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        # get available buttons for keyboard
        food_pref = menu.keys()

        # when user wants to find nearest canteen, use Google Maps API to get details to get there
        if content_type == 'location':
            x = msg['location']['latitude']
            y = msg['location']['longitude']
            origins = [[x, y]]
            print(origins)  # print current loc for checking
            destinations = [[1.346628, 103.686028], [1.348363, 103.685482], [1.344189, 103.685439],
                            [1.352270, 103.685298],
                            [1.354908, 103.686477], [1.351721, 103.681082], [1.352692, 103.682108],
                            [1.350299, 103.680914],
                            [1.354395, 103.688173], [1.347029, 103.680254], [1.342459, 103.682427],
                            [1.348746, 103.677614]]
            n = Nearest_Canteen(x, y)
            print(n)  # know what to draw from string
            listz = (GetAllDistance_Canteen(origins, destinations))
            print(listz)  # print whole list for checking
            distance_timetowalk = listz[n]
            print(distance_timetowalk[0])
            menu_response = ('The nearest food location is ' + canfood[n] + '.\nIt is approximately ' + distance_timetowalk[0]
                + ' away\nWhich is about ' + distance_timetowalk[1] + ' if you walk.')
            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                            [KeyboardButton(text=pref)] for pref in food_pref
                            ] + [[KeyboardButton(text='Find Nearest Canteen', request_location=True)]])

            bot.sendMessage(chat_id, menu_response, reply_markup=menu_keyboard)
            bot.sendMessage(chat_id, 'What can I do for you?')  # added this line to get user to choose options again if required

            # move to second state for user to choose options
            self.state = choose_second_button
        else:
            
            try:

                #initial response when bot is started
                if msg['text'] == '/start' or self.state == 0 :# consider /start for resetting bot

                    response = 'Welcome to NTU Food Bot!\nFood decisions are very personal,\nso I will only work in private chats!!'

                    bot.sendMessage(chat_id, response)

                    # prepare custom keyboard
                    choose_first_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                        [KeyboardButton(text = pref)] for pref in food_pref
                    ] + [[KeyboardButton(text = 'Find Nearest Canteen', request_location=True)]])

                    response = 'What can I do for you?'

                    bot.sendMessage(chat_id, response, reply_markup=choose_first_keyboard)

                    # move to next state
                    self.state = choose_second_button

                # to avoid repeating welcome message after bot is started
                elif (self.state > choose_first_button) :

                    msg_text = msg['text']
                    # placeholders for keyboard and response
                    menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                        [KeyboardButton(text = pref)] for pref in food_pref
                    ] + [[KeyboardButton(text = 'Find Nearest Canteen', request_location=True)]])
                    menu_response = ''

                    #separate into different functions when different buttons are selected
                    if (self.state == choose_second_button):

                        #when food preference is chosen
                        if 'Preference' in msg_text:

                            #update context preference for later re-use
                            self.pref = msg_text

                            #load list of canteens for the chosen preference
                            which_canteen = menu[self.pref]

                            #prepare keyboard and response to get user selection of canteen
                            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                                [KeyboardButton(text = canteens)] for canteens in which_canteen.keys()
                            ] + [[KeyboardButton(text = 'Return to main menu')]])

                            menu_response = 'Which canteen?'

                            # move to next state
                            self.state = choose_third_button

                        #when user want to give review about a stall
                        elif 'Give/Check stall rating' in msg_text:

                            #load list of canteens for review
                            which_canteen = menu['Give/Check stall rating']

                            # prepare keyboard and response to get user selection of canteen
                            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                                [KeyboardButton(text=canteens)] for canteens in which_canteen.keys()
                            ] + [[KeyboardButton(text = 'Return to main menu')]])

                            menu_response = 'Which canteen?'

                            # move to next state
                            self.state = review_stall_button

                    #for user to choose what food type they prefer
                    elif (self.state == choose_third_button):

                        if msg_text != 'Return to main menu':

                            # update context canteen for later re-use
                            self.can = msg_text

                            # load list of food types for the chosen canteen
                            what_food_type = menu[self.pref][self.can]

                            # prepare keyboard and response to get user selection of food type
                            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                                [KeyboardButton(text=stalls)] for stalls in what_food_type.keys()
                            ] + [[KeyboardButton(text = 'Return to main menu')]])

                            menu_response = 'What food type?'

                            # move to next state
                            self.state = list_stalls

                        else:

                            menu_response = 'What can I do for you?'

                            self.state = choose_second_button

                    #return list of stalls for the chosen food type
                    elif (self.state == list_stalls):

                        if msg_text != 'Return to main menu':

                            # update context food type for later re-use
                            self.type = msg_text

                            # load list of stalls for the chosen food type
                            menu_response = menu[self.pref][self.can][self.type]

                            # move to second state for user to choose options
                            self.state = choose_second_button

                            bot.sendMessage(chat_id, menu_response, reply_markup=menu_keyboard)
                            bot.sendMessage(chat_id, 'What can I do for you?')  # added this line to get user to choose options again if required
                            return

                        else:

                            menu_response = 'What can I do for you?'

                            self.state = choose_second_button

                    #for user to choose stall
                    elif (self.state == review_stall_button):

                        if msg_text != 'Return to main menu':

                            # update context canteen for later re-use
                            self.can = msg_text

                            # load list of stalls for the chosen canteen
                            which_stall = menu['Give/Check stall rating'][self.can]

                            # prepare keyboard and response to get user selection of stall
                            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                                [KeyboardButton(text=stalls)] for stalls in which_stall.keys()
                            ] + [[KeyboardButton(text = 'Return to main menu')]])

                            menu_response = 'Which stall?'

                            # move to next state
                            self.state = review_give_ratings

                        else:

                            menu_response = 'What can I do for you?'

                            self.state = choose_second_button

                    #for user to enter rating for stall
                    elif (self.state == review_give_ratings):

                        if msg_text != 'Return to main menu':

                            # update context stall for later re-use
                            self.stall = msg_text

                            # obtain the position of the stall in the ratings lists from the dictionary
                            list_pos = menu['Give/Check stall rating'][self.can][self.stall]

                            # prepare keyboard and response to get user rating of stall from 1 to 5
                            menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=[
                                [KeyboardButton(text=rating)] for rating in range(1, 6)
                            ] + [[KeyboardButton(text = 'Return to main menu')]])

                            response = ('The current rating for the stall is ' + str(rating_avg[list_pos]) + '⭐')

                            menu_response = "Please choose your rating for the stall.\nIf you don't want to give a rating, press 'Return to main menu'."

                            bot.sendMessage(chat_id, response)

                            # move to next state
                            self.state = review_get_rating

                            # store position in list
                            self.stallkey = list_pos

                        else:

                            menu_response = 'What can I do for you?'

                            self.state = choose_second_button

                    #for updating user rating to the rating database
                    elif (self.state == review_get_rating):

                        if msg_text != 'Return to main menu':

                            # update context rating for later re-use
                            self.rating = msg_text

                            # update numerator with addition of user rating
                            rating_num[self.stallkey] = rating_num[self.stallkey] + int(self.rating)

                            # update denominator with addition of user rating
                            rating_div[self.stallkey] += 1

                            # obtain new average rating
                            before_rounding = rating_num[self.stallkey] / rating_div[self.stallkey]

                            # round up value of average rating as accuracy required is only 1 decimal place, so round function is adequate
                            rating_avg[self.stallkey] = round(before_rounding, 2)

                            # thank user for their rating
                            menu_response = 'Thank you for your review!'

                            # move to second state for user to choose options
                            self.state = choose_second_button

                            bot.sendMessage(chat_id, menu_response, reply_markup=menu_keyboard)
                            bot.sendMessage(chat_id, 'What can I do for you?')  # added this line to get user to choose options again if required
                            return

                        else:

                            menu_response = 'What can I do for you?'

                            self.state = choose_second_button

                    bot.sendMessage(chat_id, menu_response, reply_markup=menu_keyboard)
                    return
                
            except:# if user use their normal keyboard 
                 print(self.state)
                 bot.sendMessage(chat_id, 'Error, please use the keyboard provided!')
                


TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = DelegatorBot(TOKEN, [
    pave_event_space()
    (per_chat_id(), create_open, FoodBot, timeout=600)
])

# let it auto receive msg
MessageLoop(bot).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
