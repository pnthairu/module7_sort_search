# Start Program
"""
Program: cars_sort_and_Search.py
Author: Paul Thairu
Last date modified: 06/019/2020

You can make a new files test_sort_and_search_list.py and sort_and_search_list.py. In the appropriate directories.
For this assignment, you can hard-code a list you pass to the sort_list() and search_list()

write 2 functions sort_list() and search_list().
search_list() will return the index of the object in the list or a -1 if the item is not found
sort_list() will sort the list

"""
# Declaring getLis function
def getList(myList):
    print(myList) # print the list of items

# Declaring searchList function
def search_list(myList, search_car):
    print("****************************************************")
    print("Find " + search_car)  # element to search on th list
    for i in myList:  # looping through the list to find an element
        if (i == search_car):  # if car is not in the list break
            break
    if search_car in myList:
        pass
    else:
        return -1

def sort_list(myList):
    myList.sort()  # in build sort function to sort cars in alphabetical order
    print("My cars in alphabetical order")
    print(myList)  # Print list of cars in order


if __name__ == '__main__':
    myList = ["Mercedes", "Ford", "Chevrolet", "Jeep"]  # Hard list of cars
    search_car = "Ford"  # car to search
    getList(myList)  # function call and assigning to list of cars
    if (search_list(myList, search_car) == -1): # If car not found
        print(search_car + " 'Does not exit in the list of cars!!!!!'")
    else: # if car is found
        print(search_car + " FOUND in the list of my cars")
    print("****************************************************")
    sort_list(myList)  # sorting list in alphabetical order


