# import sys
# print("Script Name:", sys.argv[0])
# print("Script Argument1:", sys.argv[1])
# print("Script Argument2:", sys.argv[2])

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    fruits = ["Apple", "Banana", "Cherry"]
    return render_template("home.html",name='Anjali',fruits=fruits)
if __name__=="__main__":
    app.run(debug=True)
