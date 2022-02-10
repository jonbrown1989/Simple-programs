def remove_outliers(value_list, n):
    """
    Function takes 2 inputs- one number(fl/int) and one list and removes a number of both the minimum and maximum values in the list based
    on the user inputted number, then returns it as a new list.
    value_list= User input list of numbers
    new_list= New formatted list
    n= User input number
    count= counter for 'for' loop which is set based on the input number, n
    num = each number element in new_list

    """

    # First sort list to ensure location of minimum and maximum values
    new_list = sorted(value_list)
    count = n

    # For loop and pop to remove last value in the list n times. Does not matter which of min/max values get removed since the other will be removed in next step
    for num in new_list:
        if count > 0:
            new_list.pop()
            count -= 1

    count = n

    # Reverse list and repeat previous step to remove the other n values, return the new list
    new_list.reverse()

    for r in new_list:
        if count > 0:
            new_list.pop()
            count -= 1

    return new_list


if __name__ == '__main__':

    user_list = []

    # While loop to allow user to input their list
    while True:
        user_num = input('Enter a number for your list (Enter blank space when finished): ')

        if user_num == '' and len(user_list) < 4:
            print('List needs to be at least 4 numbers, please add more')
            continue

        if user_num == '':
            break

        user_list.append(int(user_num))

    # Pass user's list through function (use 2 as number input), display output from function
    finished = remove_outliers(user_list, 2)

    print(f'\nOriginal list: {user_list}')
    print(f'New list minus outliers: {finished}')

