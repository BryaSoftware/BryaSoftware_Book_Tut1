from books import Books
from dbconfig import app
from flask_restful import Api

@app.route("/")
def index():
    name = "www.bryasoftware.com"
    return name

api = Api(app)
#URL Extension
api.add_resource(Books, '/Books')

if __name__ == '__main__':
    #host and port can be changed to your environment
    app.run(debug=False, port= 5000, host='localhost')