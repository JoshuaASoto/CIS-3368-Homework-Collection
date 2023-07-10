import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#creating connection to mysql database
conn = create_connection("cis3368.c46eqokjvltp.us-east-2.rds.amazonaws.com", "admin", "Technologic7!", "CIS3368Fall2021")

app = flask.Flask(__name__) #Sets up application
app.config["DEBUG"] = True #Allows showning of errors


#Standard GET api, pulls entire zoo table and displays in JSON format to look better
@app.route('/api/animal', methods=['GET'])
def get_animal():
    if request.methods == 'GET':
        view_query = "SELECT * FROM zoo"
        view_dict = execute_read_query(conn,view_query)
        results = []
        for x in view_dict:
            results.append(x)
        return jsonify(results)
    else:
        
        return('View animals failed')


#JSON post method into zoo, uses MAX() sql function to newly created id to insert into log table, comment uses value from postamnimal sinc ethere is no reason to have to call it
@app.route('/api/animal', methods=['POST'])
def post_animal():
    request_data = request.get_json()
    postanimal = request_data['animal']
    postgender = request_data['gender']
    postsub = request_data['subtype']
    postage = request_data['age']
    postcolor = request_data['color']
    if request.method == 'POST':

        postquery = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES ('%s','%s','%s',%s,'%s')" % (postanimal, postgender, postsub, postage, postcolor)
        postlog = "INSERT INTO logs (animalid, comment) VALUES ((SELECT MAX(id) FROM zoo), 'Added %s to zoo')" % (postanimal)
        execute_read_query(conn,postquery)
        execute_query(conn,postlog)

        return('Animal added')
    else:
        return('Animal addition failed')

 #PUT api updates data for a selected animal
@app.route('/api/animal', methods=['PUT'])
def put_animal():
    request_data_update = request.get_json()
    updateid = request_data_update['id']
    updateanimal = request_data_update['animal']
    updategender = request_data_update['gender']
    updatesub = request_data_update['subtype']
    updateage = request_data_update['age']
    updatecolor = request_data_update['color']

    if updateid and updateid and updateanimal and updategender and updatesub and updateage and updatecolor and request.method == 'PUT':
        query = """
        UPDATE zoo SET animal = '%s', gender = '%s', subtype = '%s', age = %s, color = '%s' WHERE id = %s  """ % (updateanimal,updategender,updatesub,updateage,updatecolor, updateid)
        execute_query(conn,query)
        return('Success! Animal updated.')
    else:
        return('Sorry, failed to update animal.')



#DELETE api based on id, log message is created first due to it being uncallable after being deleted, message in logs notes deletion but no other characteristics.
@app.route('/api/animal/<int:id>', methods=['DELETE'])
def del_animal(id):
    if request.method == 'DELETE':
        logquery = "INSERT INTO logs (animalid, comment) VALUES (%s,'Deleted from zoo')" % (id)
        delete_query = "DELETE FROM zoo WHERE id =%s" %(id)
        execute_query(conn,logquery)
        execute_query(conn,delete_query)
        return('Success! Animal deleted')
    else:
        return('Sorry, Failded to delete animal')

#Simple GET api to view log table
@app.route('/api/logs', methods=['GET'])
def view_logs():
    if request.method == 'GET':
        view_loq_query = "SELECT * FROM logs"
        log_dict = execute_read_query(conn,view_loq_query)
        results = []
        for x in log_dict:
            results.append(x)
        return jsonify(results)
    else:
        return('Select proper api method')




#https://linuxtut.com/en/fcd4570743f1445a443a/
#https://www.youtube.com/watch?v=MF75aNH3Gjs
# @app.route('/api/logs', methods=['DELETE'])
# def reset_logs():
#     choice = request.args['reset'] 

#     for x in resetValue: #loop over all users and find one that is authorized to access
#         if x['reset'] == choice : #found an authorized user
#             reset_logs = "DELETE * FROM logs"
#             execute_query(conn,reset_logs)
#             return('Wrong Trigger Choice')
app.run()