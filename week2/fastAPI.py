from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':"Patient management system API "}

@app.get("/about")
def about():
    return {'message':"Fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description='Id of the patient',example='P005')):
    data = load_data()
    print(data)
    if(patient_id in data):
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail='Patient not found')
    
@app.get('/sort')
def sort_patient(sort_by:str = Query(...,description='Option to sort on the basis of height ,weight,bmi') , order:str = Query('asc',description='Sort in ascending or descending order') ):
    valid_fields = ['height','weight','bmi']
    if(sort_by not in valid_fields):
        raise HTTPException(status_code=400 , detail=f'Invalid fields, select from: {valid_fields}')
    if(order not in ['asc','desc']):
        raise HTTPException(status_code=400 , detail=f'Invalid fields, select from: asc or desc')
    
    #if everything is correct
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse = sort_order)
    return sorted_data

    

