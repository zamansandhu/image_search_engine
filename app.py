import os
from flask import Flask, render_template, request,jsonify, request, url_for, redirect, session
import docx2txt
from flask_bootstrap import Bootstrap
from tryout import run_processing

app = Flask(__name__)
Bootstrap(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():

    target = os.path.join(APP_ROOT, 'images/')
    destination=''

    if not os.path.isdir(target):
        os.mkdir(target)


    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
    
    if request.method == 'POST':

        #first type - ignore
        print(file)
        text = docx2txt.process(destination)
        forb = [('Consultant', 'thing no 1')] 
        req = [('no greater liability', 'thing no 2')]

        #second type - ignore
        a = {'print this': ['John', 'Consultant', 'Consultant'], 'another one': ['Consultant', 'lolo', 'nunu']} 
        
        #third type (external function - in tryout.py) - fix
        result=[] 
        for r in run_processing(text):
        	result.append(r)
        #result = run_processing()
        print(result)

    return render_template('home.html', text=text, display=False, forb=forb, req=req,a=a, result=result)



if __name__ == '__main__':
    app.run(port=5000, debug=True)