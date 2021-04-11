from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
print("*" * 87)

@app.route("/dojo")
def dojo_one():
    return "Dojo!"
print("*" * 87)

@app.route("/say/<name>")
def multi_person(name):
    return f"Hi {name}!"
print("*" * 87)

@app.route("/repeat/<greeting>/<int:num_times>")
def multi_person2(greeting, num_times):
    return f"{greeting}" * num_times  
print("*" * 87)







    

if __name__=="__main__":    
    app.run(debug=True)

