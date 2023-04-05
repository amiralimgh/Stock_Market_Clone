from .User import User
from .Bank import Bank
from .Stock import Stock
from werkzeug.security import check_password_hash
from . import create_app

#User class
#test user init
def test_new_user():
    #Assertion 1 correct check if user init working with given vals
    #Outcome true, user object created
    user = User("kikikoko@gmail.com", "NicoleKidman123", "Kiki", "Kardashian")
    assert user.email != "cool@yahoo.com"
    assert user.email == "kikikoko@gmail.com"
    assert user.password != "NicoleKidman123"
    assert user.first_name == "Kiki"
    assert user.last_name != "Kardashians"

    #Assertion 2 correct check if user init working with given vals
    #Outcome true, user object created
    user2 = User("cool@yahoo.com", "Manchester@1234", "Daniel", "Ghofli")
    assert user2.email == "cool@yahoo.com"
    assert check_password_hash(user2.password, "Manchester@1234")
    assert user2.first_name == "Daniel"
    assert user2.last_name != "Saati"

    #Assertion 3 correct check if user init working with given vals
    #Outcome true, user object created
    user3 = User("amirali.malekghasemi@torontomu.ca",
                 "Barcelona1234", "Kiki", "Smith")
    assert user3.email == "amirali.malekghasemi@torontomu.ca"
    assert not check_password_hash(user3.password, "Barcelona12345")
    assert user3.first_name != "Koko"
    assert user3.last_name == "Smith"

#Stock class
#test stock init
def test_new_stock():
    #Assertion 1 correct check if stock init working with given vals
    #Outcome true, stock object created
    stock = Stock("Google", 2800, 600, 2900, 2700, 2750, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280,
                  281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280])
    assert stock.name == "Google"
    assert stock.price == 2800
    assert stock.volume != 590
    assert stock.high == 2900
    assert stock.low != 2777
    assert stock.open == 2750
    assert stock.price_30_days != [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281, 289,
                                   273, 270, 274, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]

    #Assertion 2 correct check if stock init working with given vals
    #Outcome true, stock object created
    stock2 = Stock("Visa", 220, 2500, 230, 210, 215, [235, 215, 235, 214, 232, 206, 224, 231, 231, 222,
                   213, 235, 211, 220, 225, 209, 213, 215, 227, 223, 226, 217, 229, 231, 233, 213, 233, 235, 209, 219])
    assert stock2.name != "Voodoo"
    assert stock2.price != 2800
    assert stock2.volume == 2500
    assert stock2.high != 2900
    assert stock2.low == 210
    assert stock2.open != 216
    assert stock2.price_30_days == [235, 215, 235, 214, 232, 206, 224, 231, 231, 222, 213, 235,
                                    211, 220, 225, 209, 213, 215, 227, 223, 226, 217, 229, 231, 233, 213, 233, 235, 209, 219]

    #Assertion 3 correct check if stock init working with given vals
    #Outcome true, stock object created
    stock3 = Stock("Oracle", 80, 7000, 90, 70, 75, [
                   86, 72, 81, 77, 72, 76, 86, 84, 81, 72, 79, 87, 79, 73, 85, 82, 73, 82, 78, 78, 86, 88, 82, 85, 78, 76, 87, 88, 78, 78])
    assert stock3.name == "Oracle"
    assert stock3.price == 80
    assert stock3.volume == 7000
    assert stock3.high == 90
    assert stock3.low == 70
    assert stock3.open == 75
    assert stock3.price_30_days == [86, 72, 81, 77, 72, 76, 86, 84, 81, 72, 79,
                                    87, 79, 73, 85, 82, 73, 82, 78, 78, 86, 88, 82, 85, 78, 76, 87, 88, 78, 78]


def test_volume_down():
    stock = Stock("Google", 2800, 600, 2900, 2700, 2750, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280,
                  281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280])
    #Assertion 1 correct check if volume decreased by 10
    #Outcome true, stock decreased by 10 now equals 590
    assert stock.volume_down(10) == 590
    #Assertion 2 correct check if volume decreased by 30
    #Outcome false, stock decreased by 10 now equals 560 not 550
    assert stock.volume_down(30) != 550
    #Assertion 3 correct check if volume decreased by 60
    #Outcome true, stock decreased by 60 now equals 500
    assert stock.volume_down(60) == 500
    #Assertion 4 correct check if volume decreased by 55
    #Outcome true, stock decreased by 55 now equals 445
    assert stock.volume_down(55) == 445
    #Assertion 5 correct check if volume decreased by 45
    #Outcome true, stock decreased by 45 now equals 400
    assert stock.volume_down(45) == 400
    #Assertion 6 correct check if volume decreased by 10
    #Outcome false, stock decreased by 10 now equals 390 not 300
    assert stock.volume_down(10) != 300

#Stock class
#test volume_up()
def test_stock_volume_up():
    stock = Stock("Google", 2800, 600, 2900, 2700, 2750, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280])
    #Assertion 1 correct check if volume increased by 30
    #Outcome true, stock increased by 10 now equals 610
    assert stock.volume_up(10) == 610
    #Assertion 2 correct check if volume increased by 30
    #Outcome false, stock increased by 30 now equals 640 not 443440
    assert stock.volume_up(30) != 443440
    #Assertion 3 correct check if volume increased by 30
    #Outcome true, stock increased by 60 now equals 700
    assert stock.volume_up(60) == 700
    #Assertion 4 correct check if volume increased by 0
    #Outcome true, stock increased by 0 still equals 700
    assert stock.volume_up(0) == 700
    #Assertion 5 correct check if volume increased by 300
    #Outcome true, stock increased by 300 now equals 1000
    assert stock.volume_up(300) == 1000
    #Assertion 6 correct check if volume increased by 19
    #Outcome true, stock increased by 19 now equals 1019
    assert stock.volume_up(19) == 1019

#bank class
#test Bank init
def test_new_bank():
    #Assertion 1 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank = Bank("6022545578941324", "01/25", "654")
    assert bank.card_number == "6022545578941324"
    assert bank.exp_date == "01/25"
    assert bank.cvc == "654"

    #Assertion 2 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank2 = Bank("6233541589471234", "01/24", "999")
    assert bank2.card_number != "6022545578941324"
    assert bank2.exp_date != "01/25"
    assert bank2.cvc != "654"

    #Assertion 3 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank3 = Bank("6055541512344321", "12/26", "987")
    assert bank3.card_number == "6055541512344321"
    assert bank3.exp_date != "01/25"
    assert bank3.cvc == "987"
    
    #Assertion 4 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank4 = Bank("1234567812345678", "06/23", "657")
    assert bank4.card_number == "1234567812345678"
    assert bank4.card_number != " "
    assert bank4.exp_date == "06/23"
    assert bank4.exp_date != True
    assert bank4.cvc == "657"
    assert bank4.cvc != "65890092383"

    #Assertion 5 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank5 = Bank("1231231231231231", "08/34", "929")
    assert bank5.card_number == "1231231231231231"
    assert bank5.card_number != " "
    assert bank5.exp_date == "08/34"
    assert bank5.exp_date != True
    assert bank5.cvc == "929"
    assert bank5.cvc != "65890092383"

    #Assertion 6 correct check if bank init working with given vals
    #Outcome true, bank object created
    bank6 = Bank("0987654321098765", "0/90", "972")
    assert bank6.card_number == "0987654321098765"
    assert bank6.card_number != "                 "
    assert bank6.exp_date == "0/90"
    assert bank6.exp_date != False
    assert bank6.cvc == "972"
    assert bank6.cvc != "   "

#Stock class
#test sameStock()
def test_same_stock():
    stock1 = Stock("Coca-Cola",55 ,5000 ,65 ,45 ,50, [56, 47, 63, 56, 62, 48, 48, 49, 55, 55, 60, 62, 50, 53, 49, 53, 62, 55, 51, 52, 48, 49, 47, 49, 63, 51, 57, 51, 57, 56])
    stock2 = Stock("PepsiCo",150 ,4500 ,160 ,140 ,145, [132, 164, 135, 142, 160, 166, 140, 145, 134, 158, 135, 145, 149, 147, 145, 168, 149, 139, 141, 159, 148, 148, 166, 158, 144, 163, 143, 155, 168, 141])

    #Assertion 1 incorrect check if stock 1 equals stock 2
    #Outcome false, stocks not equal
    assert stock1.sameStock(stock2.name) == False
    #Assertion 2 incorrect check if stock 2 equals stock 1
    #Outcome false, stocks not equal
    assert stock2.sameStock(stock1.name) ==  False
    #Assertion 3 correct check if stock 1 name equal Coca-Cola
    #Outcome true, stock names equal
    assert stock1.sameStock("Coca-Cola") == True
    #Assertion 4 correct check if stock 2 name equal PepsiCo
    #Outcome true, stock names equal
    assert stock2.sameStock("PepsiCo") == True
    #Assertion 5 incorrect check if stock 1 name  = " "
    #Outcome false, stock1 not equal " "
    assert stock1.sameStock(" ") == False
    #Assertion 6 incorrect check if stock 2 name  = ""
    #Outcome false, stock2 not equal ""
    assert stock2.sameStock("") == False
    #Assertion 7 incorrect check if stock 2 name  is int
    #Outcome false, stock2 name not an int
    assert stock2.sameStock(1829292) == False

#init for global user, stock and bank objects to be uses in further testing
global_user = User("Mandar@gmail.com", "406Project123", "Amir", "Smith")
stocks = [
    Stock("Apple", 150, 1000, 160, 140, 145, [150, 143, 148, 151, 159, 152, 149, 146, 157, 146, 160,
          150, 160, 140, 156, 141, 153, 160, 154, 158, 149, 144, 141, 156, 142, 143, 154, 159, 144, 160]),
    Stock("Microsoft", 280, 2000, 290, 270, 275, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281,
          289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
    Stock("Amazon", 3300, 500, 3400, 3200, 3250, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281,
          289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
    Stock("Google", 2800, 600, 2900, 2700, 2750, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281,
          289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
    Stock("Facebook", 340, 1500, 350, 330, 335, [342, 328, 338, 346, 336, 341, 338, 346, 347, 347, 338,
          346, 354, 344, 331, 348, 338, 340, 352, 337, 352, 339, 332, 335, 335, 337, 347, 338, 328, 329]),
    Stock("Tesla", 800, 800, 810, 790, 795, [802, 788, 807, 807, 802, 807, 812, 789, 805, 791, 793,
          791, 815, 814, 806, 807, 806, 785, 810, 794, 795, 807, 788, 787, 803, 786, 791, 788, 788, 795]),
    Stock("NVIDIA", 220, 1200, 230, 210, 215, [211, 233, 214, 223, 228, 235, 207, 233, 219, 228, 222,
          233, 226, 224, 230, 223, 209, 210, 227, 211, 213, 215, 212, 217, 223, 223, 234, 216, 207, 221]),
]
bank = Bank("6022545578941324", "01/25", "654")
bank2 = Bank("6233541589471234", "01/24", "999")


#User class
#test add_bank() and add_funds()
def test_add_funds_and_bank():
    app = create_app()
    with app.app_context():
        #adds bank object to user
        global_user.add_bank(bank)
        #Assertion 1 correct 1000000 added with card 6022545578941324
        #Outcome true, 1000000 add to user budget
        assert global_user.add_funds(1000000, "6022545578941324") == True
        assert global_user.budget == 1000000
        #Assertion 2 incorrect empty card value
        #Outcome false, user budget unchanged
        assert global_user.add_funds(1000000, " ") == False
        assert global_user.budget == 1000000
        #adds bank2 object to user
        global_user.add_bank(bank2)
        #Assertion 3 correct 220 added with card 6233541589471234
        #Outcome true, 220 addded to user budget
        assert global_user.add_funds(220, "6233541589471234") == True
        assert global_user.budget == 1000220
        #Assertion 4 incorrect invalid card value
        #Outcome false, user budget unchanged
        assert global_user.add_funds(1000, "737373737373733") == False
        assert global_user.budget == 1000220
        #Assertion 5 correct 0 added with card 6022545578941324
        #Outcome true, 0 addded to user budget
        assert global_user.add_funds(0, "6022545578941324") == True
        assert global_user.budget == 1000220
        #Assertion 6 correct 11 added with card 6022545578941324
        #Outcome true, 11 addded to user budget
        assert global_user.add_funds(11, "6022545578941324") == True
        assert global_user.budget == 1000231


#User class
#test buy_stocks()
def test_buy_stocks():
    app = create_app()
    with app.app_context():
        #Assertion 1 correct 10 of stock 3 bought
        #Outcome true, 10 of stock 3 added to user stock list
        assert global_user.buy_stocks(stocks[3], 10) == True
        assert global_user.stocks == [{'name': 'Google', 'quantity': 10}]
        #Assertion 2 incorrect 10000 stock 3 price greater then budget
        #Outcome false, user stock list unchanged
        assert global_user.buy_stocks(stocks[3], 10000) == False
        assert global_user.stocks == [{'name': 'Google', 'quantity': 10}]
        #Assertion 3 incorrect 1201 stock 6 price greater then budget
        #Outcome false, user stock list unchanged
        assert global_user.buy_stocks(stocks[-1], 1201) == False
        assert global_user.stocks == [{'name': 'Google', 'quantity': 10}]
        #Assertion 4 correct 25 of stock 4 bought
        #Outcome true, 25 of stock 4 added to user stock list
        assert global_user.buy_stocks(stocks[4], 25) == True
        assert global_user.stocks == [{'name': 'Google', 'quantity': 10}, {'name': 'Facebook', 'quantity': 25}]
        #Assertion 5 correct 12 of stock 2 bought
        #Outcome true, 12 of stock 2 added to user stock list
        assert global_user.buy_stocks(stocks[2], 12) == True
        assert global_user.stocks == [{'name': 'Google', 'quantity': 10}, {'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}]
        #Assertion 6 correct 15 of stock 3 bought
        #Outcome true, 15 more  of stock 3 added to user stock list
        assert global_user.buy_stocks(stocks[3], 15) == True
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}, {'name': 'Google', 'quantity': 25}]


#User class
#tests sell_stocks()
def test_sell_stocks():
    app = create_app()
    with app.app_context():
        #Assertion 1 incorrect not enough quantity of stock 3
        #Outcome false, stock list unchanged
        assert global_user.sell_stocks(stocks[3], 30) == False
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}, {'name': 'Google', 'quantity': 25}]
        #Assertion 2 correct sell 20 of stock 3
        #Outcome true, 20 of stock 3 sold
        assert global_user.sell_stocks(stocks[3], 20) == True
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}, {'name': 'Google', 'quantity': 5}]
        #Assertion 3 correct sell 5 of stock 3
        #Outcome true, 5 of stock 3 sold
        assert global_user.sell_stocks(stocks[3], 5) == True
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}]
        #Assertion 4 incorrect stock 6 not owned by user
        #Outcome false, stock list unchanged
        assert global_user.sell_stocks(stocks[6], 5) == False
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 25}, {'name': 'Amazon', 'quantity': 12}]
        #Assertion 5 correct sell 5 of stock 4
        #Outcome true, 5 of stock 4 sold
        assert global_user.sell_stocks(stocks[4], 5) == True
        assert global_user.stocks == [{'name': 'Amazon', 'quantity': 12}, {'name': 'Facebook', 'quantity': 20}]
        #Assertion 6 correct sell 12 of stock 2
        #Outcome true, 12 of stock 2 sold
        assert global_user.sell_stocks(stocks[2], 12) == True
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 20}]
        #Assertion 7 incorrect trying to sell too much of stock 4
        #Outcome false, stock list unchanged
        assert global_user.sell_stocks(stocks[4], 120) == False
        assert global_user.stocks == [{'name': 'Facebook', 'quantity': 20}]


#User class
#tests change_password() 
def test_change_password():
    app = create_app()
    with app.app_context():
        #Assertion 1 incorrect inital password
        #Outcome false, password unchanged
        assert global_user.change_password("NotCorrectOldPass", "SomethingNew1234") == False
        assert check_password_hash(global_user.password, "406Project123")
        #Assertion 2 correct inital password
        #Outcome True, password changed
        assert global_user.change_password("406Project123", "SomethingNew1234") == True
        assert check_password_hash(global_user.password, "SomethingNew1234")
        #Assertion 3 correct inital password, invalid new password
        #Outcome false, password unchanged
        assert global_user.change_password("SomethingNew1234", "gdhue") == False
        assert check_password_hash(global_user.password, "SomethingNew1234")
        #Assertion 4 correct inital password, blank new password
        #Outcome false, password unchanged
        assert global_user.change_password("SomethingNew1234", "") == False
        assert check_password_hash(global_user.password, "SomethingNew1234")
        #Assertion 5 correct inital password, valid new password
        #Outcome True, password changed
        assert global_user.change_password("SomethingNew1234", "123456") == True
        assert check_password_hash(global_user.password, "123456")
        #Assertion 6 incorrect inital password
        #Outcome false, password unchanged
        assert global_user.change_password("gadwygwdgadwgdaygydag", "cps406pass") == False
        assert check_password_hash(global_user.password, "123456")



#User class 
#tests add_watchlist()
def test_add_watchlist():
      app = create_app()
      with app.app_context():
          #Assertion 1 correct add stock 4
          #Outcome true, add to user watch list
          assert global_user.add_watchlist(stocks[4]) == True
          assert global_user.watchlist == [stocks[4]]
          #Assertion 2 correct add stock 0
          #Outcome true, add to user watch list
          assert global_user.add_watchlist(stocks[0]) == True
          assert global_user.watchlist == [stocks[4], stocks[0]]
          #Assertion 3 correct add stock 1
          #Outcome true, add to user watch list
          assert global_user.add_watchlist(stocks[1]) == True
          assert global_user.watchlist == [stocks[4], stocks[0], stocks[1]]
          #Assertion 4 correct add stock 5
          #Outcome true, add to user watch list
          assert global_user.add_watchlist(stocks[5]) == True
          assert global_user.watchlist == [stocks[4], stocks[0], stocks[1], stocks[5]]
          #Assertion 5 incorrect add stock 1, stock 1 already in list
          #Outcome false, watchlist unchanged
          assert global_user.add_watchlist(stocks[1]) == False
          assert global_user.watchlist == [stocks[4], stocks[0], stocks[1], stocks[5]]
          #Assertion 6 incorrect add stock 4, stock 4 already in list
          #Outcome false, watchlist unchanged
          assert global_user.add_watchlist(stocks[4]) == False
          assert global_user.watchlist == [stocks[4], stocks[0], stocks[1], stocks[5]]


#User class 
#tests remove_watchlist()
def test_remove_watchlist():
    app = create_app()
    with app.app_context():
        #Assertion 1 correct remove stock 4
        #Outcome true, removed stock 4 from user watch list
        assert global_user.remove_watchlist(stocks[4]) == True
        assert global_user.watchlist == [stocks[0], stocks[1], stocks[5]]
        #Assertion 2 incorrect remove stock 6
        #Outcome False, list unchanged stock 6 not in watchlist 
        assert global_user.remove_watchlist(stocks[6]) == False
        assert global_user.watchlist == [stocks[0], stocks[1], stocks[5]]
        #Assertion 3 incorrect remove stock 4
        #Outcome False, list unchanged stock 4 not in watchlist 
        assert global_user.remove_watchlist(stocks[4]) == False
        assert global_user.watchlist == [stocks[0], stocks[1], stocks[5]]
        #Assertion 4 correct remove stock 0
        #Outcome true, removed stock 0 from watchlist 
        assert global_user.remove_watchlist(stocks[0]) == True
        assert global_user.watchlist == [stocks[1], stocks[5]]
        #Assertion 5 correct remove stock 5
        #Outcome true, removed stock 5 from watchlist 
        assert global_user.remove_watchlist(stocks[5]) == True
        assert global_user.watchlist == [stocks[1]]
        #Assertion 6 correct remove stock 1
        #Outcome true, removed stock 1 from watchlist 
        assert global_user.remove_watchlist(stocks[1]) == True
        assert global_user.watchlist == []

#User class 
#tests in_watchlist()
def test_in_watchlist():
    app = create_app()
    with app.app_context():
        #Add stocks to watch list to test the function
        assert global_user.add_watchlist(stocks[4]) == True
        assert global_user.add_watchlist(stocks[0]) == True
        assert global_user.add_watchlist(stocks[1]) == True
        assert global_user.add_watchlist(stocks[5]) == True

        #Assertion 1 correct check for stock 1
        #Outcome true, stock 1 in list 
        assert global_user.in_user_watchlist(stocks[1].name) == True
        #Assertion 2 incorrect check for stock 2
        #Outcome false, stock 2 not  in list 
        assert global_user.in_user_watchlist(stocks[2].name) == False
        #Assertion 3 correct check for stock 5
        #Outcome true, stock 5 in list 
        assert global_user.in_user_watchlist(stocks[5].name) == True
        #Assertion 4 correct check for stock 0
        #Outcome true, stock 0 in list 
        assert global_user.in_user_watchlist(stocks[0].name) == True
        #Assertion 5 incorrect check for stock 6
        #Outcome false, stock 2 not  in list 
        assert global_user.in_user_watchlist(stocks[6].name) == False
        #Assertion 6 incorrect check for stock 3
        #Outcome false, stock 3 not  in list 
        assert global_user.in_user_watchlist(stocks[3].name) == False
