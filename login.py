"""
1. This is the port that i preferably assinged
2. This is assigning for @route function
3. This is a secret key
4. mypos() function are the first function to initialize program to login form
"""
import webview
import threading
from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, abort
from ipconfig import myip
from note import login_note
from sqlquery import loginquery

#1
port = 5000

#2
posapp = Flask(__name__)

#3
posapp.secret_key = 'd08c92d50ae43bde171697297e3c9b11fcfdb90cb2f9ac24cd0ce9e69aff33ea'

#4
@posapp.route('/mypos')
def mypos():
    return render_template('Logintopos.html', myipaddress = myip.fullip(), note = login_note.note)

@posapp.route('/loginconfirm', methods = ['POST', 'GET'])
def loginconfirmfunc():
    if request.method == 'POST':
        myuser = request.form['u_ser']
        mypass = request.form['p_ass']
        try:
            a, b = loginquery(myuser, mypass)
            return render_template('show-ab.html', a = a, b = b)
        except:
            return render_template('Logintopos.html', myipaddress = myip.fullip(), note = login_note.note, note1 = login_note.loginfail())
 
@posapp.route('/exitlogin', methods = ['POST'])
def exitloginfunc():
    window.destroy()
 
def start_server():
    posapp.run(myip.ip, myip.port)

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    # This line is to launch program in hybrid platform
    window = webview.create_window("adeguin", 'http://192.168.1.2:5000/mypos', fullscreen=True, frameless=False)
    webview.start(mypos, window)
    print(myip.fullip())
    