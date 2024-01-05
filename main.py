from fastapi import FastAPI
from routes import elves, packages
from data import initialize_data, assign_packages_to_elves

app = FastAPI()

app.include_router(elves.router)
app.include_router(packages.router)

initialize_data()
assign_packages_to_elves()
