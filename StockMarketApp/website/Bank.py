# Define a class to represent a bank account
class Bank:
    # Define a constructor method to initialize the bank account with card number, expiration date and cvc
    def __init__(self, card_number, exp_date, cvc):
        self.card_number = card_number # A string of 16 digits
        self.exp_date = exp_date # A string of format MM/YY
        self.cvc = cvc # A string of 3 digits