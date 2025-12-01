from flask import render_template, request, flash
from app import app

app.config['SECRET_KEY'] = 'dfghdftyerstfgjdgykdghkcg'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        flash('Your message has been sent successfully!')

    return render_template('contact.html')
