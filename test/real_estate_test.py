
from app.real_estate import fetch_soldhomes


def function_type():
    results = fetch_soldhomes(State="MI",City="Detroit",Zipcode="48205")
    assert len(results) == int(25)

    
   