from flask import Flask,render_template
import boto3
import pprint


app=Flask(__name__)

@app.route("/")
def index():
    ec2=boto3.resource('ec2')
    aws=ec2.instances.all() 
    return render_template("r3.html",aws=aws)

if __name__=='__main()':
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
    #app.run(debug=True)