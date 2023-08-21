# Author: Blake Jennings
# GitHub username: BlakeJenn
# Email: blakej94@gmail.com
# Description: Executes a unit test of LemonadeStand.py

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError


class TestLemonadeStand(unittest.TestCase):
    '''Creates a unit test for LemonadeStand.py'''

    def test_1(self):
        '''Tests the get_name function of MenuItem'''
        item_1 = MenuItem('Tea', 0.5, 1.25)
        self.assertEqual(item_1.get_name(), 'Tea')

    def test_2(self):
        '''Tests the get_selling_price function of MenuItem'''
        item_1 = MenuItem('Tea', 0.5, 1.25)
        self.assertEqual(item_1.get_selling_price(), 1.25)

    def test_3(self):
        '''Tests the add_menu_item function of LemonadeStand'''
        stand = LemonadeStand('Lemon La Vida Loca')
        item_1 = MenuItem('Tea', 0.5, 1.25)
        stand.add_menu_item(item_1)
        self.assertIn('Tea', stand._menu)

    def test_4(self):
        '''Tests if InvalidSalesItemError is raised'''
        stand = LemonadeStand('Lemon La Vida Loca')
        item_1 = MenuItem('Tea', 0.5, 1.25)
        stand.add_menu_item(item_1)
        day_1_sales = {'Tea': 4, 'Dog': 3}
        with self.assertRaises(InvalidSalesItemError):
            stand.enter_sales_for_today(day_1_sales)

    def test_5(self):
        '''Tests the total_profit_for_menu_item function of LemonadeStand'''
        stand = LemonadeStand('Lemon La Vida Loca')
        item_1 = MenuItem('Tea', 0.5, 1.25)
        stand.add_menu_item(item_1)
        day_0_sales = {'Tea': 5}
        stand.enter_sales_for_today(day_0_sales)
        self.assertAlmostEqual(stand.total_profit_for_menu_item('Tea'), 3.75)


if __name__ == '__main__':
    unittest.main()
