from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

# EX39 / EX44: Hello Flask
@app.route('/')
def hello_flask():
    return "Hello, World! Flask Server is running."

# EX40 / EX45: URL Info
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

# EX41 / EX46: Flask Load HTML
@app.route('/home')
def home():
    return render_template('41_46.html')

# EX42 / EX47: Show Variables
@app.route('/show_vars')
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('42_47.html', text="User Profile Info", appInfo=x)

# EX48: Show double of the inputted number
@app.route("/double")
def double_index():
    return render_template("48.html", result=None)

@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
