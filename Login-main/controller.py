from flask import render_template,request,redirect,url_for,jsonify,session,flash
import re
import sys
from config import app,db,mycursor
from flask.wrappers import Request
#from models import login_details

global email
global f_name
global l_name
global list_events
global list_flagships
global list_workshops
global list_papers

list_events = []
list_flagships = []
list_workshops = []
list_papers = []

'''email = " "
f_name = " "
l_name = " " '''

@app.route("/")
def home():
   return render_template("main.html")

@app.route("/index", methods = ['POST','GET'])
def home1():
   if request.method == 'GET':
       list_event = db.session.execute("select * from event_table")
       list_event = list_event.fetchall()
       for i in range(6):
              list_events.append(list_event[i][0])
       
       list_flagship = db.session.execute("select * from flagshipevent_table")
       list_flagship = list_flagship.fetchall()
       for i in range(5):
              list_flagships.append(list_flagship[i][0])
       
       list_workshop = db.session.execute("select * from workshop_table")
       list_workshop = list_workshop.fetchall()
       for i in range(8):
              list_workshops.append(list_workshop[i][0])

       list_paper = db.session.execute("select * from paperpresentation_table")
       list_paper = list_paper.fetchall()
       for i in range(5):
              list_papers.append(list_paper[i][0])
       
       print(list_events)
       print(list_events[0])
       return render_template("index.html", list_events = list_events)
   elif request.method == 'POST':
       return render_template("index.html")

@app.route("/afterlogin", methods = ['POST','GET'])
def afterlogin():
       if request.method == 'GET':
              return render_template("afterlogin.html")
            
            
@app.route("/signup",methods = ['POST','GET'] )
def about():
       if request.method== 'GET':
              return render_template("login.html")
       elif request.method== 'POST':
              p1 = request.form.get('fname')
              global f_name
              f_name = p1
              
              p2 = request.form.get('lname')
              global l_name
              l_name = p2
              
              p3 = request.form.get('email')
              global email
              email = p3
              
              p4 = request.form.get('gen')
              p5 = request.form.get('clg')
              p6 = request.form.get('number')
              p7 = request.form.get('pswd')
              #obj1 = user_table(p1,p2,p3,p4,p5,p6)
              #db.session.add(obj1)
              #print(obj1,p1,p2,p3,p4,p5,p6,p7)
              db.session.execute("insert into user_table(f_name,l_name,email,gender,college,mobile_number) values('{}','{}','{}','{}','{}','{}')".format(p1,p2,p3,p4,p5,p6))
              db.session.commit()
              #obj2 = login_details(p3,p7)
              #db.session.add(obj2)
              db.session.execute("insert into login_details values('{}','{}')".format(p3,p7))
              db.session.commit()
              return redirect(url_for('home1'))

@app.route("/loginuser",methods = ['POST','GET'] )
def userlogin():
       error = None
       if request.method== 'GET':
              return render_template("login.html")
       elif request.method== 'POST':
              p1 =request.form.get('email')
              p2 = request.form.get('pswd')
              global email
              email = p1
              res = db.session.execute("select user_mail, user_password from login_details where user_mail = '{}'".format(p1))
              res = res.fetchall()[0][0]
              
              res1 = db.session.execute("select user_password from login_details where user_mail = '{}'".format(p1))
              res1 = res1.fetchall()[0][0]
              
              f_name_res = db.session.execute("select f_name from user_table where email = '{}'".format(p1))
              global f_name
              f_name = f_name_res.fetchall()[0][0]
              
              l_name_res = db.session.execute("select l_name from user_table where email = '{}'".format(p1))
              global l_name
              l_name = l_name_res.fetchall()[0][0]
              
              #print(f_name, l_name)
              print(res1,p2)
              
              if res == p1:
                     if res1 == p2:
                            return render_template("afterlogin.html",list_events = list_events)
                     else:
                            flash("INVALID EMAIL ID/PASSWORD")
                            return render_template("login.html")

@app.route("/registerevent", methods = ['POST','GET'])
def eventregister():
       if request.method == 'GET':
              return render_template("registerevent.html",f_name = f_name,l_name = l_name,email = email,list_events = list_events)
       elif request.method == 'POST':
              option = request.form.get('event')
              print(type(option))
              op = db.session.execute("select email from event_register where event_name = '{}'".format(option))
              op = op.fetchall()
              print(op)
              if(len(op) == 0):
                     print("empty")
                     db.session.execute("insert into event_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              elif((email,) not in op):
                     print(str(email))
                     db.session.execute("insert into event_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              else:
                     flash("Already Registered in " + option)
                     return render_template("registerevent.html",f_name = f_name,l_name = l_name,email = email,list_events = list_events)

@app.route("/registerflagshipevent", methods = ['POST','GET'])
def flagshipeventregister():
       if request.method == 'GET':
              return render_template("registerflagship.html",f_name = f_name,l_name = l_name,email = email,list_flagships = list_flagships)
       elif request.method == 'POST':
              option = request.form.get('flagship')
              print(type(option))
              op = db.session.execute("select email from flagshipevent_register where event_name = '{}'".format(option))
              op = op.fetchall()
              print(op)
              if(len(op) == 0):
                     print("empty")
                     db.session.execute("insert into flagshipevent_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              elif((email,) not in op):
                     db.session.execute("insert into flagshipevent_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              else:
                     flash("Already Registered in " + option)
                     return render_template("registerflagship.html",f_name = f_name,l_name = l_name,email = email,list_flagships = list_flagships)

@app.route("/registerworkshop", methods = ['POST','GET'])
def workshopregister():
       if request.method == 'GET':
              return render_template("registerworkshop.html",f_name = f_name,l_name = l_name,email = email,list_workshops = list_workshops)
       elif request.method == 'POST':
              option = request.form.get('workshop')
              print(type(option))
              op = db.session.execute("select email from workshop_register where event_name = '{}'".format(option))
              op = op.fetchall()
              print(op)
              if(len(op) == 0):
                     print("empty")
                     db.session.execute("insert into workshop_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              elif((email,) not in op):
                     db.session.execute("insert into workshop_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              else:
                     flash("Already Registered in " + option)
                     return render_template("registerworkshop.html",f_name = f_name,l_name = l_name,email = email,list_workshops = list_workshops)

@app.route("/registerpaperpresentation", methods = ['POST','GET'])
def paperpresentationregister():
       if request.method == 'GET':
              return render_template("registerpaper.html",f_name = f_name,l_name = l_name,email = email,list_papers = list_papers)
       elif request.method == 'POST':
              option = request.form.get('paper')
              print(type(option))
              op = db.session.execute("select email from paperpresentation_register where event_name = '{}'".format(option))
              op = op.fetchall()
              print(op)
              if(len(op) == 0):
                     print("empty")
                     db.session.execute("insert into paperpresentation_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              elif((email,) not in op):
                     db.session.execute("insert into paperpresentation_register(email,f_name,l_name,event_name) values('{}','{}','{}','{}')".format(email,f_name,l_name,option))
                     db.session.commit()
                     return render_template("afterlogin.html",list_events = list_events)
              else:
                     flash("Already Registered in " + option)
                     return render_template("registerworkshop.html",f_name = f_name,l_name = l_name,email = email,list_papers = list_papers)

@app.route("/dashboard", methods = ['POST','GET'])
def dashboard():
       if request.method == 'GET':
              user_events = []
              user_event = db.session.execute("select event_name from event_register where email = '{}' order by event_name ASC".format(email))
              user_event = user_event.fetchall()
              for i in range(len(user_event)):
                     user_events.append(user_event[i][0])

              user_flagships = []
              user_flagship = db.session.execute("select event_name from flagshipevent_register where email = '{}' order by event_name ASC".format(email))
              user_flagship = user_flagship.fetchall()
              for i in range(len(user_flagship)):
                     user_flagships.append(user_flagship[i][0])

              user_workshops = []
              user_workshop = db.session.execute("select event_name from workshop_register where email = '{}' order by event_name ASC".format(email))
              user_workshop = user_workshop.fetchall()
              for i in range(len(user_workshop)):
                     user_workshops.append(user_workshop[i][0])

              user_papers = []
              user_paper = db.session.execute("select event_name from paperpresentation_register where email = '{}' order by event_name ASC".format(email))
              user_paper = user_paper.fetchall()
              for i in range(len(user_paper)):
                     user_papers.append(user_paper[i][0])
              
              return render_template("dashboard.html",f_name = f_name, l_name = l_name,user_events = user_events,user_flagships = user_flagships,user_workshops = user_workshops, user_papers = user_papers)

if __name__ == '__main__':
       app.run(debug = True)