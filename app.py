from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

# This is CMPE ENGR project 

app = Flask(__name__)

# Testing for user login
users = {
    'fiona': generate_password_hash('0123abcd'),
    'alyssa': generate_password_hash('4567abcd')
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/my_account', methods=['GET', 'POST'])
def my_account():
    return redirect(url_for('user_login'))

@app.route('/submit_form', methods=['POST'])
def submit_form():
    cuisine = request.form.get('cuisine')
    dietary_filter = request.form.get('dietary_filter')
    difficulty = request.form.get('difficulty')

    if cuisine == 'japanese' and dietary_filter == 'vegetarian' and difficulty == 'entry':
        return redirect(url_for('j_v_e'))
    elif cuisine == 'random' and dietary_filter == 'none' and difficulty == 'random':
        return redirect(url_for('random'))
    elif cuisine == 'japanese' and dietary_filter == 'none' and difficulty == 'entry':
        return redirect(url_for('j_n_e'))
    elif cuisine == 'japanese' and dietary_filter == 'gluten_free' and difficulty == 'entry':
        return redirect(url_for('j_g_e'))
    elif cuisine == 'japanese' and dietary_filter == 'none' and difficulty == 'advanced':
        return redirect(url_for('j_n_a'))
    elif cuisine == 'japanese' and dietary_filter == 'none' and difficulty == 'medium':
        return redirect(url_for('j_n_m'))
    elif cuisine == 'korean' and dietary_filter == 'none' and difficulty == 'entry':
        return redirect(url_for('k_n_e'))
    elif cuisine == 'korean' and dietary_filter == 'vegetarian' and difficulty == 'entry':
        return redirect(url_for('k_v_e'))
    elif cuisine == 'korean' and dietary_filter == 'none' and difficulty == 'medium':
        return redirect(url_for('k_n_m'))
    else:
        return render_template('error.html')

@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == 'Fiona' and password == '0123abcd') or (username == 'Alyssa' and password == '4567abcd'):
            return redirect(url_for('userAccount_page'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('user_login'))
    else:
        return render_template('user_login.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/userAccount_page')
def userAccount_page():
    return render_template('userAccount_page.html')

@app.route('/j_v_e')
def j_v_e():
    return render_template('j_v_e.html')

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/j_g_e')
def j_g_e():
    return render_template('j_g_e.html')

@app.route('/j_n_m')
def j_n_m():
    return render_template('j_n_m.html')

@app.route('/j_n_a')
def j_n_a():
    return render_template('j_n_a.html')

@app.route('/k_n_e')
def k_n_e():
    return render_template('k_n_e.html')

@app.route('/k_v_e')
def k_v_e():
    return render_template('k_v_e.html')

@app.route('/k_g_e')
def k_g_e():
    return render_template('k_g_e.html')

@app.route('/k_d_e')
def k_d_e():
    return render_template('k_d_e.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'  # Required for flash messages
    app.run(debug=True)
