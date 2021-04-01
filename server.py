from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def file1():
    return render_template('index.html')

@app.route('/<string:page_name>')
def file2(page_name):
    return render_template(page_name)

# def write_to_file(data):
    # with open('database.txt','a') as fh1:
        # email=data["email"]
        # subject=data["subject"]
        # message=data["message"]        
        # fh1.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    with open('database.csv','a',newline='') as fh2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]        
        csv1=csv.writer(fh2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv1.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/Thank_you.html')
        except:
            return 'not added to database'
    else:
        return 'something went wrong,try again'



