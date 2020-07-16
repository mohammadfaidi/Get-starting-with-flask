from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("home.html")





@app.route('/bye')
def bye():
    return 'Hello bye'




@app.route('/nablus')
def nablus2():
    return render_template("nablus.html")


if __name__ =='__main__':
    app.run(debug=True)
