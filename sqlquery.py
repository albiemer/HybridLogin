
import sqlite3


def loginquery(uname, pword):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("select * from user where Username=(?) and Password=(?)", (uname, pword))
    result = c.fetchone()
    
    if result[3] == uname and result[5] == pword:
        return result[3], result[5]

#a, b = loginquery('albiemer', 'albi3mer')

#print(b)