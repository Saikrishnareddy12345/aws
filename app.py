from flask import Flask,render_template
import boto3
import pprint


app=Flask(__name__)

@app.route("/")
def index():
    ec2=boto3.resource('ec2')
    aws=ec2.instances.all()
    data=[]
    data1=[]
    for i in aws:
            data.append(i.id)
            data1.append(i.instance_type)
            
    
    return render_template("home.html",data=data,data1=data1)

if __name__=='__main()':
    #app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
    app.run(debug=True)