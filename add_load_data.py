import json
import os
import time

def initializeJson():
    if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
        data = {"users": []}
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)


def getNames():
    if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
        return []  
    with open("data.json", "r") as f:
        data = json.load(f)
        names = [user["name"] for user in data.get("users", [])]
    return names


def addNewName(name):

    with open("data.json", "r") as f:
        data = json.load(f)

    data["users"].append({
        "name": name,
        "owes": 0,
        "paid": 0,
        "logs": []
    })

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def setPrice(target_name, new_owes):
    with open("data.json", "r") as f:
        data = json.load(f)

    for user in data["users"]:
        if user["name"] == target_name:
            user["owes"] += new_owes
            user["logs"].append((new_owes,time.ctime().split()[1::]))
            break  # stop once found

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def getPrice(target_name):
    with open("data.json", "r") as f:
        data = json.load(f)
    for user in data["users"]:
        if user["name"] == target_name:
            return user["owes"]


def clearPrice(target_name):
    with open("data.json","r") as f:
        data = json.load(f)
    for user in data["users"]:
        if user["name"] == target_name:
            if user["owes"] != 0:
                user["paid"] = user["owes"]
                user["owes"] = 0
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)