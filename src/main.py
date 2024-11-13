import random
from name_list import first_name, middle_name, last_name

motd = "INDONESIA USERNAME GENERATOR"
print("=" * len(motd))
print(motd)
print("=" * len(motd))

qty = int(input("quantity of usernames to be generated :"))

def generate_username():
    first = random.choice(first_name)
    middle = random.choice(middle_name)
    last = random.choice(last_name)
    number = random.randint(10, 99)
    username = f"{first.lower()}{middle.lower()}{last.lower()}{number}"
    return username

for i in range(qty):
    print(generate_username())
