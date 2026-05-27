from flask import Flask, render_template, request
from markupsafe import escape

# template_folder='.' 代表讓 Flask 直接在根目錄尋找你的 HTML 檔案
app = Flask(__name__, template_folder='.')

# ==========================================
# Exercise 39 & 44: Hello Flask
# 測試網址: /
# ==========================================
@app.route('/')
def hello_flask():
    return "Hello, World! Flask Server is running."


# ==========================================
# Exercise 40 & 45: URL Info
# 測試網址: /user/Jenny
# ==========================================
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


# ==========================================
# Exercise 41 & 46: Flask Load HTML
# 測試網址: /home
# 使用你建立的 41_46.html
# ==========================================
@app.route('/home')
def home():
    return render_template('41_46.html')


# ==========================================
# Exercise 42 & 47: Show Variables
# 測試網址: /show_vars
# 使用你建立的 42_47.html
# ==========================================
@app.route('/show_vars')
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('42_47.html', text="User Profile Info", appInfo=x)


# ==========================================
# Exercise 48: Show double of the inputted number
# 測試網址: /double 
# 使用你建立的 48.html
# ==========================================
@app.route("/double")
def double_index():
    return render_template("48.html", result=None)

@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("48.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
