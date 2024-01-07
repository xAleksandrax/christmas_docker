from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

router = APIRouter()

class Elf(BaseModel):
    name: str
    available: bool = True
    maternity_leave: bool = False
    paternity_leave: bool = False

# Funkcja do dodawania elfa do bazy SQLite
@router.post("/elves/", response_model=Elf)
def create_elf(elf: Elf):
    conn = sqlite3.connect('example_db.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO elves (name, available, maternity_leave, paternity_leave) VALUES (?, ?, ?, ?)',
                   (elf.name, elf.available, elf.maternity_leave, elf.paternity_leave))
    conn.commit()
    conn.close()
    return elf

# Funkcja do pobierania elfów z bazy SQLite
@router.get("/elves/", response_model=List[Elf])
def get_elves():
    conn = sqlite3.connect('example_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM elves')
    elves_data = cursor.fetchall()
    conn.close()

    elves = []
    for elf_data in elves_data:
        elf = Elf(name=elf_data[1], available=bool(elf_data[2]), maternity_leave=bool(elf_data[3]), paternity_leave=bool(elf_data[4]))
        elves.append(elf)

    return elves

# Pozostałe funkcje obsługujące modyfikację danych elfów (update, delete, etc.) również należy zaktualizować, korzystając z `sqlite3`.
