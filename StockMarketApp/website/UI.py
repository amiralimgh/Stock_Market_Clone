from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .User import User
from .Stock import Stock
from .Bank import Bank
from . import db
import requests
import json

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/ne/news"

headers = {
	"X-RapidAPI-Key": "e33f954bb9mshd0889af383bdd27p1ef7e2jsnadb37b93a8a6",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

news_items = data[-20:]



class UI:
    def __init__(self):
        self.views = Blueprint('views', __name__)
        self.auth = Blueprint('auth', __name__)
           
        self.stocks = [
            Stock("Apple", 150, 1000, 160, 140, 145, [150, 143, 148, 151, 159, 152, 149, 146, 157, 146, 160, 150, 160, 140, 156, 141, 153, 160, 154, 158, 149, 144, 141, 156, 142, 143, 154, 159, 144, 160]),
            Stock("Microsoft", 280, 2000, 290, 270, 275, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
            Stock("Amazon", 3300, 500, 3400, 3200, 3250, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
            Stock("Google", 2800, 600, 2900, 2700, 2750, [283, 284, 274, 283, 270, 276, 284, 284, 282, 280, 281, 289, 273, 270, 275, 275, 277, 280, 270, 286, 290, 288, 270, 283, 282, 273, 283, 278, 283, 280]),
            Stock("Facebook", 340, 1500, 350, 330, 335, [342, 328, 338, 346, 336, 341, 338, 346, 347, 347, 338, 346, 354, 344, 331, 348, 338, 340, 352, 337, 352, 339, 332, 335, 335, 337, 347, 338, 328, 329]),
            Stock("Tesla", 800, 800, 810, 790, 795, [802, 788, 807, 807, 802, 807, 812, 789, 805, 791, 793, 791, 815, 814, 806, 807, 806, 785, 810, 794, 795, 807, 788, 787, 803, 786, 791, 788, 788, 795]),
            Stock("NVIDIA", 220, 1200, 230, 210,215, [211, 233, 214, 223, 228, 235, 207, 233, 219, 228, 222, 233, 226, 224, 230, 223, 209, 210, 227, 211, 213, 215, 212, 217, 223, 223, 234, 216, 207, 221]),
            Stock("JP Morgan", 160,3000 ,170 ,150 ,155, [164, 172, 165, 160, 169, 172, 153, 148, 166, 155, 152, 168, 146, 157, 171, 153, 145, 151, 156, 152, 171, 155, 161, 148, 167, 159, 174, 172, 156, 153] ),
            Stock("Visa",220 ,2500 ,230 ,210 ,215, [235, 215, 235, 214, 232, 206, 224, 231, 231, 222, 213, 235, 211, 220, 225, 209, 213, 215, 227, 223, 226, 217, 229, 231, 233, 213, 233, 235, 209, 219]),
            Stock("Johnson & Johnson",170 ,3500 ,180 ,160 ,165, [164, 160, 155, 172, 173, 184, 159, 173, 173, 174, 171, 180, 168, 159, 176, 182, 169, 185, 169, 159, 165, 178, 168, 179, 184, 173, 157, 168, 157, 174]),
            Stock("Procter & Gamble",140 ,4000 ,150 ,130 ,135, [141, 135, 153, 127, 138, 154, 137, 138, 148, 134, 148, 127, 143, 128, 135, 125, 144, 147, 134, 133, 130, 152, 132, 154, 139, 154, 148, 127, 150, 132]),
            Stock("Coca-Cola",55 ,5000 ,65 ,45 ,50, [56, 47, 63, 56, 62, 48, 48, 49, 55, 55, 60, 62, 50, 53, 49, 53, 62, 55, 51, 52, 48, 49, 47, 49, 63, 51, 57, 51, 57, 56]),
            Stock("PepsiCo",150 ,4500 ,160 ,140 ,145, [132, 164, 135, 142, 160, 166, 140, 145, 134, 158, 135, 145, 149, 147, 145, 168, 149, 139, 141, 159, 148, 148, 166, 158, 144, 163, 143, 155, 168, 141]),
            Stock("Intel",60 ,5500 ,70 ,50 ,55,[58, 52, 65, 52, 65, 57, 68, 57, 54, 66, 63, 65, 54, 54, 60, 61, 63, 58, 57, 65, 54, 68, 56, 61, 60, 64, 56, 62, 65, 54] ),
            Stock("IBM",140 ,6000 ,150 ,130 ,135, [155, 149, 124, 138, 158, 153, 134, 127, 147, 132, 152, 143, 147, 150, 133, 146, 123, 139, 127, 132, 126, 141, 141, 122, 122, 157, 150, 125, 146, 156]),
            Stock("Cisco",50 ,6500 ,60 ,40 ,45, [49, 44, 55, 57, 49, 56, 54, 44, 45, 48, 58, 54, 58, 47, 51, 50, 49, 42, 42, 42, 51, 58, 53, 49, 56, 54, 45, 46, 47, 50]),
            Stock("Oracle",80 ,7000 ,90 ,70 ,75, [86, 72, 81, 77, 72, 76, 86, 84, 81, 72, 79, 87, 79, 73, 85, 82, 73, 82, 78, 78, 86, 88, 82, 85, 78, 76, 87, 88, 78, 78]),
            Stock("Boeing",240 ,7500 ,250 ,230 ,235, [240, 225, 240, 237, 245, 228, 229, 234, 222, 227, 239, 234, 238, 225, 244, 244, 226, 246, 236, 232, 243, 240, 239, 229, 224, 230, 236, 241, 233, 231]),
            Stock("General Electric",13 ,8000 ,14 ,12 ,13, [12, 11, 11, 11, 14, 13, 11, 14, 14, 11, 13, 14, 15, 11, 11, 11, 13, 13, 14, 13, 13, 11, 14, 11, 12, 12, 12, 13, 13, 11] ),
            Stock("Ford",14 ,8500 ,15 ,13 ,14, [15, 15, 13, 15, 15, 12, 12, 14, 16, 16, 15, 14, 13, 16, 13, 16, 14, 12, 14, 16, 12, 12, 14, 16, 16, 15, 14, 16, 15, 12] ),
            Stock("Chevron",110 ,9000 ,120 ,100 ,105, [122, 115, 108, 123, 114, 106, 114, 113, 120, 94, 106, 124, 117, 101, 93, 95, 95, 111, 107, 96, 107, 123, 108, 123, 116, 110, 92, 116, 120, 126]),
            Stock("ExxonMobil",65 ,9500 ,70 ,60 ,65, [77, 54, 53, 65, 67, 49, 58, 67, 76, 52, 54, 71, 62, 69, 54, 55, 53, 52, 67, 70, 81, 66, 80, 47, 64, 81, 63, 50, 51, 72]),
            Stock("Verizon",60 ,10000 ,65 ,55 ,60, [77, 54, 53, 65, 67, 49, 58, 67, 76, 52, 54, 71, 62, 69, 54, 55, 53, 52, 67, 70, 81, 66, 80, 47, 64, 81, 63, 50, 51, 72]),
            Stock("AT&T",30 ,10500 ,35 ,25 ,30, [35, 30, 32, 38, 22, 32, 28, 34, 33, 35, 38, 38, 23, 37, 29, 32, 33, 32, 28, 33, 34, 37, 31, 35, 23, 32, 32, 32, 27, 22]),
            Stock("Pfizer",40 ,11000 ,45 ,35 ,40, [34, 44, 32, 46, 42, 37, 35, 33, 44, 41, 38, 46, 45, 40, 34, 38, 38, 42, 36, 37, 38, 35, 46, 43, 47, 42, 40, 36, 36, 37]),
            Stock("Merck",80 ,11500 ,85 ,75 ,80,[74, 83, 80, 78, 75, 72, 79, 82, 77, 76, 80, 80, 75, 73, 73, 80, 73, 82, 72, 76, 85, 87, 86, 84, 82, 82, 72, 79, 76, 80] ),
            Stock("Walgreens Boots Alliance",50 ,12000, 55, 45, 50, [45, 50, 44, 54, 57, 47, 54, 44, 44, 42, 43, 52, 51, 45, 51, 46, 47, 43, 54, 58, 57, 43, 44, 47, 51, 50, 51, 55, 43, 51]),
            Stock("CVS Health",80 ,12500, 85, 75, 80, [74, 83, 80, 78, 75, 72, 79, 82, 77, 76, 80, 80, 75, 73, 73, 80, 73, 82, 72, 76, 85, 87, 86, 84, 82, 82, 72, 79, 76, 80]),
            Stock("UnitedHealth Group",330,13000, 340, 320, 325, [314, 310, 323, 315, 322, 334, 324, 321, 332, 341, 336, 347, 343, 313, 340, 336, 320, 343, 333, 340, 322, 310, 316, 324, 323, 347, 314, 325, 342, 344]),
            Stock("McDonald's",220 ,13500, 230, 210, 215, [224, 225, 216, 229, 211, 213, 237, 204, 228, 204, 220, 218, 217, 228, 211, 205, 230, 224, 223, 238, 232, 208, 237, 211, 223, 214, 226, 231, 225, 216])
        ]

        self.views.add_url_rule('/', view_func=self.home, methods=['GET', 'POST'])
        self.views.add_url_rule('/profile', view_func=self.profile, methods=['GET', 'POST'])
        self.auth.add_url_rule('/login', view_func=self.login, methods=['GET', 'POST'])
        self.auth.add_url_rule('/logout', view_func=self.logout)
        self.auth.add_url_rule('/sign-up', view_func=self.sign_up, methods=['GET', 'POST'])
        self.views.add_url_rule('/search', view_func=self.search, methods=['GET', 'POST'])
        self.views.add_url_rule('/setting', view_func=self.setting, methods=['GET', 'POST'])

    def home(self):
        return render_template("home.html", user=current_user, stocks=self.stocks, news_items=news_items)

    def search(self):
        if request.method == "POST":
            form = request.form['form-type']
            if form == "search":
                stock_name = request.form.get('stock_name')
                for stock in self.stocks:
                    if stock.sameStock(stock_name):
                        if current_user.is_authenticated:
                            in_watchlist = current_user.in_user_watchlist(stock_name)
                            return render_template("search.html", user=current_user, stock=stock, watchlist=in_watchlist)
                        else:
                            return render_template("search.html", user=current_user, stock=stock)
                flash('Stock not found', category='error')
                return render_template("home.html", user=current_user, stocks=self.stocks, news_items=news_items)
            elif form == "buy-stock":
                stock_name = request.form["stock"]
                stock = next((s for s in self.stocks if s.name == stock_name), None)
                quantity = request.form["quantity"]
                if quantity != "":
                    quantity = int(quantity)
                    stock = next((s for s in self.stocks if s.name == stock_name), None)
                    if current_user.buy_stocks(stock, quantity):
                        flash('Stocks bought successfully!', category='success')
                    else:
                        flash('Cannot buy shares. Insufficient funds!', category='error')
                else:
                    flash('Please enter an amount!', category='error')
            elif form == "add_watchlist":
                stock_name = request.form['stock_name']
                stock = next((s for s in self.stocks if s.name == stock_name), None)
                if current_user.add_watchlist(stock):
                    flash('Stock added to watchlist successfully', category='success')
                else:
                    flash('Stock already in the watchlist', category='error')
            elif form == "remove_watchlist":
                stock_name = request.form['stock_name']
                stock = next((s for s in self.stocks if s.name == stock_name), None)
                current_user.remove_watchlist(stock)
                flash('Stock removed successfully', category='success')
                
        if current_user.is_authenticated:
            in_watchlist = False
            for stock in current_user.watchlist:
                if stock.name == stock_name:
                    in_watchlist = True
                    break
            return render_template("search.html", user=current_user, stock=stock, watchlist=in_watchlist)
        else:
            return render_template("search.html", user=current_user, stock=stock)

    @login_required
    def profile(self):
        if request.method == "POST":
            stock_name = request.form["stock"]
            if stock_name != "":
                action = request.form["action"]
                quantity = request.form["quantity"]
                if quantity != "":
                    quantity = int(quantity)
                    stock = next((s for s in self.stocks if s.name == stock_name), None)
                    if stock:
                        if action == "buy":
                            if current_user.buy_stocks(stock, quantity):
                                flash('Stocks bought successfully!', category='success')
                            else:
                                flash('Cannot buy shares. Insufficient funds!', category='error')
                        elif action == "sell":
                            if current_user.sell_stocks(stock, quantity):
                                flash('Stocks sold successfully!', category='success')
                            else:
                                flash('Cannot sell stocks. Insufficient number of stocks!', category='error')
                else:
                    flash('Please enter an amount!', category='error')
            else:
                flash('Please select a stock!', category='error')
        return render_template("profile.html", user=current_user, stocks=self.stocks, user_stocks=current_user.stocks, budget=current_user.budget, watchlist=current_user.watchlist, transaction=current_user.transaction_history)
    

    def setting(self):
        if request.method == 'POST':
            form = request.form['form-type']
            if form == "add-card":
                card_number = request.form['card-number']
                exp_date = request.form['exp-date']
                cvc = request.form['cvc']
                new_card = Bank(card_number, exp_date, cvc)
                current_user.add_bank(new_card)
                flash('Card added successfully!', category='success')
            if form == "add-funds":
                current_card = request.form['card-number']
                amount = request.form['amount']
                amount = int(amount)
                if current_user.add_funds(amount, current_card):   
                    flash('Funds added successfully!', category='success')
                else:
                    flash('Card not selected', category='error')
            if form == "change-password":
                old_password = request.form.get('old_password')
                new_password = request.form.get('new_password')

                if not current_user.change_password(old_password, new_password):
                    flash('Old password incorrect or new password does not fit requirements!', category='error')
                else:
                    flash('Password changed successfully!', category='success')
            if form == 'delete-account':
                password = request.form.get('password')
                if not check_password_hash(current_user.password, password):
                    flash('Incorrect password.', category='error')
                else:
                    db.session.delete(current_user)
                    db.session.commit()
                    logout_user()
                    flash('Account deleted successfully', category='success')
                    return render_template("home.html", user=current_user, stocks=self.stocks, news_items=news_items)
        if current_user.is_authenticated:
            return render_template("setting.html", user=current_user, cards=current_user.get_bank())
        else:
            return render_template("setting.html", user=current_user)
        

    def login(self):
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.profile'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email does not exist.', category='error')

        return render_template("login.html", user=current_user)

    @login_required
    def logout(self):
        logout_user()
        return redirect(url_for('auth.login'))

    def sign_up(self):
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('firstName')
            last_name = request.form.get('lastName')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='error')
            elif len(last_name) < 2:
                flash('Last name must be greater than 1 character.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                
                new_user = User(email=email, first_name=first_name,last_name=last_name,password=password1)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account created!', category='success')
                return redirect(url_for('views.profile'))

        return render_template("sign_up.html", user=current_user)


