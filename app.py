from flask import Flask,render_template,request,url_for
app= Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST' :
        username= request.form['username']
        email=request.form['email']
        password=request.form['password']
        print(f"username :{username},Email :{email}, password:{password} ")
        return render_template('success.html')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)


