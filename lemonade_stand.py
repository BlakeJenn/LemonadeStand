# Author: Blake Jennings
# GitHub username: BlakeJenn
# Email: blakej94@gmail.com
# Description: Creates a Lemonade Stand with a MenuItem Class, a SalesForDay
# Class, and a LemonadeStand Class. The LemonadeStand Class has a dictionary of
# MenuItem Objects, a list of SalesForDay Objects, and keeps track of the current day.

class InvalidSalesItemError(Exception):
    '''Creates an InvalidSalesItemError.'''
    pass


class MenuItem:
    '''Represents an item on a Menu.'''

    def __init__(self, name, wholesale_cost, selling_price):  # str, float, float
        '''Creates a MenuItem Object with a wholesale cost and selling price.'''
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        '''Returns the name of a MenuItem Object.'''
        return self._name

    def get_wholesale_cost(self):
        '''Returns the wholesale cost of a MenuItem Object.'''
        return self._wholesale_cost

    def get_selling_price(self):
        '''Returns the selling price of a MenuItem Object.'''
        return self._selling_price


class SalesForDay:
    '''Represents the documented amount of sales for a particular day.'''

    def __init__(self, day, sales_dict):  # int, dict
        '''Creates a SalesForDay object with a recorded day and dictionary of sold items.'''
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        '''Returns the recorded day.'''
        return self._day

    def get_sales_dict(self):
        '''Returns the sales dictionary.'''
        return self._sales_dict


class LemonadeStand:
    '''Represents a Lemonade Stand that has a dictionary of MenuItem Objects,
    a list of SalesForDay Objects,keeps track of the current day, and returns
    the total profit of the stand and menu items.'''

    def __init__(self, name):
        '''Creates a LemonadeStand Object.'''
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales = []

    def get_name(self):
        '''Returns the name of a LemonadeStand Object.'''
        return self._name

    def add_menu_item(self, menuitem):  # MenuItem object
        '''Adds a MenuItem Object to the LemonadeStand Object's dictionary of
        MenuItem Objects.'''
        self._menu[menuitem.get_name()] = menuitem

    def enter_sales_for_today(self, sales_dict):  # dict
        '''Adds a SalesForDay Object to the LemonadeStand Object's list of
        SalesForDay Objects and increments the current day by one. If an item in
        the daily sales is not on the menu, it raises an InvalidSalesItemError.'''
        for item in sales_dict:
            if item not in self._menu:
                raise InvalidSalesItemError
        self._sales.append(SalesForDay(self._current_day, sales_dict))
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item_name):  # int, str
        '''Returns the amount sold of a MenuItem Object for a specific day.
        If none were sold, returns 0.'''
        sales_that_day = self._sales[day].get_sales_dict()
        if menu_item_name in sales_that_day:
            return sales_that_day[menu_item_name]
        else:
            return 0

    def total_sales_for_menu_item(self, menu_item_name):  # str
        '''Returns the total amount sold of a MenuItem Object.'''
        final = 0
        for day in range(len(self._sales)):
            final += self.sales_of_menu_item_for_day(day, menu_item_name)
        return final

    def total_profit_for_menu_item(self, menu_item_name):  # str
        '''Returns the total profit of a MenuItem object.'''
        menu_item = self._menu[menu_item_name]
        total_sold = self.total_sales_for_menu_item(menu_item_name)
        total_cash = total_sold * menu_item.get_selling_price()
        total_cost = total_sold * menu_item.get_wholesale_cost()
        return total_cash - total_cost

    def total_profit_for_stand(self):
        '''Returns the total profit of a LemonadeStand Object'''
        total = 0
        for item in self._menu:
            total += self.total_profit_for_menu_item(item)
        return total


def main():
    '''Executes the program and attempts to raise an InvalidSalesItemError'''
    stand = LemonadeStand('Lemon La Vida Loca')
    item1 = MenuItem('lemonade', 0.5, 1.75)
    stand.add_menu_item(item1)
    item2 = MenuItem('bag of chips', 1, 2)
    stand.add_menu_item(item2)
    item3 = MenuItem('brownie', 0.2, 1)
    stand.add_menu_item(item3)
    day_0_sales = {'lemonade': 5, 'brownie': 2, 'puppy': 4}

    try:
        stand.enter_sales_for_today(day_0_sales)
    except InvalidSalesItemError:
        print("Lemon La Vida Loca does not sell at least one of the items listed, Loca.")


if __name__ == '__main__':
    main()
