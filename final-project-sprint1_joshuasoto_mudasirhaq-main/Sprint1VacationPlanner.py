import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import datetime
import time
import hashlib
#User logs in, can create a new vacation or view exisitng ones

#User should be able to add, edit and delete destinations

#Add or Edit: User should choose among the seperately setup destinations

#Date Format is Year-Month-Date ie. 2022-02-23
#Dates are double quoted when inserted into sql ie. values(int,'String',"Date") | values(2,'Apple', "2010-12-25")
#Dates in JSON are quoted just like strings


#Setting up application name
app = flask.Flask(__name__) #Sets up application
app.config["DEBUG"] = True #Allows shownog of errors

#password 'password' hashed
masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
masterusername = 'username'

#creating connection to mysql database
conn = create_connection("cis3368.c46eqokjvltp.us-east-2.rds.amazonaws.com", "admin", "Technologic7!", "CIS3368Fall2021")

# ---------------------------------------------------------------------------------------------------------------

# ADD DESTINATION

@app.route('/api/adddestination', methods=['POST'])
def addDest():
    # destination to be added gets entered in postman payload as json format 
    request_data_adddest = request.get_json()
    newcountry = request_data_adddest['country']
    newcity = request_data_adddest['city']
    newsight = request_data_adddest['sightseeing']

    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #if login is successful, a new destination is added with a new country, new city, and new sightseeing values
    query_adddest = "INSERT INTO destination(country,city,sightseeing) VALUES ('%s','%s','%s')" % (newcountry, newcity, newsight)
    execute_query(conn,query_adddest)
    return('Success! Destination added.')
    # return('Sorry, failed to add destination.')
    
# ---------------------------------------------------------------------------------------------------------------

# DELETE DESTINATION

#Delete destination based around ID
#Front end could show the table to allow users to know which destination has what id, will try to implememt into sprint 2

# user enters the id in api url to delete the specific row
@app.route('/api/deletedestination/<int:id>',methods=['DELETE'])
def deleteDest(id):
    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #sql statement is best suited for deleting a specific row with id mentioned in the API URL, granted the user login is successful
            query_deletedest = "DELETE from destination WHERE id=%s" % (id)
            execute_query(conn,query_deletedest)
            return('Success! Destination deleted.')
    # return('Sorry, failed to delete destination.')

# ---------------------------------------------------------------------------------------------------------------

# EDIT/UPDATE DESTINATION

# user selects which id they want to update without entering id in the url
@app.route('/api/updatedestination', methods=['POST'])
def updateDest():
    # destination to be updated gets entered in postman payload as json format
    request_data_updatedest = request.get_json()
    updatedestid = request_data_updatedest['id']
    updatecountry = request_data_updatedest['country']
    updatecity = request_data_updatedest['city']
    updatesight = request_data_updatedest['sightseeing']


    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #triple quote sql query method used for the specific case of updating the destination table without entering the ID in API URL
    query = """
    UPDATE destination SET country = '%s', city = '%s', sightseeing = '%s' WHERE ID = %s """ % (updatecountry, updatecity, updatesight, updatedestid)
    execute_query(conn,query)
    return('Success! Destination updated.')
    # return('Sorry, failed to update destination.')

# ---------------------------------------------------------------------------------------------------------------

# ADD TRIP

# user enters additional destinationid, transportation, start and end dates into postman directly rather than entering id in the api url
@app.route('/api/addtrip', methods=['POST'])
def addTrip():
    # trip to be added gets entered in postman payload as json format
    request_data_addtrip = request.get_json()
    #variables for each column to be added to the trip table are created and imported in JSON format
    newdestinationid = request_data_addtrip['destinationid']
    newtransportation = request_data_addtrip['transportation']
    newstartdate = request_data_addtrip['startdate']
    newenddate = request_data_addtrip['enddate']
    newtripname = request_data_addtrip['tripname']

    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #trip is only added if login is successful, sql formatting is valid as id is an integer, so it doesn't need apostrophes around the percent value in sql statement
    query = "INSERT INTO trip(destinationid,transportation,startdate,enddate,tripname) VALUES (%s,'%s','%s','%s','%s')" % (newdestinationid, newtransportation, newstartdate, newenddate,newtripname)
    execute_query(conn,query)
    return('Success! Trip added.')
        # return('Sorry, failed to add trip.')
#     dict = execute_query(conn,query)
# for x in dict:
#             print(x)
#         print()
        
# ---------------------------------------------------------------------------------------------------------------

# DELETE TRIP

@app.route('/api/deletetrip/<int:id>',methods=['DELETE'])
def deleteTrip(id):
    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #deletes record from the trip table based on the id entered in the API URL. must remove arrow brackets around the ID entered in API URL to succesfully execute
            query = "DELETE from trip WHERE id=%s" % (id)
            execute_query(conn,query)
            return('Success! Trip deleted.')
    # return('Sorry, failed to delete trip.')

# ---------------------------------------------------------------------------------------------------------------

# EDIT/UPDATE TRIP


@app.route('/api/updatetrip', methods=['POST'])
def update_trip():
    # trip to be updated gets entered in postman payload as json format
    request_data_update = request.get_json()
    updateid = request_data_update['id']
    updatedestid = request_data_update['destinationid']
    updatetransport = request_data_update['transportation']
    updatestartdate = request_data_update['startdate']
    updateenddate = request_data_update['enddate']
    updatetripname = request_data_update['tripname']

    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
    query = " UPDATE trip SET destinationid = %s, transportation = '%s', startdate = '%s', enddate = '%s', tripname = '%s' WHERE id = %s  " % (updatedestid, updatetransport, updatestartdate, updateenddate, updatetripname, updateid)
    execute_query(conn,query)
    return('Success! Trip updated.')
    # return('Sorry, failed to update trip.')



# ---------------------------------------------------------------------------------------------------------------

#Create vacation
#Show destination table
#Just like adddestination code wise

# VIEW TRIP
#Simple get method
@app.route('/api/viewtrip',methods=['GET'])
def view_trip():
    # if request.authorization:
        #password for login implementation
        # encoded=request.authorization.password.encode() #unicode encoding
        # hashedResult = hashlib.sha256(encoded) #hashing
        #username implementation for user login
        # if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #displays trip to the user in dictionary only if username and password login is successful
            
            query = "SELECT * FROM trip" 
            trip_dict = execute_read_query(conn,query)
            results = []
            for x in trip_dict:
                results.append(x)
            return jsonify(results)
  


# VIEW Destination
#Simple get method
@app.route('/api/viewdestination',methods=['GET'])
def view_dest():
    # if request.authorization:
    #     encoded=request.authorization.password.encode() #unicode encoding
    #     hashedResult = hashlib.sha256(encoded) #hashing
    #     if request.authorization.username == 'username'and hashedResult.hexdigest() == masterPassword:
            #displays destination to the user in dictionary only if username and password login is successful
            query = "SELECT * FROM destination" 
            dest_dict = execute_read_query(conn,query)
            results = []
            for x in dest_dict:
                results.append(x)
            return jsonify(results)
    # return('Destination view failed')
    

app.run()
