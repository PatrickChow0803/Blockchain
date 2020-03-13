
import json

def save(data):
    file = open("./cache.json", "w")
    file.write(str(json.dumps(data)))
    file.close()

def load():
    with open("./cache.json") as f:
        data = json.load(f)
    return data

def main():
    data = load()
    if "id" not in data:
        id = input("Enter a user id:")
        data["id"] = id
    else:
        print(f"Welcome back {data['id']}")

    while True:
        menu = [
            "Select an Option",
            "*Change ID: 1",
            "*Check Balance: 2",
            "*View Transactions: 3",
        ]
        for item in menu:
            print(item)
        option = input()

        if option == "1":
            id = input("Enter New ID:")
            data["id"] = id

        elif option == "2":
            print(f"Your balance is {data['balance']}")
        elif option == "3":
            print(data["transactions"])

main()
