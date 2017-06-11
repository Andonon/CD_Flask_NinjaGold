'''Ninja Gold Assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103,C0111

from flask import Flask, render_template, redirect, session

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('ninjagold.html')



@app.route('/process_money')
def processmoney():
    return redirect('/')



app.run(debug=True)
