import psycopg2
import csv
import os


# подключение бд
def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="123456789"
    )


###################################создание таблицы
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(100),
            surname VARCHAR(100),
            phone_number VARCHAR(20)
        );
    """)
    conn.commit()
    conn.close()
    print("Таблица 'phonebook' создана или существует")


###################################создание таблицы через csv

def insert_from_csv(filename='phonebook.csv'):
    conn = connect()
    cur = conn.cursor()

    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, filename)

    if not os.path.exists(csv_path):
        print(f"CSV файл не найден: {csv_path}")
        return

    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)

        count = 0
        for row in reader:
            if len(row) >= 3:
                user_name = row[0].strip()
                surname = row[1].strip()
                phone_number = row[2].strip()

                cur.execute(
                    "INSERT INTO phonebook (user_name, surname, phone_number) VALUES (%s, %s, %s)",
                    (user_name, surname, phone_number)
                )
                count += 1

    conn.commit()
    conn.close()
    print(f"Данные из CSV добавлены. Добавлено контактов: {count}")


############## добавляем через консоль

def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Телефон: ")

    cur.execute(
        "INSERT INTO phonebook (user_name, surname, phone_number) VALUES (%s, %s, %s)",
        (name, surname, phone)
    )

    conn.commit()
    conn.close()
    print("Контакт добавлен")


################################### процедура insert_or_update
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


################################### процедура insert_many_users 
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
    
    try:
        cur.execute("CALL insert_many_users(%s, %s, %s)", (names, surnames, phones))
        conn.commit()
        print("Batch insert completed")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()


################################### функция пагинации 
def pagination():
    limit = int(input("Limit (сколько записей на странице): "))
    offset = int(input("Offset (с какой записи начать): "))
    conn = connect()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        
        print(f"\nСтраница данных (лимит: {limit}, смещение: {offset})")
        print("-" * 50)
        
        if rows:
            print(f"{'ID':<5} {'Имя':<15} {'Фамилия':<15} {'Телефон':<15}")
            print("-" * 50)
            for r in rows:
                print(f"{r[0]:<5} {r[1]:<15} {r[2]:<15} {r[3]:<15}")
        else:
            print("Нет данных для отображения")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


################################### функция удаления через процедуру
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


## фильтрация

def query_data():
    conn = connect()
    cur = conn.cursor()
    
    print("\n1 - Все контакты")
    print("2 - Поиск по имени")
    print("3 - Поиск по фамилии")
    print("4 - Поиск по телефону")
    print("5 - Поиск по ID")
    print("6 - Поиск по шаблону") 
    choice = input("Выберите: ")
    
    if choice == '1':
        cur.execute("SELECT * FROM phonebook ORDER BY id")
        results = cur.fetchall()
    elif choice == '2':
        name = input("Имя: ")
        cur.execute("SELECT * FROM phonebook WHERE user_name ILIKE %s ORDER BY id", (f'%{name}%',))
        results = cur.fetchall()
    elif choice == '3':
        surname_input = input("Фамилия: ")
        cur.execute("SELECT * FROM phonebook WHERE surname ILIKE %s ORDER BY id", (f'%{surname_input}%',))
        results = cur.fetchall()
    elif choice == '4':
        phone = input("Телефон: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number ILIKE %s ORDER BY id", (f'%{phone}%',))
        results = cur.fetchall()
    elif choice == '5':
        try:
            contact_id = int(input("ID контакта: "))
            cur.execute("SELECT * FROM phonebook WHERE id = %s", (contact_id,))
            results = cur.fetchall()
        except ValueError:
            print("ID должен быть числом!")
            return
    elif choice == '6':  
        pattern = input("Введите шаблон для поиска: ")
        search_pattern = f'%{pattern}%'
        cur.execute("""
            SELECT * FROM phonebook 
            WHERE user_name ILIKE %s 
               OR surname ILIKE %s 
               OR phone_number ILIKE %s 
            ORDER BY id
        """, (search_pattern, search_pattern, search_pattern))
        results = cur.fetchall()
    else:
        print("Неверный выбор")
        return
    
    if results:
        print(f"\nНайдено контактов: {len(results)}")
        print("-" * 50)
        print(f"{'ID':<5} {'Имя':<15} {'Фамилия':<15} {'Телефон':<15}")
        print("-" * 50)
        for row in results:
            print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15}")
    else:
        print("Ничего не найдено")
    
    conn.close()


################ обновление

def update_data():
    conn = connect()
    cur = conn.cursor()

    print("\nОБНОВЛЕНИЕ КОНТАКТА")
    print("1 - Изменить по ID")
    print("2 - Изменить по телефону")
    choice = input("Выберите: ")

    if choice == '1':
        try:
            contact_id = int(input("ID контакта: "))
            
            cur.execute("SELECT * FROM phonebook WHERE id = %s", (contact_id,))
            if not cur.fetchone():
                print(f"Контакт с ID {contact_id} не найден")
                conn.close()
                return
                
            print("Что вы хотите изменить?")
            print("1 - Имя")
            print("2 - Фамилию")
            print("3 - Телефон")
            print("4 - Все данные")
            sub_choice = input("Выберите: ")
            
            if sub_choice == '1':
                new_name = input("Новое имя: ")
                cur.execute("UPDATE phonebook SET user_name = %s WHERE id = %s", (new_name, contact_id))
                print("Имя обновлено")
            elif sub_choice == '2':
                new_surname = input("Новая фамилия: ")
                cur.execute("UPDATE phonebook SET surname = %s WHERE id = %s", (new_surname, contact_id))
                print("Фамилия обновлена")
            elif sub_choice == '3':
                new_phone = input("Новый телефон: ")
                cur.execute("UPDATE phonebook SET phone_number = %s WHERE id = %s", (new_phone, contact_id))
                print("Телефон обновлен")
            elif sub_choice == '4':
                new_name = input("Новое имя: ")
                new_surname = input("Новая фамилия: ")
                new_phone = input("Новый телефон: ")
                cur.execute("""UPDATE phonebook 
                             SET user_name = %s, surname = %s, phone_number = %s 
                             WHERE id = %s""", 
                           (new_name, new_surname, new_phone, contact_id))
                print("Все данные обновлены")
            else:
                print("Неверный выбор")
                
        except ValueError:
            print("ID должен быть числом!")
            
    elif choice == '2':
        old_phone = input("Старый телефон: ")
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE phone_number = %s", (new_phone, old_phone))
        print("Телефон обновлен")
    else:
        print("Неверный выбор")
        conn.close()
        return

    conn.commit()
    conn.close()


################ удаление

def delete_contact():
    conn = connect()
    cur = conn.cursor()

    print("\nУДАЛЕНИЕ КОНТАКТА")
    print("1 - Удалить по ID")
    print("2 - Удалить по имени")
    print("3 - Удалить по фамилии")
    print("4 - Удалить по телефону")
    choice = input("Выберите: ")

    if choice == '1':
        try:
            contact_id = int(input("ID для удаления: "))
            cur.execute("SELECT * FROM phonebook WHERE id = %s", (contact_id,))
            contact = cur.fetchone()
            if contact:
                print(f"Удаляем контакт: ID={contact[0]}, Имя={contact[1]}, Фамилия={contact[2]}, Телефон={contact[3]}")
                confirm = input("Подтвердите удаление (y/n): ")
                if confirm.lower() == 'y':
                    cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id,))
                    print("Контакт удален")
                else:
                    print("Удаление отменено")
            else:
                print(f"Контакт с ID {contact_id} не найден")
        except ValueError:
            print("ID должен быть числом!")
    elif choice == '2':
        name = input("Имя для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE user_name = %s", (name,))
    elif choice == '3':
        surname = input("Фамилия для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE surname = %s", (surname,))
    elif choice == '4':
        phone = input("Телефон для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
    else:
        print("Неверный выбор")
        conn.close()
        return

    conn.commit()
    conn.close()


################################### ГЛАВНОЕ МЕНЮ

def main():
    """Главное меню программы"""
    print("_" * 50)
    print("Phonebook")
    print("_" * 50)

    create_table()
    
    while True:
        print("\n" + "_" * 30)
        print("ГЛАВНОЕ МЕНЮ")
        print("_" * 30)
        print("1. Загрузить из CSV")
        print("2. Добавить контакт")
        print("3. Добавить/Обновить контакт (процедура)")
        print("4. Добавить несколько пользователей")  
        print("5. Просмотр по страницам (пагинация)")
        print("6. Изменить контакт")
        print("7. Найти контакты")
        print("8. Удалить контакт")
        print("9. Удалить через процедуру")
        print("10. Выход")

        choice = input("\nВыберите действие (1-10): ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            insert_or_update()
        elif choice == '4':
            insert_many()
        elif choice == '5':
            pagination()
        elif choice == '6':
            update_data()
        elif choice == '7':
            query_data()
        elif choice == '8':
            delete_contact()
        elif choice == '9':
            delete_data()
        elif choice == '10':
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


# ЗАПУСК ПРОГРАММЫ
if __name__ == "__main__":
    main()