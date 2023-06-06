import json
import mariadb
import dbcreds


from flask import Flask
app = Flask(__name__)

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

def close_all():
    if(cursor != None):
        cursor.close()
    if(conn != None):
        conn.close()

@app.get('/api/books')
def get_api_books():
    cursor.execute('CALL get_all_books')
    results=cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return 'something went wrong'
    
@app.get('/api/books_authored')
def get_api_auth_count():
    cursor.execute('CALL get_auth_count')
    results=cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return 'something went wrong'
    
@app.get('/api/best_selling_book')
def get_api_auth_count():
    cursor.execute('CALL get_most_sold')
    results=cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return 'something went wrong'
    
@app.get('/api/best_selling_author')
def get_api_auth_count():
    cursor.execute('CALL get_pop_auth')
    results=cursor.fetchall()
    if(type(results) == list):
        results_json = json.dumps(results,default=str)
        close_all()
        return(results_json)
    else:
        close_all()
        return 'something went wrong'
    
app.run(debug=True)

