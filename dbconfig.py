from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
CORS(app)

#Here we set our DB Connect configs
app.config['MYSQL_DATABASE_USER'] = 'bookBoss' # for this example we're using the user from another MySQL Tutorial, but replace bookboss with a user from your DB Connection if have existing installation
app.config['MYSQL_DATABASE_PASSWORD'] = 'BryaSoftware_Book123' #Again we're using a previously provided password, change according to your setup
app.config['MYSQL_DATABASE_DB'] = 'MyBookDB' #Provide Database name, in previous tutorial we created MyBookDB database in MYSQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #this can be either localhost, or a ip ie 192.133.33.33

mysql.init_app(app)