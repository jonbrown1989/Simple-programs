def get_shipping_charge(items):
    """
    Function takes quantity of items as input variable, then
    determines and returns total cost of shipping for those items
    based on pricing formula

    """

    # Use if/elif/else to account for items < 2
    if items == 0:
        return 0

    elif items == 1:
        return 10.95

    else:
        total = 10.95 + ((items - 1) * 2.95)
        return total


if __name__ == '__main__':
    # Take user input for items ordered and pass through shipcharge function, display result
    items = int(input('How many items were purchased? '))
    total = get_shipping_charge(items)

    print(f'Total shipping charges: ${total}')