#Danny Radosevich
#Arguments
#COSC1101

def describe_pet(pet_kind, pet_name):
    """Displays information about a pet"""
    print(f"I have a {pet_kind} and their name is {pet_name.title()}")
describe_pet("dog","Apollo")

describe_pet("fish","nemo")

describe_pet(pet_name="Apollo",pet_kind="dog")

def pets_two(pet_name, pet_kind="dog"):
    print(f"I have a {pet_kind} and their name is {pet_name.title()}")

pets_two("apollo")
