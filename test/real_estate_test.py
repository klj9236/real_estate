
from app.real_estate import fetch_soldhomes

total_cols=len(df.axes[1])

def function_type():
    results = fetch_soldhomes(State="MI",City="Detroit",Zipcode="48205")
    assert len(results) == int(25)

    
   