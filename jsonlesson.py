import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000} 
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

jsdata = json.dumps(data)
realdata = json.loads(talaba_json)

with open('students.json') as f:
    students = json.loads(f.read())
    for stu in students['student']:
        print(f"{stu['name']} {stu['lastname']}, {stu['year']}-kurs, {stu['faculty']} talabasi \n")
