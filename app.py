from flask import Flask, render_template, request
from markupsafe import escape

# template_folder='.' 設定讓 Flask 直接在根目錄尋找 41_46.html 等檔案
app = Flask(__name__, template_folder='.')

# ===================================================
# 【EX43】: Flask Online (Azure 部署測試首頁)
# 路由: /
# ===================================================
@app.route('/')
def ex43_online():
    return "<h1>[EX43] Flask Online Success!</h1><p>Your Flask App is running on Azure.</p>"


# ===================================================
# 【EX44】: Hello Flask
# 路由: /hello
# ===================================================
@app.route('/hello')
def ex44_hello():
    return "Hello, World! Flask Server is running."


# ===================================================
# 【EX45】: URL Info (傳入動態變數)
# 路由: /user/<username>
# ===================================================
@app.route('/user/<username>')
def ex45_url_info(username):
    return f'User {escape(username)}'


# ===================================================
# 【EX46】: Flask Load HTML
# 路由: /home
# 使用檔案: 41_46.html
# ===================================================
@app.route('/home')
def ex46_load_html():
    return render_template('41_46.html')


# ===================================================
# 【EX47】: Show Variables
# 路由: /show_vars
# 使用檔案: 42_47.html
# ===================================================
@app.route('/show_vars')
def ex47_show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('42_47.html', text="User Profile Info", appInfo=x)


# ===================================================
# 【EX48】: Show double of the inputted number
# 路由: /double 與 /predict
# 使用檔案: 48.html
# ===================================================
@app.route("/double")
def ex48_double_index():
    return render_template("48.html", result=None)

@app.route("/predict", methods=["POST"])
def ex48_predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("48.html", result=result)


if __name__ == "__main__":
    # Azure 部署時必須能透過 0.0.0.0 監聽
    app.run(host='0.0.0.0', port=5000, debug=True)
