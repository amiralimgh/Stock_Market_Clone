# Define a Stock class to represent a stock
class Stock:
    # Initialize the class with attributes for name, price, volume, high, low, open and price_30_days
    def __init__(self, name, price, volume,high, low, open, list):
        self.name = name # The name of the stock
        self.price = price # The current price of the stock
        self.volume = volume # The number of shares traded
        self.high = high # The highest price of the day
        self.low = low # The lowest price of the day
        self.open = open # The opening price of the day
        self.price_30_days = list # A list of prices for the past 30 days

    # Define a method to increase the volume by a given amount
    def volume_up(self, amount):
        self.volume += amount
        return self.volume

    # Define a method to decrease the volume by a given amount
    def volume_down(self, amount):
        # Check if the amount is greater than the current volume
        if amount > self.volume:
            # Print an error message and return
            print(f"Error: Cannot sell {amount} shares. Only {self.volume} shares available.")
            return
        # Otherwise, subtract the amount from the current volume
        self.volume -= amount
        return self.volume


    def sameStock(self, searchedStock):
        if self.name == searchedStock:
            return True
        return False