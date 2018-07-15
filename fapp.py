from flask import Flask,render_template,request,redirect
from webYoutube import findLink
app=Flask(__name__)
@app.route('/')

def insex():
    return render_template('firstspp.html')


@app.route('/handle_data', methods=['POST'])

#songname=str()

def handle_data():
    projectpath = request.form['projectFilepath']
    songname=projectpath
    findLink(songname)
    return redirect('/')

if __name__=='__main__':
    app.run()

