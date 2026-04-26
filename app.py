# from flask import Flask,request,redirect,url_for,render_template
# from database import get_db_connection

# app = Flask(__name__)

# @app.route("/")

# def index():
#     connection = get_db_connection()
#     student_data = connection.execute("select * from students")
#     return render_template("index.html",students=student_data)
    
# @app.route("/add", methods=["GET","POST"])
# def add_student():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         course = request.form["email"]

#         connection = get_db_connection()
#         connection.execute ("""
#                         INSERT INTO students(name,email,course)values(?,?,?)'(name,email,course)
#                             """)
        
#         connection.commit()
#         connection.close()

#         return redirect("/")
#     return render_template("add_student.html")
# @app.route("/delete/<int:id>")

# def delete_student(id):
#     connection = get_db_connection()

#     connection.execute("DELETE from students where id=?",(id,))
#     connection.commit()
#     connection.close()

#     return redirect("/")

# # @app.route("/home")

# # def home():

# #     return "<h1>Home</h1>"
# # @app.route("/json")

# # def json():

# #     return {"mykey":"JSON Data","mylist":[1,2,3,4,5]}

# # @app.route("/dynamic/<user_input>")

# # def dynamic(user_input):

# #     return f"<h1> The user entered : {user_input}</h1>"

# # @app.route("/query")

# # def query():

# #     hello = request.args.get("hello")
# #     world = request.args.get("world")
# #     return f"<h1> The query string contains : {hello} and {world} </h1>"
# # @app.route("/login",methods=["GET","POST"])

# # def login():
# #     if request.method == "POST":
# #         username = request.form.get("username")
# #         if username:
# #             return redirect(url_for("home"))
        
# #     return """
# #     <H1> Login Page </H1>
# #     <form method="POST">
# #         <input type="text" name="username" placeholder="enter username">
# #         <button type="submit">Login</button>
# #     </form>
# #     """

# if __name__ == "__name__":
#     app.run(debug=True)


# from flask import Flask,render_template, request, redirect

# from database import get_db_connection

# app = Flask(__name__)

# @app.route("/")

# def index():

#     connection = get_db_connection()

#     students_data = connection.execute(

#         "SELECT * FROM students"

#     ).fetchall()

#     connection.close()

#     return render_template("index.html",students=students_data)

 

# @app.route("/add",methods = ["GET","POST"])

# def add_student():

#     if request.method == "POST":

#         name = request.form["name"]

#         email = request.form["email"]

#         course = request.form["course"]

#         connection = get_db_connection()

#         connection.execute(

#             "INSERT INTO students (name,email,course) values (?,?,?)",

#             (name,email,course)

#         )

#         connection.commit()

#         connection.close()

#         return redirect("/")

#     return render_template("add_student.html")

 

# @app.route("/delete/<int:id>")

# def delete_student(id):

#     connection = get_db_connection()

#     connection.execute(

#         "DELETE FROM students where id = ?",(id,)

#     )

#     connection.commit()

#     connection.close

#     return redirect("/")

# if __name__ == "__main__":

#     app.run(debug=True)
from flask import Flask,request, redirect ,url_for , render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite3"

db=SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(100))

    date_joined = db.Column(db.DateTime)

@app.route("/")

def home():

    return "Flask Running"

if  __name__ =="__main__":

    app.run(debug=True)