from flask import Flask,redirect,render_template,url_for,abort,make_response,request

app = Flask(__name__)

@app.route('/')
def return_hello():
    return "HEllo 陈辉"

@app.route('/hello/<str>')
def return_str(str):
    return str

@app.route('/page')
def return_page():
    return render_template('index.html',msg = '登录用户名或密码错误')

@app.route('/error_page')
def return_error_page():
    return render_template('error.html',msg = '登录用户名或密码错误')

@app.route('/success_page')
def return_success_page():
    return render_template('success.html',msg = '正在登陆中。。。')

@app.route('/login',methods=['GET','POST'])
def login_in():
    if request.form['username'] == 'yufx' and request.form['password'] == '123':
        return redirect(url_for('return_success_page'))
    else:
        return redirect(url_for('return_error_page'))

@app.route('/index')
def return_url():
    return redirect(url_for('return_page'))

@app.route('/code')
def return_error():
    abort(405)

@app.route('/set')
def return_set():
    response = make_response("返回一个自定义的响应")
    response.headers['cookies']= "abc"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
