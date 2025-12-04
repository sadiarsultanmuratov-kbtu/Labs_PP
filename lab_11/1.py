import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="123456789"
    )

def search_pattern():
    pattern = input("Enter pattern to search: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM find_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    print("\n Search results")
    for r in rows:
        print(r)
    conn.close()

def insert_or_update():
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    conn.close()
    print("Inserted or updated.")

def insert_many():
    n = int(input("How many users to insert? "))
    names = []
    surnames = []
    phones = []
    for i in range(n):
        print(f"--- User {i+1} ---")
        names.append(input("Name: "))
        surnames.append(input("Surname: "))
        phones.append(input("Phone: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL insert_many_users(%s, %s, %s)",
        (names, surnames, phones)
    )
    conn.commit()
    conn.close()
    print("Batch insert completed")

def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    print("\n Paginated data ")
    for r in rows:
        print(r)

    conn.close()

def delete_data():
    conn = connect()
    cur = conn.cursor()

    print("Delete by: 1 - name, 2 - surname, 3 - phone")
    option = input("Choose: ")

    if option == "1":
        value = input("Enter name: ")
        cur.execute("CALL delete_user(%s, %s)", ("name", value))

    elif option == "2":
        value = input("Enter surname: ")
        cur.execute("CALL delete_user(%s, %s)", ("surname", value))

    elif option == "3":
        value = input("Enter phone: ")
        cur.execute("CALL delete_user(%s, %s)", ("phone", value))

    else:
        print("Invalid option")
        return

    conn.commit()
    conn.close()
    print("Deleted successfully.")

def main():
    while True:
        print("\n PHONEBOOK MENU")
        print("1 - Search by pattern")
        print("2 - Insert or update user")
        print("3 - Insert many users")
        print("4 - Pagination")
        print("5 - Delete user")
        print("0 - Exit")

        choice = input("Choose option: ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            insert_or_update()
        elif choice == "3":
            insert_many()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()