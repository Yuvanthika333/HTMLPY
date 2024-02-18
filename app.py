from flask import Flask,render_template,request,redirect,url_for
from jsonutiles import *

app=Flask(__name__)

@app.route("/register",methods=["GET","POST"])
def resister():
    if request.method=="POST":
        data=read_json()
        stud_data={
            "sno":len(data["student"])+1,
            "name": request.form["Name"],
            "address":request.form["Address"],
            "course":request.form["Course"],
            "course_duration":request.form["Courseduration"]
        }
        data["student"].append(stud_data)
        write_json(data)
        # msg="Student registred successfully"
    return redirect("/home")

# @app.route("/msg/<str>")
@app.route("/",methods=["POST","GET"])
def login():
    msg=""
    if request.method=="POST":
        
        data=read_json()
        for user in data["users"]:
            # print(request.form["username"],user["username"])
            # print(request.form["pass"],user["password"])
            if request.form["username"]==user["username"] and request.form["pass"]==user["password"]:
                print("login succesfully")
                
                return redirect("/home")
        msg=request.form["username"]+"username not match"    
            
    return render_template("login.html",msg=msg)

@app.route("/delete/<id>")
def delete(id):
    data=read_json()
    for stud in data["student"]:
        if stud["sno"]==int(id):
            data["student"].remove(stud)
    
    sno=1
    for stud in data["student"]:
        stud["sno"]=sno
        sno+=1
    write_json(data)
        
    return redirect("/home")
                
@app.route("/update/<id>",methods=["POST","GET"])
def update(id):
    data=read_json()
    for stud in data["student"]:
        if stud["sno"]==int(id):
            stud["name"]=request.form["Name"]
            stud["address"]=request.form["Address"]
            stud["course"]=request.form["Course"]
            stud["course_duration"]=request.form["Courseduration"]
    
    write_json(data)
        
    return redirect("/home")
                                

@app.route("/home")       
def home(msg=None):
    data=read_json()
    
    # finalmsg=msg
    # msg=""
    return render_template("index.html",stud_data=data["student"],final="")
    
if __name__=="__main__":
    app.run(debug=True)
    
