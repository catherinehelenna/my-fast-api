from fastapi import FastAPI,HTTPException
app = FastAPI()

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
# @app.get('/')
# def root():
#     return {"message":"Hello World"}

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
def addStudent(studentData:dict):
    print('StudentData: ', studentData)
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
@app.get('/hacktiv-rmt-27')
# karna statis, tidak perlu berargumen
def info_rmt_27():
    return {"message":'Hacktiv RMT 27 adalah murid batch remote yang telah dilatih di Hacktiv selama 3 bulan dengan skill yang dibutuhkan oleh perusahaan'}

 
