from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session


app = Flask(__name__)
SECRET = "4D1MiN_10V3_Y0u"
flag = "FLAG{cOOkI3_witH0uT_seCr37_No7_G00D}"
app.secret_key = SECRET
@app.route("/")
def index():
    if 'want_flag' in session:
        if session['want_flag']==1:
            if session.modified == False:
                return flag
            else:
                return 'Cheating detected' 
        else:
            return f'Hello, i need check something... \n You dont want a flag!!! \n Tip: i heard about secrets {SECRET}'
    else:
        session['want_flag']=0
        return f'Hello, i need check something... \n You dont want a flag!!! \n Tip: i heard about secrets {SECRET}' 

if __name__=="__main__":
    app.run(host='0.0.0.0')