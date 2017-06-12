'''Ninja Gold Assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103,C0111

from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'kljasldjlaskjdlkasjdlkjasdlkj'

def getrandomnum(start,end):
    import random
    return random.randint(start, end)

def hasgold():
    #check to see if they have any gold, set variable.
    try:
        session['gold'] += 0
        print "=== got session gold from client ==="
    except:
        session['gold'] = 0
        print "=== no session gold, set to 0 ==="
        return


@app.route('/')
def mainpage():
    return render_template('ninjagold.html')



@app.route('/process_money', methods=['post'])
def processmoney():
    print "35=== Got Form Post: ===", request.form
    #check if they have any gold
    hasgold()
    currgold = 0
    print "39===Gold was ", session['gold']
    if request.form.get('action') == "farm":
        #add 10 to 20 gold
        print "41=== Detected farm activity ==="
        earnings = getrandomnum(10, 20)
        currgold = currgold + earnings
    elif request.form.get['action'] == "cave":
        #add 5 to 10 fold
        print "=== Request Form: ", request.form
        earnings = getrandomnum(5, 10)
        currgold = currgold +  earnings
    elif request.form.get['action'] == "house":
        #add 2 to 5 gold
        print "=== Request Form: ", request.form
        earnings = getrandomnum(2, 5)
        currgold = currgold +  earnings
    elif request.form.get['action'] == "casino":
        #add -50 to 50 gold
        print "=== Request Form: ", request.form
        earnings = getrandomnum(-50, 50)
        currgold = currgold +  earnings
    print "You earned ", earnings
    print "Gold is now", currgold
    session['gold'] = currgold
    return redirect('/')



app.run(debug=True)
