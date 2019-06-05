
from flask import render_template, request, redirect, url_for
from app import app, db, db1
#from app.schemas.post import Posts, Users
from app.models.modeldb import Model
from app.models.validaciones import Validar
#from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def index():
    titulo = "Home!"
    urlrev = "http://127.0.0.1:5000/registro"
    lista = ["footer", "header", "info"]
   
    print(titulo)
    #urlrev = titulo
    #print(urlrev)
    return render_template("index.html", titulo=titulo, lista=lista, url = urlrev)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/insert/default")
def insert_default():
    
    #new_post = Posts(title="Default Title")
    #db.session.add(new_post)
    #db.session.commit()
    
    return "The default post was created."

@app.route("/select/default")
def select_default():
    #post = Posts.query.filter_by(id=1).first()

    #print(post.title)

    return "Query done."

@app.route("/singup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        id = None
        nick = request.form['nick']
        nombre = request.form['name']
        email = request.form['Email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        password = request.form['password']
        passwordc = request.form['passwordc']
        
        Insert_users= dict()
        Insert_users= {'TABLE':'users', 
            'Col1':'id',
            'Col2':'nick',
            'Col3':'nombre',
            'Col4':'email',
            'Col5':'direccion',
            'Col6':'telefono',
            'Col7':'password',
            'Col8':'salt',
            'Val9':'%s',
            'Val10':'%s',
            'Val11':'%s',
            'Val12':'%s',
            'Val13':'%s',
            'Val14':'%s',
            'Val15':'%s',
            'Val16':'%s'
        }
        Inst_TUsers= Model(Insert_users)
        sql = Inst_TUsers.IT_TABLE()
        hash= Validar()
        pass_hash=[]
        pass_hash=hash.hash_password(password)   
        salt=pass_hash[0]
        password_hash=pass_hash[1]
        #h2=hash.check_password(myhash1, password)
        #sql = "INSERT INTO equipos (id, id_liga, nombre, ciudad, estado) VALUES (%s, %s, %s,  %s,  %s);"
        cursor = db1.cursor()
        cursor.execute(sql, (id, nick , nombre, email, direccion, telefono,password_hash,salt))
        cursor.close()
        db1.commit()
        #hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        #new_user = Users(user = request.form["user"], Email = request.form["Email"], username=request.form["name"], password=hashed_pw)
        #db.session.add(new_user)
        #db.session.commit()
        #return "You've registered successfully."
        return render_template("login.html")

    

@app.route("/validar", methods=["GET", "POST"])
def validar():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
    TSWusers = dict()
    TSWusers = {'TABLE':'users', 
        'Col1':'nick',
        'Col2':'password',
        'Col3':'salt',
        'Whe4':'nick=%s'
        }
    TUsers= Model(TSWusers)
    sql = TUsers.SW_TABLE()
    cursor = db1.cursor()
    cursor.execute(sql, (username))
    DatosUsers = cursor.fetchall()
    password_userbd = DatosUsers[0]['password']
    salt_userbd = DatosUsers[0]['salt']
    #print (r)     
    hash= Validar()
    #myhash=[]
    #myhash=hash.hash_password(password)   
    #salt=myhash[0]
    #myhash1=myhash[1]
    h2=hash.check_password(password_userbd, password, salt_userbd)  
    if h2:
        g="Son iguales"
    else:
        g = "Son diferentes"
    return g

    

@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render_template("registro.html")