import os
from flask import Flask, render_template, request


app = Flask(__name__)

# Database is under construction


# home page
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/uderConstruction')
def uderConstruction():
   return render_template('uderConstruction.html')


if __name__ == '__main__':
    app.run()
