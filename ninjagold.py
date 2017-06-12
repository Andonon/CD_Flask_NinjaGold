'''Ninja Gold Assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
import datetime
import random
from flask import Flask, render_template, redirect, session, request

#pylint: disable=C0103,C0111

app = Flask(__name__)
app.secret_key = 'kljasldjlaskjdlkasjdlkjasdlkj'
@app.route('/')
def mainpage():

    try:
        session['gold']
    except KeyError:
        session['gold'] = 0
    try:
        session['activities']
    except KeyError:
        session['activities'] = []

    return render_template('ninjagold.html')



@app.route('/process_money', methods=['post'])
def processmoney():

    if request.form.get('action') == "farm":
        earnings = random.randrange(10, 20)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "cave":
        earnings = random.randrange(5, 10)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "house":
        earnings = random.randrange(2, 5)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "casino":
        earnings = random.randrange(-50, 50)
        session['gold'] += earnings
        if earnings > 0:
            session['activities'].append(
                'Entered a casino and Won ' + str(earnings) + ' gold! Ouch! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        else:
            session['activities'].append(
                'Entered a casino and Lost ' + str(earnings) + ' gold. Holy Cow! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
    return redirect('/')

app.run(debug=True)
