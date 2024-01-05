from typing import List, Tuple, Optional
from pydantic import BaseModel

fake_db = {
    "elves": [],
    "packages": []
}

class Elf(BaseModel):
    name: str
    available: bool = True
    maternity_leave: bool = False
    paternity_leave: bool = False

class Package(BaseModel):
    name: str
    assigned_elf: Optional[str] = None

def initialize_data():
    elves_data = [
        {"name": "Legolas"},
        {"name": "Gandalf"},
        {"name": "Arwen"},
    ]

    for elf_data in elves_data:
        elf = Elf(**elf_data)
        fake_db["elves"].append(elf)

    packages_data = [
        {"name": "Package1"},
        {"name": "Package2"},
        {"name": "Package3"},
    ]

    for package_data in packages_data:
        package = Package(**package_data)
        fake_db["packages"].append(package)

def assign_packages_to_elves():
    assignments = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]

    for elf_idx, package_idx in assignments:
        if elf_idx < len(fake_db["elves"]) and package_idx < len(fake_db["packages"]):
            fake_db["packages"][package_idx].assigned_elf = fake_db["elves"][elf_idx].name
