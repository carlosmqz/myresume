from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    return render_template("index.html")

@application.route('/skills')
def skills():
    return render_template("skills.html")

if __name__ == '__main__':
    application.run()