from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from data import fake_db

router = APIRouter()

class Elf(BaseModel):
    name: str
    available: bool = True
    maternity_leave: bool = False
    paternity_leave: bool = False

@router.post("/elves/", response_model=Elf)
def create_elf(elf: Elf):
    fake_db["elves"].append(elf)
    return elf

@router.get("/elves/", response_model=List[Elf])
def get_elves():
    return fake_db["elves"]

@router.put("/elves/{elf_id}", response_model=Elf)
def update_elf(elf_id: int, elf: Elf):
    if elf_id < len(fake_db["elves"]):
        fake_db["elves"][elf_id] = elf
        return elf
    raise HTTPException(status_code=404, detail="Elf not found")


@router.delete("/elves/{elf_id}")
def delete_elf(elf_id: int):
    if elf_id < len(fake_db["elves"]):
        del fake_db["elves"][elf_id]
        return {"message": "Elf deleted"}
    raise HTTPException(status_code=404, detail="Elf not found")

@router.put("/elves/{elf_id}/leave")
def grant_leave(elf_id: int):
    if elf_id < len(fake_db["elves"]):
        fake_db["elves"][elf_id].available = False
        return {"message": f"Leave granted to elf {elf_id}"}
    raise HTTPException(status_code=404, detail="Elf not found")


@router.put("/elves/{elf_id}/maternity-leave")
def grant_maternity_leave(elf_id: int):
    if elf_id < len(fake_db["elves"]):
        fake_db["elves"][elf_id].maternity_leave = True
        return {"message": f"Maternity leave granted to elf {elf_id}"}
    raise HTTPException(status_code=404, detail="Elf not found")


@router.put("/elves/{elf_id}/paternity-leave")
def grant_paternity_leave(elf_id: int):
    if elf_id < len(fake_db["elves"]):
        fake_db["elves"][elf_id].paternity_leave = True
        return {"message": f"Paternity leave granted to elf {elf_id}"}
    raise HTTPException(status_code=404, detail="Elf not found")


@router.put("/assign/{package_id}/{elf_id}")
def assign_package_to_elf(package_id: int, elf_id: int):
    if package_id < len(fake_db["packages"]) and elf_id < len(fake_db["elves"]):
        fake_db["packages"][package_id].assigned_elf = fake_db["elves"][elf_id].name
        return {"message": f"Package {package_id} assigned to Elf {elf_id}"}
    raise HTTPException(status_code=404, detail="Package or elf not found")
