import json

# Открываем JSON-файл
with open("labs/lab4/JSON parsing/data.json", "r") as f:

    data = json.load(f)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 10, "-" * 10)

# Проходим по всем интерфейсам в imdata
for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu = attrs["mtu"]

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))