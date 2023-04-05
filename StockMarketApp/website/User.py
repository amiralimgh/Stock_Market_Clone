# Import the db object from the same package
from . import db
# Import the UserMixin and func objects from flask_login and sqlalchemy
from flask_login import UserMixin
from sqlalchemy.sql import func
# Import the generate_password_hash and check_password_hash functions from werkzeug.security
from werkzeug.security import generate_password_hash, check_password_hash

# Define a User class that inherits from db.Model and UserMixin
class User(db.Model, UserMixin):
    # Initialize the class with attributes for email, password, first_name, last_name, budget, stocks, banks and watchlist
    def __init__(self, email, password, first_name, last_name):
        self.email = email # The user's email address
        self.password = generate_password_hash(password, method='sha256') # The user's password
        self.first_name = first_name # The user's first name
        self.last_name = last_name # The user's last name
        self.budget = 0 # The user's budget for buying stocks
        if not self.stocks:
            self.stocks = [] # A list of stocks that the user owns
        self.banks = [] # A list of bank accounts that the user has
        self.watchlist = [] # A list of stocks that the user is watching
        self.transaction_history = []
        
    # Define the columns for the user table in the database
    id = db.Column(db.Integer, primary_key=True) # The user's id (primary key)
    email = db.Column(db.String(150), unique=True) # The user's email (unique)
    password = db.Column(db.String(150)) # The user's password
    first_name = db.Column(db.String(150)) # The user's first name
    last_name = db.Column(db.String(150)) # The user's last name
    budget = db.Column(db.Integer) # The user's budget
    stocks = db.Column(db.PickleType) # The user's stocks (stored as a pickle type)
    banks = db.Column(db.PickleType) # The user's banks (stored as a pickle type)
    watchlist = db.Column(db.PickleType) # The user's watchlist (stored as a pickle type)
    transaction_history = db.Column(db.PickleType)

    # Define a method to buy stocks for the user
    def buy_stocks(self, stock, amount):
        cost = stock.price * amount # Calculate the cost of buying the stock
        if cost > self.budget or amount > stock.volume: # Check if the cost exceeds the budget
            return False
        stock.volume_down(amount) # Decrease the volume of the stock by the amount bought
        self.budget -= cost # Subtract the cost from the budget

        for s in self.stocks: # Loop through the stocks that the user owns
            if s['name'] == stock.name: # Check if the stock is already in the list
                new_quantity = s['quantity'] + amount # Increase the quantity by the amount bought
                self.stocks.remove(s) # Remove the old entry from the list
                self.stocks = self.stocks + [{'name': stock.name, 'quantity': new_quantity}] # Add a new entry with the updated quantity to the list
                self.transaction_history = self.transaction_history + [('Bought', stock.name, amount)]
                db.session.commit() # Commit the changes to the database
                return True # Return True to indicate success
        self.stocks = self.stocks + [{'name': stock.name, 'quantity': amount}] # If the stock is not in the list, add a new entry with the amount bought to the list
        self.transaction_history = self.transaction_history + [('Bought', stock.name, amount)]
        db.session.commit() # Commit the changes to the database
        return True # Return True to indicate success

    def sell_stocks(self, stock, amount):
        for s in self.stocks: # Loop through the stocks that the user owns
            if s['name'] == stock.name: # Check if the stock is in the list
                if s['quantity'] < amount: #if qunaity less the amount print error
                    return False
                stock.volume_up(amount) # else increase volume
                # Add the revenue from selling the stock to the budget
                self.budget += stock.price * amount
                # Calculate the new quantity of the stock after selling
                new_quantity = s['quantity'] - amount
                # Add a new entry with the updated quantity to the list of stocks
                self.stocks.remove(s)
                self.stocks = self.stocks + [{'name': stock.name, 'quantity': new_quantity}]
                db.session.commit()
                # Remove the old entry from the list of stocks if the quantity is 0
                updated_stocks = []
                for s in self.stocks:
                    if s['quantity'] != 0:
                        updated_stocks += [s]
                self.stocks = updated_stocks
                self.transaction_history = self.transaction_history + [('Sold', stock.name, amount)]
                db.session.commit()  # Update the budget and stocks in the database
                # Return True to indicate success
                return True
        return False

        # Define a method to add a bank account to the user
    def add_bank(self, bank):
        # Append the bank to the list of banks
        self.banks = self.banks + [bank]
        # Update the banks in the database
        db.session.commit()
        return self.banks

    # Define a method to get the list of bank accounts for the user
    def get_bank(self):
        # Return the list of banks
        return self.banks
        
    # Define a method to add funds to the user's budget
    def add_funds(self, amount, current_card):
        if any(card.card_number == current_card for card in self.banks):
            amount = int(amount)
            self.budget += amount
            db.session.commit()
            return True
        return False

    # Define a method to change the user's password
    def change_password(self, old_password, new_password):
        # Check if the old password matches the current password
        if not check_password_hash(self.password, old_password):
            # If not, return False
            return False
        # Check if the new password is at least 6 characters long
        elif len(new_password) < 6:
            # If not, return False
            return False
        else:
            # Otherwise, generate a hashed password from the new password using sha256 method
            self.password = generate_password_hash(new_password, method='sha256')
            # Update the password in the database
            db.session.commit()
            # Return True to indicate success
            return True
            
    # Define a method to add a stock to the user's watchlist
    def add_watchlist(self, stock):
        # Loop through the watchlist
        for s in self.watchlist:
            # Check if the stock is already in the watchlist
            if stock.name == s.name:
                # If so, return False
                return False
        # Otherwise, append the stock to the watchlist
        self.watchlist = self.watchlist + [stock]
        # Update the watchlist in the database
        db.session.commit()
        # Return True to indicate success
        return True
        
    def remove_watchlist(self, stock):
        updated_watchlist = []
        for s in self.watchlist:
            if s.name != stock.name:
                updated_watchlist += [s]
        if len(updated_watchlist) != len(self.watchlist):
            self.watchlist = updated_watchlist
            db.session.commit()
            print(self.watchlist)
            return True
        print(self.watchlist)
        return False
        
    def in_user_watchlist(self, stock_name):
        for stock_self in self.watchlist:
            if stock_self.name == stock_name:
                return True
        return False