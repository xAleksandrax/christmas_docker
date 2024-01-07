import sqlite3

def initialize_database():
    conn = sqlite3.connect('example_db.db')
    cursor = conn.cursor()

    # Tworzenie tabel
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS elves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            available INTEGER DEFAULT 1,
            maternity_leave INTEGER DEFAULT 0,
            paternity_leave INTEGER DEFAULT 0
        )
    ''')

    # Sprawdzenie, czy tabela elves została utworzona
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='elves'")
    table_exists = cursor.fetchone()
    if table_exists:
        print("Tabela 'elves' została utworzona poprawnie.")
    else:
        print("Błąd: Tabela 'elves' nie została utworzona.")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            assigned_elf TEXT
        )
    ''')

    # Dodawanie przykładowych danych
    elves_data = [
        ('Elf 1', 1, 0, 0),
        ('Elf 2', 1, 0, 0),
        ('Elf 3', 1, 0, 0)
    ]

    packages_data = [
        ('Package 1', 'Elf 1'),
        ('Package 2', None),
        ('Package 3', 'Elf 2')
    ]

    cursor.executemany('INSERT INTO elves (name, available, maternity_leave, paternity_leave) VALUES (?, ?, ?, ?)', elves_data)
    cursor.executemany('INSERT INTO packages (name, assigned_elf) VALUES (?, ?)', packages_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
