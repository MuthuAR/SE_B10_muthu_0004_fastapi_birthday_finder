# Understand FASTAPI
# Create a simple API for greeting users and
# Calculating days until their next birthday.

import fastapi
from fastapi import Body, FastAPI
from datetime import date, datetime

test_app = FastAPI()

# Define a default welcome page for "/"" (root endpoint)
@test_app.get("/")
def root():
    return {"message": "Hello, Welcome to DayFinder & Birthday Calculator!"}

@test_app.get("/greet/{name}")
# Greet the user with their name and the current day of the week
def greet_with_day(name: str):
    # Find the current day of the week
    current_day = datetime.now().strftime("%A")
    return {"message": f"Hello, {name}! Today is {current_day}."}

@test_app.post("/daysdob")
# Calculate the number of days till the next birthday
def days_until_birthday(birthdate: str = Body(..., embed=True)):
    
    # Convert the birthdate string to a date object
    birthdate_obj = datetime.strptime(birthdate, "%Y-%m-%d").date()

    # Get the current date
    today = date.today()

    # Calculate the next birthday
    try:
        next_birthday = birthdate_obj.replace(year=today.year)
    except ValueError:
        next_birthday = date(today.year, 3, 1)

    # If the birthday has already occurred this year, set it to next year
    if next_birthday < today:
        try:
            next_birthday = birthdate_obj.replace(year=today.year + 1)
        except ValueError:
            next_birthday = date(today.year + 1, 3, 1)

    # Calculate the number of days until the next birthday
    days_until = (next_birthday - today).days

    return {"days_until_birthday": days_until}