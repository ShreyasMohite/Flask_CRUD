from flask import Flask,render_template,redirect,flash,url_for,request,flash

from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SECRET_KEY"]="3UHJENDCASDO2IKJEBNHDC"
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:''@localhost/testdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)


class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

    def __init__(self,name,email):
        self.name=name
        self.email=email


@app.route("/",methods=['GET','POST'])
def Add_User():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']

        mydata=Data(name,email)
        db.session.add(mydata)
        db.session.commit()
        flash("User Added succesfully")

        return redirect(url_for('Add_User'))

    return render_template("home.html",title="Home")

@app.route("/user")
def View_User():
    all_data=Data.query.all()
    
    return render_template("user.html",title="Home",user=all_data)



#@app.route("/user/edit/<id>",methods=["GET","POST"])
#def Edit_User(id):
#    user = Data.query.filter_by(id=id).first_or_404()
#    if request.method=="POST":
#        user.name=request.form['name']
#        user.email=request.form['email']
#        db.session.commit()
#        return redirect(url_for('View_User'))


       
#    return render_template('Select.html', user=user)
    
  
    




 

@app.route("/user/update/<id>",methods=["GET",'POST'])
def Update_User(id):
    #user = Data.query.filter_by(id=id).first_or_404()
    user=Data.query.get(id)
    if request.method=="POST":
        user.name=request.form['name']
        user.email=request.form['email']
        db.session.commit()
        flash("User updated succesfully")


        return redirect(url_for('View_User'))

    return render_template('Update.html',user=user)

    
    

    
        

   
    
    

    
        
    
    



@app.route("/user/delete/<id>",methods=["GET","POST"])
def Delete_User(id):
    my_datas=Data.query.get(id)
    db.session.delete(my_datas)
    db.session.commit()
    flash("User Deleted succesfully")
    return redirect(url_for("View_User"))


if __name__ == "__main__":
    app.run(debug=True)