from flask import Flask, render_template 
app = Flask(__name__)   









 
@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
       {'name' : 'Michael', 'lname' : 'Choi', 'flname' : 'Michael Choi'},
       {'name' : 'John', 'lname' : 'Supsupin', 'flname' : 'John Supsupin'},
       {'name' : 'Mark', 'lname' : 'Guillen', 'flname' : 'Mark Guillen'}
    ]
    return render_template("index.html", users = users,)













if __name__=="__main__":
    app.run(debug=True)    
