# Start Program
"""
Program: test_sort_and_Search.py
Author: Paul Thairu
Last date modified: 06/019/2020

Purpose of this program is to unit test. Trying to find an element in a list of elements
In my example i have a list of car type and I will try to search and sort list of these cars
"""
import unittest
from sort_search_function import cars_sort_and_search

class MyTestCase(unittest.TestCase):
    def test_sort(lst): # sorting the elements in alphabetical order
        new_lst = sorted(lst)
        cars_sort_and_search.sort_list(lst) # using sort function to sort in alphabetical order
        if lst == new_lst:
            print("Pass, car found in the list")
        else:
            print("Failed, var NOT FOUND IN THE LIST")

    def test_search(lst, value): # searching for an element (car) in the list
        index = cars_sort_and_search.search_list(lst, value)
        if index == -1:
            print(value, "Not found")
        else:
            print(value, "Present: ", index)

    my_list_cars = ["Mercedes", "Ford", "Chevrolet", "Jeep"]
    test_search(my_list_cars, "Ford")  # searching for FORD in the list
    test_search(my_list_cars, "BMW")   # searching for BMW in the list
    test_sort(my_list_cars) # sorting the cars in order

# ENd program
