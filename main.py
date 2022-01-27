import json
import os

n = 0
users_dict = {
    "user_count": n
}

if os.stat("storage.json").st_size != 0:
    with open("storage.json", "r") as f:
        all_data = json.loads(f.read())
        if all_data["user_count"]:
            n = all_data["user_count"]
else:
    all_data = {
        "user_count": n
    }


def add_to(users):
    global n
    name = input("Name: ").title()
    bday = input("Birthday: ")
    age = input("Age: ")
    email = input("Email: ")
    password = input("Password: ")
    # if type(name) != str or type(bday) != int or type(age) != int or type(email) != str:
    #     print("invalid datatypes. try again")
    #     return
    users[f"user{n}"] = {
        "name": name,
        "birthday": bday,
        "age": age,
        "email": email,
        "password": password
    }


more = "y"
while more == "y":
    # if add_to(all_data) is not None:
    n += 1
    add_to(all_data)
    all_data["user_count"] = n
    more = input("More people? Y or N: ").lower()

with open("storage.json", "w") as outfile:
    json.dump(all_data, outfile)


