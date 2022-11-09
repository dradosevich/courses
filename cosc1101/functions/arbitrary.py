#Danny Radosevich
#COSC1101

def make_pizza(size,*toppings):
    print(size, toppings)

make_pizza("pepperoni")
make_pizza("large","pepperoni","extra cheese", "sausage")

def build_profile(first, last, **user_info):

    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)