ef
is_sorted(user_list):
"""
Function takes list as its only paramater and returns True if the list is sorted, False if it isn't

    user_list= list to be tested
    sorted_list= the sorted version of user_list (will be identical if user_list is already sorted)

"""

# create and sort a copy of the user_list, then check to see if they match
sorted_list = sorted(user_list)

if user_list == sorted_list:
    return True

# Use reverse method and repeat previous step to ensure function also works when an input list is sorted by descending values
sorted_list.reverse()

if user_list == sorted_list:
    return True

else:
    return False

user_list = []

if __name__ == '__main__':

    # While loop to allow user to input their list
    while True:
        user_number = input('Enter a number (enter blank space to finish): ')

        # if/elif/else statements to error out input lists that don't meet list length requirements
        if user_number == '':
            if len(user_list) == 0:
                print("Can't sort what isn't there. Try again...")
                continue

            elif len(user_list) == 1:
                print("Single values are already sorted. Add more...")
                continue

            else:
                break

        user_list.append(user_number)

    user_list = is_sorted(user_list)

    if user_list == True:
        print('Your list is already sorted')

    else:
        print('Your list is not sorted yet')
