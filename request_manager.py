
from fileinput import filename 
from flask import * 
import os  
import re 
from database_manager import DB
from s3_manager import S3


app = Flask(__name__)   

def check_email_format(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    return False

def add_request(email,file):
    db = DB()
    id = db.new_request(email)

    s3= S3()
    s3.upload_object(id,file)
    # pass



@app.route('/')   
def main():   
    return render_template("index.html")   

@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST': 
        email = request.form.get("email")  
        
        file = request.files['file']   
        print(email)
        print(type(file))
        print("-------")
        if (check_email_format(email) and file.filename.endswith(".mp3")):
            add_request(email,file)
            return render_template("Acknowledgement.html", name = file.filename)   
        else:
            print("error")
            
        
    
    

def run():
    app.run(debug=True)

run()