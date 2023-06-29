from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def web():
    return render_template("/Webpage.html")
@app.route('/LoginPage')
def web():
    return render_template("/LoginPage.html")
if("__main__"==__name__):
    app.run()