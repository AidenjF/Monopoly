import random 
import time
# 39 tiles on the board starting at 0
# trade??
# look at deed cards mid game
# check rent
# check parking and distribution of cash
class Tiles:
    def __init__(self,name,cost,rent,special):
        self._name = name
        self._cost = cost
        self._owner = None
        self._rent = rent
        self._special = special
        self._houses = 0
        self._hotels = 0
    def set_owner(self,name):
        self._owner = name
    def get_owner(self):
        return self._owner
    def get_rent(self):
        if self._special == 'railroad':
            return self._rent
        if self._hotels != 0:
            return self._rent[4]
        else:
            return self._rent[self.get_houses()]
    def bought_house(self):
        self._houses += 1
    def get_houses(self):
        return self._houses
    def get_special(self):
        return self._special
    def parking_to_zero(self):
        self._special = 0
    def add_to_parking(self,num):
        self._special += num
    def get_cost(self):
        return self._cost
    def bought_hotel(self):
        self._houses = 0
        self._hotel = 1

class People:
    def __init__(self, name):
        self._name = name
        self._tile_position = 0
        self._money = 1500
        self._jail = []
        self._houses = 0
        self._hotels = 0
        self._utilities = 0
        self._railroads = 0
        self._jail_free_card = 0
        self._properties = {'brown':[],'light blue':[],'pink':[],'orange':[],'red':[],'yellow':[], 'green':[],'dark blue':[]}
    def move(self, dice_number):
        self._tile_position += dice_number
    def set_tile(self, set_number):
        self._tile_position = set_number
    def take_money(self, money):
        self._money -= money
    def give_money(self, money):
        self._money += money
    def get_money(self):
        return self._money
    def get_name(self):
        return self._name
    def get_tile_number(self):
        return self._tile_position
    def check_jail(self):
        return self._jail
    def get_utilities(self):
        return self._utilities
    def get_railroads(self):
        return self._railroads
    def increment_jail_free_card(self):
        self._jail_free_card += 1
    def get_jail_free(self):
        if self._jail_free_card > 0:
            return True
        return False
    def get_houses(self):
        return self._houses
    def get_hotels(self):
        return self._houses
    def get_properties(self):
        return self._properties
    def bought_house(self):
        self._houses += 1
    def bought_hotel(self):
        self._houses -= 4
        self._hotels += 1

# (name,cost,rent,special properties)
tile_0 = Tiles('Go!',None,0,'Go')   #corner
tile_1 = Tiles('Medieranian Avenue', 60,[2,10,30,90,169],None)
tile_2 = Tiles('Community Chest',None,0,'Chest')
tile_3 = Tiles('Baltic Avenue',60,[4,20,60,180,320],None)
tile_4 = Tiles('Income Tax', None,0,'Inc. Tax')
tile_5 = Tiles('Reading Railroad', 200,25,'railroad')
tile_6 = Tiles('Oriental Avenue', 100,[6,30,90,270,400],None)
tile_7 = Tiles('Chance',None,0,'Chance')
tile_8 = Tiles('Vermont Avenue',100,[6,30,90,270,400],None)
tile_9 = Tiles('Connecticut Avenue',120,[8,40,100,300,450],None)
tile_10 = Tiles('Jail',None,0,'Visit')      #corner 5
tile_11 = Tiles('St.Charles Place', 140,[10,50,150,450,625],None)
tile_12 = Tiles('Electric Company',150,0,'utility')
tile_13 = Tiles('States Avenue',140,[10,50,150,450,625],None)
tile_14 = Tiles('Virginia Avenue',160,[12,60,180,500,700],None)
tile_15 = Tiles('Pennsylvania Railroad',200,25,'railroad')
tile_16 = Tiles('St.James Place', 180,[14,70,200,550,750],None)
tile_17 = Tiles('Community Chest',None,24,'Chest')
tile_18 = Tiles('Tennesse Avenue',180,[14,70,200,550,750],None)
tile_19 = Tiles('New York Avenue', 200,[16,80,220,600,800],None)
tile_20 = Tiles('Free Parking',None,0,0)    #corner
tile_21 = Tiles('Kentucky Avenue',220,[18,90,250,700,875],None)
tile_22 = Tiles('Chance',None,30,'Chance')
tile_23 = Tiles('Indiana Avenue',220,[18,90,250,700,875],None)
tile_24 = Tiles('Illinois Avenue',240,[20,100,300,750,925],None)
tile_25 = Tiles('B.&.O. Railroad',200,25,'railroad')
tile_26 = Tiles('Atlantic Avenue',260,[22,110,330,800,975],None)
tile_27 = Tiles('Ventnor Avenue',260,[22,110,330,800,975],None)
tile_28 = Tiles('Water Works',150,0,'utility')
tile_29 = Tiles('Marvin Gardens',280,[24,120,360,850,1025],None)
tile_30 = Tiles('Go to Jail!',None,0,'Jail')    #corner
tile_31 = Tiles('Pacific Avenue',300,[26,130,390,900,1100],None)
tile_32 = Tiles('North Carolina Avenue',300,[26,130,390,900,1100],None)
tile_33 = Tiles('Community Chest',None,0,'Chest')
tile_34 = Tiles('Pennsylvania Avenue',320,[28,150,450,1000,1200],None)
tile_35 = Tiles('Short Line',200,25,'railroad')
tile_36 = Tiles('Chance',None,0,'Chance')
tile_37 = Tiles('Park Place',350,[35,175,500,1100,1300],None)
tile_38 = Tiles('Luxury Tax',None,35,'Lux. Tax')
tile_39 = Tiles('Boardwalk',400,[50,200,600,1400,1700],None)

PROPERTIES = {'brown':[tile_1,tile_3],
'light blue':[tile_6,tile_8,tile_9],
'pink':[tile_11,tile_13,tile_14],
'orange':[tile_16,tile_18,tile_19],
'red':[tile_21,tile_23,tile_24],
'yellow':[tile_26,tile_27,tile_29],
'green':[tile_31,tile_32,tile_34],
'dark blue':[tile_37,tile_39]}

BOARD = [tile_0,tile_1,tile_2,tile_3,tile_4,tile_5,tile_6,tile_7,tile_8,tile_9,tile_10,tile_11,tile_12,tile_13,tile_14,tile_15,
tile_16,tile_17,tile_18,tile_19,tile_20,tile_21,tile_22,tile_23,tile_24,tile_25,tile_26,tile_27,tile_28,tile_29,tile_30,tile_31,
tile_32,tile_33,tile_34,tile_35,tile_36,tile_37,tile_38,tile_39]

CHANCE = {1:['Advance to Boardwalk',['turn.set_tile(39)']],
2:['Advance to Go (Collect $200)', ['turn.set_tile(0)','turn.give_money(200)']],
3:['Advance to Illinois Avenue. If you pass Go, collect $200', ['advance_to_illinois(turn,other)']],
4:['Advance to St. Charles Place. If you pass Go, collect $200',['advance_to_stcharles(turn,other)']],
5:['Advance to the nearest Railroad. If unowned, you may buy it. If owned, pay owner twice the rent',['travel_to_nearest_railroad(turn,other)']],
6:['Advance token to nearest Utility. If unowned, you may buy it. If owned, throw dice and pay owner a total ten times amount thrown.',['travel_to_nearest_utility(turn,other)']],
7:['Bank pays you dividend of $50',['turn.give_money(50)']],
8:['Get Out of Jail Free',['turn.increment_jail_free_card()']], 
9:['Go Back 3 Spaces',['go_back_three(turn,other,die_total,one,two)']],  #check
10:['Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',['turn.set_tile(30)']],
11:['Make general repairs on all your property. For each house pay $25. For each hotel pay $100',['turn.take_money(25*turn.get_houses())','turn.take_money(100*turn.get_hotels())']], ####
12:['Speeding fine $15', ['turn.take_money(15)']],
13:['Take a trip to Reading Railroad. If you pass Go, collect $200',['advance_to_reading(turn,other)']],
14:['You have been elected Chairman of the Board. Recieve $50', ['turn.give_money(50)']],
15:['Your building loan matures. Collect $150',['turn.give_money(150)']]}

CHEST = {1:['Advance to Go',['turn.give_money(200)','turn.set_tile(0)']],
2:['Bank error in your favor. Collect $200',['turn.give_money(200)']],
3:["Doctor's fee. Pay $50",['turn.take_money(50)']],
4:['From sale of stock you get $50',['turn.take_money(50)']],
5:['Get Out of Jail Free',['turn.increment_jail_free_card()']], 
6:['Go to Jail. Go directly to jail, do not pass Go, do not collect $200',['turn.set_tile(10)','one._jail.append(1)','one._jail.append(1)']],
7:['Holiday fund matures. Receive $100',['turn.give_money(100)']],
8:['Income tax refund. Collect $20',['turn.give_money(20)']],
9:['It is your birthday. Collect $10 from every player',['other.take_money(10)','turn.give_money(10)']],
10:['Life insurance matures. Collect $100',['turn.give_money(100)']],
11:['Pay hospital fees of $100',['turn.take_money(100)']],
12:['Pay school fees of $50',['turn.take_money(50)']],
13:['Receive $25 consultancy fee',['turn.take_money(50)']],
14:['You are assessed for street repair. $40 per house. $115 per hotel',['turn.take_money(40*turn.get_houses())','turn.take_money(115*turn.get_hotels())']],
15:['You have won second prize in a beauty contest. Collect $10',['turn.give_money(10)']],
16:['You inherit $100',['turn.give_money(100)']]}

def main():
    #create the players
    one,two = create_players()
    one = People(one)
    two = People(two)
    print('\nRULES:')
    print('*** If you miss spell any of the options given your turn will be skipped and you will not be able to continue ***')
    print('*** If you land on income tax, or luxury tax after pulling a chance card you loose the ability to buy houses or hotels during the same turn ***')
    time.sleep(4)
    print('\nBoth Players Start off with $1500 and will start at Go!\n'
          'Player One Will Start First')
    time.sleep(1)
    #proccess a command
    turn = one
    commands(turn,one,two)
    print('Game Over')

def commands(turn,one,two):
    if turn == one:
        other = two
    else:
        other = one
    end_game_check(turn,other)
    if turn.check_jail() == []:
        start_of_turn(turn)
        input(f"\nClick enter to roll the dice!")
        print('ROLLING!')
        time.sleep(2)
        die_1,die_2,die_total = dice_roll()
        turn.move(die_total)
        # check to see if they pass go
        if turn.get_tile_number() >= 40:
            turn.set_tile(turn.get_tile_number() - 40)
            turn.give_money(200)
        print(f'You landed on {BOARD[turn.get_tile_number()]._name}')
        time.sleep(1)
        # check if the tile is a special tile or not to see if you can buy it ot not
        # check to see if the tile is owned or not
        tile_check,jail = check_tile(turn,other,die_total,one,two)
        if not tile_check:     #----------------------
            check_owner(turn,other,die_total)
        next = False
        while not next:
            command = input(f'Would you like to buy any houses or hotels before you end your turn? (house,hotel, or end) ')
            end_turn_commands(command,turn)
            if command == 'end':
                next = True
        # if you are in jail you cant roll again
        if jail:
            if turn == one:
                commands(two,one,two)
            else:
                commands(one,one,two)
        # if you are not in jail you can roll again:
        else:
            if die_1 == die_2:
                commands(turn,one,two)
            else:
                next_turn(turn,one,two)
        return
    else:
        # if they are in jail then run this function
        player_in_jail(turn,one,two,other)
    # change who has the next turn
    next_turn(turn,one,two)

def end_turn_commands(command,turn):
    # ask if they would like to buy a house or hotel
    player_properties = turn.get_properties()
    # if command is end then they turn will be done
    if command == 'end':
        return
    # if the command is house check if there are any property groups they can buy from
    elif command == 'house':
        # first check if there are any they can buy from
        allowed_to_buy_houses = {}
        # append the properties they can buy houses for
        for color in player_properties:
            if len(player_properties[color]) == len(PROPERTIES[color]):
                allowed_to_buy_houses[color] = []
                for properties in PROPERTIES[color]:
                    allowed_to_buy_houses[color].append(properties)
        if allowed_to_buy_houses == {}:
            print('You can not buy any houses for your property sets.')
            return
        print('You can buy houses for the property colors of:')
        for colors in allowed_to_buy_houses:
            print(f'- {colors} -')
            i = 0
            for properties in allowed_to_buy_houses[colors]:
                print(f'{i}. {properties._name}')
                i += 1
        # ask which one they would like to buy a house for
        color_choice = input('What color would you like to buy a house for? ')
        color_number = input('Which property number would you like to buy out of that chosen color category? ')
        property_name = allowed_to_buy_houses[color_choice][int(color_number)]._name
        property_houses = allowed_to_buy_houses[color_choice][int(color_number)].get_houses()
        # if they dont have any houses the first one cost 50
        if property_houses == 0:
            cost = 50
        else:
            cost = 50 * property_houses
        if property_houses == 4:
            print(f'{property_name} has {property_houses} houses so far, you must buy a hotel now!')
        else:
            print(f'{property_name} has {property_houses} houses so far, you payed ${cost} for the new house.')
            # add the house to the tile
            allowed_to_buy_houses[color_choice][int(color_number)].bought_house()
            turn.take_money(cost)
            # add a house to the player profile
            turn.bought_house()
    # if the command is hotel 
    elif command == 'hotel':
        allowed_to_buy_hotels = []
        for colors in player_properties:
            for tiles in player_properties[colors]:
                if tiles.get_houses() == 4:
                    allowed_to_buy_hotels.append(tiles)
        if allowed_to_buy_hotels == []:
            print()
        if allowed_to_buy_hotels == []:
            print('You can not buy any hotels for your properties.')
            return
        print('You can buy hotels for the following properties:')
        i = 0
        for properties in allowed_to_buy_hotels:
            print(f'{i}. {properties._name}')
            i += 1
        choice = int(input('What property number would you like to purchase a hotel for?'))
        allowed_to_buy_hotels[choice].bought_hotel()
        turn.bought_hotel()
        print(f'You bought a house for {allowed_to_buy_hotels[choice]._name} for $100.')
####################################################################################################

def check_owner(turn,other,die_total):
    if BOARD[turn.get_tile_number()]._owner == turn:
        print('You already own this tile!')
    else:
        if BOARD[turn.get_tile_number()]._owner == None:
            cost = BOARD[turn.get_tile_number()].get_cost()
            buy = input(f'This tile is not owned, would you like to purchase it for ${cost}? (y or n) ')
            if buy == 'y':
                # check to make sure the player has enough money to buy
                if cost <= turn._money:
                    BOARD[turn.get_tile_number()].set_owner(turn)
                    turn.take_money(cost)
                    # check if they have a utility and if they dont then add one and if they do multiply the counter by 10
                    if BOARD[turn.get_tile_number()]._special == 'utility':
                        if turn.get_utilities() == 1:
                            turn._utilities == 10
                        else:
                            turn._utilities += 1
                    elif BOARD[turn.get_tile_number()]._special == 'railroad':
                        turn._railroads += 1
                    adding_to_owned_list(turn)
                else:
                    print(f'You do not have enough money to purchase {BOARD[turn.get_tile_number()]._name}')
            if buy == 'quit':
                quit()
        # if the tile is owned
        elif BOARD[turn.get_tile_number()]._owner != None:
            rent = BOARD[turn.get_tile_number()].get_rent()
            # check if the tile is a utility or not
            if BOARD[turn.get_tile_number()].get_special() == 'utility':
                print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${die_total*4*other.get_utilities()}')
                turn.take_money(BOARD[turn.get_tile_number()].get_rent())
                print(f'{turn.get_name()} = ${turn.get_money()}')
            # check if the tile is a railroad
            elif BOARD[turn.get_tile_number()].get_special() == 'railroad':
                print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${4*other.get_railroads()}')
                turn.take_money(BOARD[turn.get_tile_number()].get_rent())
                print(f'{turn.get_name()} = ${turn.get_money()}')
            # if the tile is not a utility or railroad 
            else:
                print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${rent}')
                turn.take_money(BOARD[turn.get_tile_number()].get_rent())
                other.give_money(BOARD[turn.get_tile_number()].get_rent())
                print(f'{turn.get_name()} = ${turn.get_money()}')

def check_tile(turn,other,die_total,one,two):
    """ Checks the tile to see if is a special case, if it is a special case then it will handle it 
        seperately.
        # other, die_total, one, and two are included so they can be called in the global variables #
    """
    special_property = BOARD[turn.get_tile_number()]._special
    if special_property == 'Jail':
        turn.set_tile(10)
        print(f'• {turn.get_name()} landed on "Go to Jail!", you will not pass go and will not collect $200. •')
        turn._jail.append(1)
        turn._jail.append(1)
        return True, True
    elif special_property == 'Chest':
        card_num = random.randint(1,15)
        print(CHEST[card_num][0])
        for items in CHEST[card_num][1]:
            eval(items)
        print(f'{turn.get_name()} has ${turn.get_money()} now!\n')
        return True, None
    elif special_property == 'Chance':
        card_num = random.randint(1,15)
        print(f'• {CHANCE[card_num][0]} •')
        for items in CHANCE[card_num][1]:
            eval(items)
        print(f'{turn.get_name()} has ${turn.get_money()}.\n')
        return True, None
    elif special_property == 'Lux. Tax':
        turn.take_money(100)
        BOARD[20].add_to_parking(200)
        print(f'• {turn.get_name()} landed on "Luxury Tax", you must pay $200 •')
        print(f'Free parking now holds ${BOARD[20].get_special()}')
        print(f'{turn.get_name()} = ${turn.get_money()}')
        return True, None
    elif special_property == 'Inc. Tax':
        turn.take_money(200)
        BOARD[20].add_to_parking(200)
        print(f'• You landed on "Income Tax" and must pay $200 •')
        print(f'Free parking now holds ${BOARD[20].get_special()}')
        print(f'{turn.get_name()} = ${turn.get_money()}')
        return True, None
    elif type(special_property) == int:
        turn.give_money(BOARD[turn.get_tile_number()].get_special())
        print(f'• {turn.get_name()} has obatined ${BOARD[turn.get_tile_number()]._special} and now has ${turn.get_money()} total •')
        BOARD[turn.get_tile_number()].parking_to_zero()
        print(f'Free parking now holds ${BOARD[20].get_special()}')
        return True, None
    elif special_property == 'Visit':
        print('However just visiting the jail!')
        return True, None
    elif special_property == 'Go':
        return True, None
    else:
        return False, None

def player_in_jail(turn,one,two,other):
    print(f'{turn.get_name()} is still in jail')
    time.sleep(.5)
    if turn.get_jail_free():
        answer = input('You have a get out of Jail Free card, would you like to use it? (y or n)')
        if answer == 'y':
            turn._jail_free_card -= 1
            print('You have escaped jail!')
            while turn._jail != []:
                turn._jail.pop(-1)
            commands(turn,one,two)
    choice = input(f'\nWould {turn.get_name()} like to pay $50 or try and roll a double to get out of jail? (pay or roll) ')
    if choice == 'pay':
        turn.take_money(50)
        while turn._jail != []:
            turn._jail.pop(-1)
        commands(other,one,two)
    elif choice == 'roll':
        die_1,die_2,die_total = dice_roll()
        if die_1 == die_2:
            print('• Congrats you rolled a double and have escaped jail •')
            while turn._jail != []:
                turn._jail.pop(-1)
            commands(other,one,two)
    turn._jail.pop(-1)

def adding_to_owned_list(turn):
    property = BOARD[turn.get_tile_number()]
    for colors, properties in PROPERTIES.items():
        for individual in properties:
            if property._name == individual:
                turn._properties[colors].append(property)

def create_players():
    """ This function creates the people as class objects.
    """
    print('Lets Create the Players!\n')
    print(' ------------------------------- \n'
          '|      Welcome to Monopoly!     |\n'
          ' ------------------------------- \n')

    name_one = input('What is the first characters name?\n')
    name_two = input('What is the second characters name?\n')
    return name_one, name_two

def dice_roll():
    """ This function roll the die and returns the numbers
    """
    die_rolls = [random.randint(1,6),random.randint(1,6)]
    for rolls in die_rolls:
        if rolls == 6:
            print(' -----\n| • • |\n| • • |\n| • • |\n -----\n')
        elif rolls == 5:
            print(' -----\n| • • |\n|  •  |\n| • • |\n -----\n')
        elif rolls == 4:
            print(' -----\n| • • |\n|     |\n| • • |\n -----\n')
        elif rolls == 3:
            print(' -----\n|   • |\n|  •  |\n| •   |\n -----\n')
        elif rolls == 2:
            print(' -----\n| •   |\n|     |\n|   • |\n -----\n')
        elif rolls == 1:
            print(' -----\n|     |\n|  •  |\n|     |\n -----\n')
    die_total = die_rolls[0]+die_rolls[1]
    return die_rolls[0],die_rolls[1],die_total

def next_turn(turn,one,two):
    if turn == one:
        commands(two,one,two)
    else:
        commands(one,one,two)

def start_of_turn(turn):
    """ This function prints a reminder of whos turn it is and how much money
        they have
    """
    turn_txt = f"{turn.get_name()}'s Turn"
    money_txt = f'${turn.get_money()}'
    print(f' \n --------------------')
    print(f'|{turn_txt:^20}|')
    print(f'|{money_txt:^20}|')
    print(f' --------------------')

def travel_to_nearest_utility(turn,other):
    """ This handles the card that travels you to the nearest utility
    """
    # check where the nearest utility is
    if 0 <= turn._tile_position <= 11 or 29 <= turn._tile_position <= 39:
        turn.set_tile(12)
        print('You advanced to the Electric Company!')
    else:
        turn.set_tile(28)
        print('You advanced to Water Works!')
    # check if the other player owns the utility
    if BOARD[turn.get_tile_number()]._owner == other:
        print('You must roll the die and pay the owner 10 times the amount rolled!')
        answer = input('Click enter to continue')
        die_1,die_2,die_total = dice_roll()
        print(f'You will pay {other.get_name()} ${die_total*10}')
        turn.take_money(die_total*10)
        other.give_money(die_total*10)
    # if it is not owned then it can be purchased
    elif BOARD[turn.get_tile_number()]._owner == None:
        answer = input(f'This propery is not owned and would you like to purchase it for ${BOARD[turn.get_tile_number()].get_cost()}? (y or n)')
        if answer == 'y':
            cost = BOARD[turn.get_tile_number()]._cost
            if cost <= turn._money:
                BOARD[turn.get_tile_number()].set_owner(turn)
                turn.take_money(cost)
                if turn.get_utilities() == 1:
                    turn._utilities == 10
            else:
                print(f'You do not have enough money to purchase {BOARD[turn.get_tile_number()]._name}')
    else:
        # if you already own the property
        print('You already own this property!')

def travel_to_nearest_railroad(turn,other):
    """ This handles the card that travels you to the nearest railroad
    """
    # find what railroad is nearest
    if 36 <= turn._tile_position <= 39 or 1 <= turn._tile_position <= 4:
        if turn.tile_position >= 39:
            print('You passed go advancing to Reading Railroad!')
        else:
            print('You advanced to Reading Railroad!')
        turn.give_money(200)
        turn.set_tile(5)
    elif 5 <= turn._tile_position <= 14:
        print('You advanced to Pennsylvania Railroad!')
        turn.set_tile(15)
    elif 15 <= turn._tile_position <= 24:
        print('You advanced to B.&.O. Railroad!')
        turn.set_tile(25)
    else:
        print('You advanced to Short Line!')
        turn.set_tile(35)
    # if it is owned you must pay the owner twice the amount you owe them originally
    if BOARD[turn.get_tile_number()]._owner == other:
            print(f'You must pay rent of {BOARD[turn.get_tile_number()].get_rent()*other.get_railroads()*2}')
    elif BOARD[turn.get_tile_number()]._owner == None:
        answer = input(f'This propery is not owned and would you like to purchase it for ${BOARD[turn.get_tile_number()].get_cost()}? (y or n) ')
        if answer == 'y':
            cost = BOARD[turn.get_tile_number()]._cost
            if cost <= turn._money:
                BOARD[turn.get_tile_number()].set_owner(turn)
                turn.take_money(cost)
                # we know they will land on a railroad so implement it if they buy it
                turn._railroads += 1
                adding_to_owned_list(turn)
            else:
                print(f'You do not have enough money to purchase {BOARD[turn.get_tile_number()]._name}')
    else:
        # if the player already owns the property
        print(f'You already own this property!')

#
#
# special functions must be implemented for the more involving chance cards
def advance_to_stcharles(turn,other):
    if turn.get_tile_number() > 11:
        print('• You passed Go advancing to St.Charles Place! •')
    turn.set_tile(11)
    if BOARD[turn.get_tile_number()]._owner == None:
        answer = input(f'This propery is not owned and would you like to purchase it for ${BOARD[turn.get_tile_number()].get_cost()}? (y or n) ')
        if answer == 'y':
            cost = BOARD[turn.get_tile_number()]._cost
            if cost <= turn._money:
                BOARD[turn.get_tile_number()].set_owner(turn)
                turn.take_money(cost)
    elif BOARD[turn.get_tile_number()]._owner == other:
        rent = BOARD[turn.get_tile_number()].get_rent()
        print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${rent}')
    else:
        print('You already own this tile!')

def advance_to_illinois(turn,other):
    if turn.get_tile_number() > 24:
        print('• You passed Go advancing to Illinois Avenue! •')
    turn.set_tile(24)
    if BOARD[turn.get_tile_number()]._owner == None:
        answer = input(f'This propery is not owned and would you like to purchase it for ${BOARD[turn.get_tile_number()].get_cost()}? (y or n) ')
        if answer == 'y':
            cost = BOARD[turn.get_tile_number()]._cost
            if cost <= turn._money:
                BOARD[turn.get_tile_number()].set_owner(turn)
                turn.take_money(cost)
    elif BOARD[turn.get_tile_number()]._owner == other:
        rent = BOARD[turn.get_tile_number()].get_rent()
        print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${rent}')
    else:
        print('You already own this tile!')

def advance_to_reading(turn,other):
    if turn.get_tile_number() > 5:
        print('• You passed Go advancing to Reading Railroad! •')
    turn.set_tile(5)
    if BOARD[turn.get_tile_number()]._owner == None:
        answer = input(f'This propery is not owned and would you like to purchase it for ${BOARD[turn.get_tile_number()].get_cost()}? (y or n) ')
        if answer == 'y':
            cost = BOARD[turn.get_tile_number()]._cost
            if cost <= turn._money:
                BOARD[turn.get_tile_number()].set_owner(turn)
                turn.take_money(cost)
    elif BOARD[turn.get_tile_number()]._owner == other:
        rent = BOARD[turn.get_tile_number()].get_rent()
        print(f'This tile is owned by {BOARD[turn.get_tile_number()].get_owner().get_name()}, the rent for this tile is ${rent}')
    else:
        print('You already own this tile!')

def go_back_three(turn,other,die_total,one,two):
    turn.set_tile(turn.get_tile_number()-3)
    print(f'• You landed on {BOARD[turn.get_tile_number()]._name}!')
    # check what the new tile is, see if it is tax or a propety
    tile_check,jail = check_tile(turn,other,die_total,one,two)
    # if not a special tile then check the owner
    if not tile_check:
        check_owner(turn,other,die_total)
    next_turn(turn,one,two)

def end_game_check(one,two):
    if one.get_money() < 0:
        print(f'{one.get_name()} has run out of money! They lose!')
    if two.get_money() < 0 :
        print(f'{two.get_name()} has run out of money! They lose!')
    quit
#
#
#
main()