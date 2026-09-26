from fastapi import FastAPI
from Schema.user_input import UserInput
from model.predict import predict_output
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get('/')
def Mama():
    return {'message': 'Mama Jayaguru ,Welcome to laptop price production API'}

@app.post('/predict')
def predict(data: UserInput):
    input_dic={
    'Company': data.company  ,
    'TypeName':  data.TypeName,
    'Ram' : data.Ram,
    'Weight' : data.weight,
    'Touchscreen' : data.ts,
    'IPS'  : data.ips,
    'ppi': data.ppi,
    'Op_sys': data.opsys,
    'Cpu_name': data.cpu_name,
    'HDD':   data.Hard_drive,
    'SSD':   data.ssd,
    'Gpu brand': data.gpu_name
    }
    try:
        price=predict_output(input_dic)
        return JSONResponse(status_code=200,content={'Price' : price})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
