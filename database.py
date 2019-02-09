from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)

#config
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="password123"
app.config["MYSQL_DB"]="connection_flask_db"

#inizializzazione della connessione con il db
mysql=MySQL(app)


@app.route("/")
def index():
    cur=mysql.connection.cursor()
    cur.execute("select data from example where id =5")
    result=cur.fetchall()
    return str(result)

@app.route("/addone/<string:insert>")
def add(insert):
    cur=mysql.connection.cursor()
    cur.execute("select max(id) from example")
    maxid=cur.fetchone()   #ci torna una tupla (5,hello)
    cur.execute("insert into example(id,data) values(%s,%s)",(maxid[0]+1,insert))
    mysql.connection.commit()
    return "Done"

@app.route("/getall")
def getall():
    cur=mysql.connection.cursor()
    cur.execute("select * from example")
    return_values=cur.fetchall() #torna tutto quindi una tupla di tuple
    print_this=""
    for i in return_values:
        print_this+=str(i)+"<br>"
    return print_this







if __name__=="__main__":
    app.run(debug=True)