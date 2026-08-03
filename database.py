import json

def backup_database():
    with open("data/students.json", "r") as f:
        data = json.load(f)

    with open("data/backup.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Backup Created")