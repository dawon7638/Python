from flask import Flask, render_template
app = Flask(__name__) 




@app.route("/")
def checkerboard1():
    return render_template("index.html")
print("*" * 87)

@app.route("/<times>")
def checkerboard2(times):
    return render_template("index2.html", num_times = int(times))
print("*" * 87)

@app.route("/<x>/<y>")
def checkerboard3(x, y ):
    return render_template("index3.html", x = int(x), y = int(y))
print("*" * 87)





if __name__=="__main__":    
    app.run(debug=True)
    