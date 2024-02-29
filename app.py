from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)





##Create a home route
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
   
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    return "The prediction is _________"
    return redirect('/')
   





if __name__ == '__main__':
    app.run(debug=True)
