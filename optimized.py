import csv
from itertools import combinations
import time


file_one = "./data/dataset1_Python+P7.csv"
file_two = "./data/dataset2_Python+P7.csv"
file_three = "./data/bruteforce.csv"

CSV_FILE = [file_one, file_two, file_three]
MAX_COST = 500

class Wallet:

    list_wallet = []

    def __init__(self, actions):
        self.actions = actions
        self.profit = self.calc_profit()
        self.list_wallet.append(self)

    def add_action(self, action):
        self.actions.append(action)
        self.profit = self.calc_profit()

    def calc_profit(self):
        profit = 0
        for action in self.actions:
            profit += action.profit_on_investment
        return profit

    def cost(self):
        total = 0
        for action in self.actions:
            total += action.price
        return total

    def __gt__(self, action):
        return self.profit > action.profit
    
    def __lt__(self, action):
        return self.profit < action.profit
    
    def __str__(self):
        result = ''
        for action in self.actions:
            result += f'name: {action.name}, '
            result += f'price: {action.price}€, '
            result += f'profit: {round(action.profit_on_investment, 2)}€\n'
    
        result += f'total = {round(self.cost(), 2)}€\n'
        result += f'profit = {round(self.profit, 2)}€\n'

        return result

class Action:

    list_action = []

    def __init__(self, name, price, profit):
        self.name = name
        self.price = float(price)
        self.profit = float(profit)
        self.profit_on_investment = self.calc_profit()
        self.ratio = self.profit_on_investment / self.price

        self.list_action.append(self)

    def calc_profit(self):
        return (self.price * self.profit)/100
    
    def __str__(self):
        return f'{self.name} | {self.price} | {self.profit}'

def read_csv(my_file):
    with open(my_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['price']) > 0:
                Action(row['name'], row['price'], row['profit'])

def main():
    read_csv(CSV_FILE[0])
    sorted_list = sorted(Action.list_action, key=lambda action: action.ratio, reverse=True)
    wallet = Wallet([])

    for action in sorted_list:
        if action.price > 0 and ((wallet.cost() + action.price) <= MAX_COST):
            wallet.add_action(action)
        if wallet.cost() >= MAX_COST:
            break

    print(wallet)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)