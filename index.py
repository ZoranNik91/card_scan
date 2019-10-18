from flask import Flask, render_template
from api import api_date

app = Flask(__name__)
app.register_blueprint(api_date)

@app.route('/')
def root():
    #Renders a template from the template folder with the given context
    return render_template("index.html", title = 'DOLASCI ZA DAN')

if __name__ == '__main__':
    app.run()

