from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "cuman_saya_yang_tahu"


# @app.get("/")
# def home():
#   return {"message":"This is my API. Welcome!"}

# @app.get("/protected")
# def protect(api_key: str = Header(None)):

#   if api_key is None or api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="Invalid API Key")

#   return {"message":"This endpoint is protected by API Token Key.",
#           "data":{"1":{"username":"fahmi","password":"1234"},
#                   "2":{"username":"raka","password":"abcd123"},
#                   "3":{"username":"rachman","password":"h8teacher"}
#                  }
#           }


# @app.get("/example")
# def read_example_headers(request: Request):
#     headers = request.headers
#     # Access specific header values
#     user_agent = headers.get("user-agent")
#     authorization = headers.get("authorization")
#     custom_header = headers.get("custom-header")

#     return {
#         "User-Agent": user_agent,
#         "Authorization": authorization,
#         "Custom-Header": custom_header
#     }


# konten kodingan

students = {
    "Aqila": {
        "score": 85,
        "age": 24
    },
    "Catherine": {
        "score": 82,
        "age": 20
    },
    "Bagus": {
        "score": 88,
        "age": 28
    },
    "Adriansyah": {
        "score": 86,
        "age": 27
    },
    "Rahardiansyah": {
        "score": 83,
        "age": 26
    }
}

# http://127.0.0.1:8000 adalah base url = '/' ; jadi  @app.get('/') akses base url
@app.get('/')
def root():
    return {"message":"Hello World"}

# statis slalu di atas dinamis
# statis
@app.get('/students')
def studentsList():
    return students

# dinamis pakai {nama_variable, bukan string}
@app.get('/{name}')
def findStudentName(name:str):
    if name in students.keys():
# cara akses list dinamis, dict_name[variable_name]; biasanya string bukan variable
        return students[name]
    else:
        raise HTTPException(status_code = 404, detail="Student Not Found")

# nanti di url tabnya di web browser, tambah /{name misal Catherine}
# http://127.0.0.1:8000/Catherine

@app.post('/students')
def addStudent(studentData:dict,api_key:str=Header(None),Authorization:str=Header(None)):
    print('StudentData: ', studentData)
    print('api_key dari user: ', api_key)
    print('authorization dari user: ', Authorization)
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail='Please submit correct API KEY')
    

    studentName = studentData['name']
    studentScore = studentData['score']
    studentAge = studentData['age']

    students[studentName] = {
        "score": studentScore,
        "age": studentAge
    }

    return {"messsage": "Student berhasil ditambahkan"}

# bikin URL sendiri
# ada @app.get, @app.post, @app.del, @app.code
# post dan code bersifat dinamis

# bikin jembatan saja
# karna statis, tidak perlu berargumen
@app.get('/hacktiv-rmt-27')
def info_rmt_27():
    return {"message":'Hacktiv RMT 27 adalah murid batch remote yang telah dilatih di Hacktiv selama 3 bulan dengan skill yang dibutuhkan oleh perusahaan'}

