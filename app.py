from flask import Flask, render_template, request, send_file
import os
import random
import shutil
import time
app = Flask(__name__)

@app.route("/")
# 접속할 주소
def rootRouter():
    return render_template("index.html")

@app.route("/print_input", methods=["POST"])
def print_input():
    inputValue = request.form['inputValue']
    return inputValue

@app.route("/webcamTest")
def webcamTest():
    return render_template("webcamTest.html")

@app.route("/viewRanking")
def viewRanking():
    return render_template("viewRanking.html")

@app.route("/getPoseImg")
def getPoseImg():
    return send_file("./AI/402-pose-estimation-webcam/result.jpg")

@app.route("/killChrome")
def killChrome():
    os.system("taskkill /im chrome.exe")
    return "ok"

@app.route("/ingame")
def ingame():
    return render_template("ingame.html")

@app.route("/createProblem")
def createProblem():
    operator = ['+', '-', '*']
    min_val = 0
    max_val = 100
    first_num = random.randint(min_val, max_val)
    second_num = random.randint(min_val, max_val)
    selected_operator = random.choice(operator)

    if (selected_operator == "+"):
        result = first_num + second_num
    if (selected_operator == "-"):
        result = first_num - second_num
    if (selected_operator == "*"):
        result = first_num * second_num
    
    return {"first_num": first_num, "second_num": second_num, "selected_num": selected_operator, "result": result}

@app.route("/saveImage")
def saveImage():
    copyFilename = time.time()
    shutil.copy('./AI/402-pose-estimation-webcam/result.jpg', f"./datas/{copyFilename}.jpg")
    return "정상수"

    # return render_template("saveImage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)