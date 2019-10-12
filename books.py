from flask_restful import Resource, Api, reqparse
from dbconfig import mysql
from flask import jsonify

class Books(Resource):
    #for this tutorial we will only be setting up Get Requests
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            #Execute SQL
            cursor.execute('SELECT * FROM books')
            #Dictionary object to contain headername
            bookResults = [dict((cursor.description[i][0], value)for i, value in enumerate(row)) for row in cursor.fetchall()]

            print (bookResults)
            return jsonify(bookResults)
        except Exception as e:
            return {'error': str(e)}