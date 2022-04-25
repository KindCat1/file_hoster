from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='text-align: center;'> Hi! </h1>"

@app.route("/set", methods=["GET"])
def set():
    data = request.args
    if data.get("file") == None or data.get("cont") == None:
        return "Error1"
    f = open("Z:\\" + data["file"], "w")
    f.write(data["cont"].replace("\\n", "\n"))
    f.close()
    return "ETOK" #EveryThing OK

@app.route("/get", methods=["GET"])
def get():
    data = request.args
    if data.get("file") == None:
        return "Error1"
    f = open("Z:\\" + data["file"])
    try:
        cont = f.read()
        f.close()
    except FileNotFoundError:
        return "Ошибка! Данный файл не найден!"
    except UnicodeDecodeError:
        return "Ошибка! Файл не может быть прочитан!"
    except:
        return "Ошибка!"
    return cont

app.run("0.0.0.0")
