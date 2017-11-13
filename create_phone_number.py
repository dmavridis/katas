def create_phone_number(n):
    """
    Write a function that accepts an array of 10 integers (between 0 and 9), 
    that returns a string of those numbers in the form of a phone number.
    """
    phone = [''.join(str(num)) for num in n]
    phone = ''.join(phone)
    return "(" + phone[0:3] + ") " + phone[3:6] + "-" + phone[6:]

### return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)