from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods = ['POST','GET'])
def index():
    if request.method =='POST' :
        Name = request.form.get('Name')
        College = request.form.get('College')
        University = request.form.get('University')
        print(Name)
        print(College)
        print(University)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)