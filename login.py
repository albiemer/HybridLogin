"""

2. This is assigning for @route function
3. This is a secret key
4. mypos() function are the first function to initialize program to login form
5. The loginconfirmfunc() function are the function to validate and to confirm the
    entry record if existed in database
6. The exitloginfunc() is a function to exit from the program.
7. The start_server() is the function to start server in multi thread program  
"""


import webview
import threading
from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, abort
from ipconfig import myip
from note import login_note
from sqlquery import loginquery


#2
posapp = Flask(__name__)

#3
posapp.secret_key = 'd08c92d50ae43bde171697297e3c9b11fcfdb90cb2f9ac24cd0ce9e69aff33ea'

#4
@posapp.route('/mypos')
def mypos():
    return render_template('Logintopos.html', myipaddress = myip.fullip(), note = login_note.note)

#5
@posapp.route('/loginconfirm', methods = ['POST', 'GET'])
def loginconfirmfunc():
    if request.method == 'POST':
        myuser = request.form['u_ser']
        mypass = request.form['p_ass']
        userlog = loginquery(myuser, mypass)
        if(userlog):
            if userlog[3] == myuser and userlog[5] == mypass:
                return render_template('show-ab.html', a = userlog[3], b = userlog[5])
        
        else:
            return render_template('Logintopos.html', myipaddress = myip.fullip(), note = login_note.note, note1 = login_note.loginfail())

#6
@posapp.route('/exitlogin', methods = ['POST'])
def exitloginfunc():
    window.destroy()

#7
def start_server():
    posapp.run(myip.ip, myip.port)

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    # This line is to launch program in hybrid platform
    window = webview.create_window("adeguin", 'http://'+myip.fullip()+'/mypos', fullscreen=True, frameless=False)
    webview.start(mypos, window)
    print(myip.fullip())
    