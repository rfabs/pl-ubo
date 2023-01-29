from fastapi import FastAPI
from crbr_transform import get_company, get_person

app = FastAPI()

@app.get("/company")
def company(nip: str):
    data = get_company(nip)
    #return JSONResponse(content=jsonable_encoder(data))
    return data

#TODO nazwa, KRS, DataOd, DataDo

@app.get("/person")
def person(pesel: str):
    data = get_person(pesel)
    #return JSONResponse(content=jsonable_encoder(data))
    return data

#TODO PierwszeImie, Nazwisko, DataUrodzenia, DataOd, DataDo
