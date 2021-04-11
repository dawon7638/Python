from flask import Flask, render_template
app = Flask(__name__) 


@app.route("/")
def play():
    return render_template("index.html")
print("*" * 87)

@app.route("/play/<times>")


def playSeven(times):
    return render_template("level2.html", num_times = int(times))
print("*" * 87)

@app.route("/play/<times>/<color>")
def playSeven2(times, color):
    return render_template("level3.html", num_times = int(times), color = color)
print("*" * 87)



if __name__=="__main__":    
    app.run(debug=True)
    