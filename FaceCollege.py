from flask import Flask, render_template, flash, request, session
from flask import render_template, redirect, url_for, request
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
# from werkzeug.utils import secure_filename


import mysql.connector
import sys, fsdk, math, ctypes, time
import datetime

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')



@app.route("/rfid")
def rfid():
    return render_template('VerifyRfid.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)

        else:
            return render_template('index.html', error=error)


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AttendanceInfo")
def AttendanceInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM attentb")
    data = cur.fetchall()
    return render_template('AttendanceInfo.html', data=data)


@app.route("/NewStudent")
def NewStudent():
    import LiveRecognition  as liv

    liv.att()
    del sys.modules["LiveRecognition"]
    return render_template('NewStudent.html')


@app.route("/NewStudent1", methods=['GET', 'POST'])
def NewStudent1():
    if request.method == 'POST':
        regno = request.form['regno']
        name = request.form['name']
        gender = request.form['gender']
        Age = request.form['Age']
        email = request.form['email']
        pnumber = request.form['pnumber']
        address = request.form['address']
        Degree = request.form['Degree']
        depart = request.form['depart']
        year1 = request.form['year1']
        rfid = request.form['rfid']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('" + regno + "','" + name + "','" + gender + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + Degree + "','" + depart + "','" + year1 + "','" + rfid + "')")
        conn.commit()
        conn.close()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()

    return render_template("AdminHome.html", data=data)


@app.route("/AUserSearch", methods=['GET', 'POST'])
def AUserSearch():
    if request.method == 'POST':

        if request.form["submit"] == "Search":
            date = request.form['date']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM attentb where date='" + date + "'")
            data = cur.fetchall()

            return render_template('AttendanceInfo.html', data=data)

        elif request.form["submit"] == "Close":

            date = request.form['date']
            regtb = ''

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            cursor = conn.cursor()
            cursor.execute("select *  from regtb ")
            data = cursor.fetchall()
            for i in data:
                regtb = i[0]
                nn = i[1]
                print(i[0])
                Deg = i[7]
                Depar = i[8]
                Yea = i[9]
                smob = i[5]

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='1faceattendancedbrfid')
                cursor = conn.cursor()
                cursor.execute("select * from attentb where Date='" + str(date) + "' and Regno='" + str(regtb) + "'")
                data = cursor.fetchone()
                if data is None:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1faceattendancedbrfid')
                    cursor = conn.cursor()
                    cursor.execute(
                        "insert into attentb values('','" + str(date) + "','" + str(
                            timeStamp) + "','" + str(Deg) + "','" + str(Depar) + "','" + str(Yea) + "','" + str(
                            regtb) + "','0')")
                    conn.commit()
                    conn.close()
                    sendmsg(smob, "Your " + str(nn) + " Not attent college today")

            conn.close()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM attentb where date='" + date + "'")
            data = cur.fetchall()

            return render_template('AttendanceInfo.html', data=data)


global cregnumber
global crfid


@app.route("/searchid")
def searchid():
    # eid= request.args.get('eid')
    # session['eid']=eid

    id1 = 0
    id2 = 0
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cursor.execute("select Max(id) as id from attentb ")
    data = cursor.fetchall()
    for i in data:
        id1 = i[0]
        print(i[0])

    conn.close()

    examvales1()

    import LiveRecognition1  as liv1

    # liv1.examvales(cregnumber, crfid)

    # liv1.att()

    # print(ExamName)

    del sys.modules["LiveRecognition1"]

    # Fillattendances()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cursor.execute("select Max(id) as id from attentb ")
    data = cursor.fetchall()
    for i in data:
        id2 = i[0]
        print(i[0])

    conn.close()

    if id1 != id2:
        conn2 = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
        # cursor = conn.cursor()
        cur2 = conn2.cursor()
        cur2.execute("SELECT * FROM attentb where id='" + str(id2) + "'")
        data2 = cur2.fetchone()
        if data2:
            regnumber = data2[6]
            print(regnumber)

            conn3 = mysql.connector.connect(user='root', password='', host='localhost',
                                            database='1faceattendancedbrfid')
            cur3 = conn3.cursor()
            cur3.execute("SELECT * FROM regtb where 	Regno='" + str(regnumber) + "'")
            data3 = cur3.fetchone()
            if data3:
                stnumber = data3[5]
                nnn = data3[1]
                print(stnumber)
                sendmsg(stnumber, "Your " + str(nnn) + " attent college today")

        # return "Attendance Successfully Submitted"

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM attentb where id='" + str(id2) + "'")
        data1 = cur.fetchall()
        return render_template('Attendance.html', data=data1)


    else:
        # messagebox.showinfo("Unknow Face or User Not register or already  Attendance")
        return "Unknow Face or User Not register or Already Face Attendance Info Saved"


@app.route("/checkrfi", methods=['GET', 'POST'])
def checkrfi():
    if request.method == 'POST':
        rfid = request.form['rfid']
        session["rfid"] = rfid
        print(rfid)
        ''' import serial

                # Define your serial port settings
                port = 'COM4'  # Change this to your serial port, e.g., 'COM1' on Windows
                baudrate = 9600  # Change this to match your device's baud rate

                # Initialize the serial port
                ser = serial.Serial(port, baudrate)

                try:
                    while True:
                        # Read a line from the serial port
                        line = ser.readline().decode().strip()


                        # Print the received line
                        print(line)
                        session["rfid"] = int(line)
                        print(session["rfid"])

                        #if intline==1:
                        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                       database='1faceattendancedbrfid')
                        cursor = conn.cursor()
                        cursor.execute("SELECT * from regtb where RFID='" +  str(line)  + "' ")
                        data = cursor.fetchone()
                        if data is None:
                            alert = 'RFID Not Found!'
                            return render_template('goback.html', data=alert)
                        else:
                            print('OK')
                        return searchid()
                        ser.close()

                except KeyboardInterrupt:
                    # Close the serial port when KeyboardInterrupt is detected (Ctrl+C)
                    ser.close()'''
        return searchid()






def examvales1():
    rfid = session["rfid"]
    print(rfid)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM regtb where  RFID='" + str(rfid) + "'")
    data = cursor.fetchone()

    if data:
        cregnumber = data[0]
        crfid = data[10]
        print(crfid)


    else:
        return 'Incorrect username / password !'
    return cregnumber, crfid


@app.route("/appr")
def appr():
    cid = request.args.get('cid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cursor.execute(
        "delete from regtb where    regno='" + str(cid) + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)




@app.route("/StudentLogin")
def StudentLogin():
    return render_template('StudentLogin.html')



@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where Regno='" + username + "' and Name='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong...!")
            return render_template('StudentLogin.html')
        else:
            session['mob'] = data[2]
            session['add'] = data[4]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where Regno='" + username + "' and Name='" + password + "'")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('StudentHome.html', data=data)


@app.route("/StudentHome")
def StudentHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where Regno='"+ session['uname'] +"'")
    data = cur.fetchall()
    return render_template('StudentHome.html', data=data)


@app.route("/SAttendanceInfo")
def SAttendanceInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
    cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM attentb where Regno='"+ session['uname'] +"'")
    data = cur.fetchall()
    return render_template('SAttendanceInfo.html', data=data)



@app.route("/SUserSearch", methods=['GET', 'POST'])
def SUserSearch():
    if request.method == 'POST':

        if request.form["submit"] == "Search":
            date1 = request.form['date1']
            date2 = request.form['date2']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1faceattendancedbrfid')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM attentb where date between '" + date1 + "' and '"+ date2 +"' and Regno='"+ session['uname'] +"'")
            data = cur.fetchall()

            return render_template('SAttendanceInfo.html', data=data)



def sendmsg(targetno,message):
    import requests
    requests.post(
        "http://sms.creativepoint.in/api/push.json?apikey=6555c521622c1&route=transsms&sender=FSSMSS&mobileno=" + targetno + "&text=Dear customer your msg is " + message + "  Sent By FSMSG FSSMSS")


def sendmail(Mailid,message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
