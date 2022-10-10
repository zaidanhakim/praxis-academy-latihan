import json, psycopg2
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/', methods =['GET'])
def create():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        
        query = f"select * from public.tes_buah" 
        curs.execute(query)
        data = curs.fetchall()
        print(data)

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id": d[0],
        #         "name": d[4]
        #     })

        resp = {
            "data": data,
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp)

@app.route('/createdata', methods =['POST'])
def insert():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        payload=json.loads(request.data)
        print(payload)
        query = f"insert into public.tes_buah(username,email,created_on) values ('{payload['username']}', '{payload['email']}', current_timestamp)" 
        print(query)
        curs.execute(query)
        conn.commit()

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id": d[0],
        #         "name": d[4]
        #     })

        resp = {
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp)

@app.route('/updatedata', methods =['PUT'])
def update():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        payload=json.loads(request.data)
        print(payload)
        query = f"update public.tes_buah  set username = '{payload['name']}', email = '{payload['email']}'  where username = '{payload['lokasi']}'" 
        print(query)
        curs.execute(query)
        conn.commit()

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id": d[0],
        #         "name": d[4]
        #     })

        resp = {
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp)

@app.route('/deletedata', methods =['DELETE'])
def delete():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        payload=json.loads(request.data)
        print(payload)
        query = f"delete from public.tes_buah where username = '{payload['name']}'" 
        print(query)
        curs.execute(query)
        conn.commit()

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id": d[0],
        #         "name": d[4]
        #     })

        resp = {
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp)

@app.route('/selectdata', methods =['GET'])
def select():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        # payload=json.loads(request.data)
        # print(payload)
        query = f"select*from public.tes_buah where id ='2' " 
        # print(query)
        curs.execute(query)
        data = curs.fetchone()
        print(data)
        
        arrayData = {
            "nama":data[1],
            "email":data[2]
        }

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id" : d[0],
        #         "username": d[1],
        #         "email": d[2]
        #     })

        resp = {
            "data" : arrayData,
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp)

@app.route('/betweendata', methods =['GET'])
def between():
    try: #ada
        # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
        # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
        curs = conn.cursor()
        print("connected")
    except Exception:
        print("connection error")
    # payload=json.loads(request.data)
    # print(payload)
    query = f"select*from public.tes_buah where id='2'" 
    # print(query)
    curs.execute(query)
    data = curs.fetchall()
    print(data)
    
    # arrayData = {
    #     "nama":data[1],
    #     "email":data[2]
    # }
    arrayData = []
    for d in data:
        arrayData.append({
            "id" : d[0],
            "username": d[1],
            "email": d[2]
        })
    resp = {
        "data" : arrayData,
        "message": "Success"
    }
    return jsonify(resp), 202 #merapikan data untuk menjadikan jsonxk

@app.route('/indata', methods =['POST'])
def indata():
    try:
        try: #ada
            # conn = psycopg2.connect(host="194.233.73.19", database="pesantren_dev", user="p0nd0k", password="p3santr3n_2021")
            conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgre")
            # conn = psycopg2.connect(host="localhost", database="postgres 2", user="belajar_database", password="test")
            curs = conn.cursor()
            print("connected")
        except Exception:
            print("connection error")
        payload=json.loads(request.data)
        print(payload)
        username = payload["username"]
        email = payload["email"]
        lokasi = payload["lokasi"]
        print(username, email, lokasi)
        query = f"indata public.tes_buah  set username = '{payload['username']}', email = '{payload['email']}'  where location = '{payload['lokasi']}'" 
        print(query)
        curs.execute(query)
        conn.commit()

        # arrayData = []
        # for d in data:
        #     arrayData.append({
        #         "id": d[0],
        #         "name": d[4]
        #     })

        resp = {
            "message": "Success"
        }
        return jsonify(resp), 202 #merapikan data untuk menjadikan json

    except Exception as e:
        resp = {
            "data": f"{e}",
            "message": "Error"
        }
        return jsonify(resp),400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)