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






###################################создания таблицы
def create_table():
    conn = connect() ##установление соединение с бз
    if conn is None:
        return
    
    cur = conn.cursor()   ## объект для выполнения SQL запросов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebooks (
            user_name VARCHAR(100),
            phone_number VARCHAR(20)
        );
    """) ##доет возможность написать запросы в SQL 
    conn.commit()  ##для сохранение изменении
    conn.close()
    print("Таблица 'phonebooks' создана или существует")






###################################создание таблицы через csv

def insert_from_csv(filename='phonebook.csv'):
    conn = connect()
    cur = conn.cursor()

    # путь относительно скрипта
    script_dir = os.path.dirname(__file__)
    csv_path = os.path.join(script_dir, filename)

    if not os.path.exists(csv_path):
        print(f"CSV файл не найден: {csv_path}")
        return

    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)  # пропустить заголовок, если есть
        
        
        for row in reader:
            if len(row) >= 2:  # проверка на корректность строки
                user_name = row[0].strip()
                phone_number = row[1].strip()
                
                cur.execute(
                    "INSERT INTO phonebooks (user_name, phone_number) VALUES (%s, %s)",
                    (user_name, phone_number)
                )

    conn.commit()
    conn.close()
    print("Данные из CSV добавлены. Добавлено контактов ")






############## добавляем через консоль

def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    
    name = input("Имя: ")
    phone = input("Телефон: ")
    
    cur.execute(
        "INSERT INTO phonebooks (user_name, phone_number) VALUES (%s, %s)",
        (name, phone)
    )
    
    conn.commit()
    conn.close()
    print("Контакт добавлен")






## фильтрация

def query_data():
    
    conn = connect()
    cur = conn.cursor()
    
    print("\n1 - Все контакты")
    print("2 - Поиск по имени")
    print("3 - Поиск по телефону")
    choice = input("Выберите: ")
    
    if choice == '1':
        cur.execute("SELECT * FROM phonebooks ORDER BY user_name")
    elif choice == '2':
        name = input("Имя: ")
        cur.execute("SELECT * FROM phonebooks WHERE user_name LIKE %s", (f'%{name}%',))
    elif choice == '3':
        phone = input("Телефон: ")
        cur.execute("SELECT * FROM phonebooks WHERE phone_number LIKE %s", (f'%{phone}%',))
    else:
        print("Неверный выбор")
        return
    
    results = cur.fetchall()
    
    if results:
        print(f"\nНайдено контактов: {len(results)}")
        print("-" * 30)
        for row in results:
            print(f"{row[0]} - {row[1]}")
    else:
        print("Ничего не найдено")
    
    cur.close()
    conn.close()






################ обновление

def update_data():
    conn = connect()
    cur = conn.cursor()
    
    print("\nОБНОВЛЕНИЕ КОНТАКТА")
    print("1 - Изменить имя")
    print("2 - Изменить телефон")
    choice = input("Выберите: ")
    
    if choice == '1':
        phone = input("Телефон контакта: ")
        new_name = input("Новое имя: ")
        cur.execute("UPDATE phonebooks SET user_name = %s WHERE phone_number = %s", 
                   (new_name, phone))
        print("Имя обновлено")
    
    elif choice == '2':
        old_phone = input("Старый телефон: ")
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE phonebooks SET phone_number = %s WHERE phone_number = %s", 
                   (new_phone, old_phone))
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
    print("1 - Удалить по имени")
    print("2 - Удалить по телефону")
    choice = input("Выберите: ")
    
    if choice == '1':
        name = input("Имя для удаления: ")
        cur.execute("DELETE FROM phonebooks WHERE user_name = %s", (name,))
    elif choice == '2':
        phone = input("Телефон для удаления: ")
        cur.execute("DELETE FROM phonebooks WHERE phone_number = %s", (phone,))
    else:
        print("Неверный выбор")
        conn.close()
        return
    
    conn.commit()
    cur.close()
    conn.close()




################################### ГЛАВНОЕ МЕНЮ

def main():
    """Главное меню программы"""
    print("_" * 50)
    print("Phonebook")
    print("_" * 50)
    
    # Создаем таблицу при запуске
    create_table()
    
    while True:
        print("\n" + "_" * 30)
        print("ГЛАВНОЕ МЕНЮ")
        print("_" * 30)
        print("1. Загрузить из CSV")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Найти контакты")
        print("5. Удалить контакт")
        print("6. Выход")
        
        choice = input("\nВыберите действие (1-6): ")
        
        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()  
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

# ЗАПУСК ПРОГРАММЫ 
if __name__ == "__main__":
    main()