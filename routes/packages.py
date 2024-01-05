from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from data import fake_db

router = APIRouter()

class Package(BaseModel):
    name: str
    assigned_elf: Optional[str] = None

@router.post("/packages/", response_model=Package)
def create_package(package: Package):
    fake_db["packages"].append(package)
    return package

@router.get("/packages/", response_model=List[Package])
def get_packages():
    return fake_db["packages"]

@router.put("/packages/{package_id}", response_model=Package)
def update_package(package_id: int, package: Package):
    if package_id < len(fake_db["packages"]):
        fake_db["packages"][package_id] = package
        return package
    raise HTTPException(status_code=404, detail="Package not found")


@router.delete("/packages/{package_id}")
def delete_package(package_id: int):
    if package_id < len(fake_db["packages"]):
        del fake_db["packages"][package_id]
        return {"message": "Package deleted"}
    raise HTTPException(status_code=404, detail="Package not found")
