from fastapi import FastAPI
from routes import elves, packages
from init_db import initialize_database  # Dodaj import inicjalizacji bazy danych

app = FastAPI()

app.include_router(elves.router)
app.include_router(packages.router)

if __name__ == "__main__":
    initialize_database()  # Inicjalizacja bazy danych

    # Tu możesz wykonać inne operacje, które wymagają bazy danych SQLite
