import json 

Data="stud.json"

def read_json():
    f=open(Data,"r")
    data=json.load(f)
    f.close()
    return data
    
def write_json(written_data):
    f=open(Data,"w")
    json.dump(written_data,f,indent=4) 
    f.close()   