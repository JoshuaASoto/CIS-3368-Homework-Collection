import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query


#creating connection to mysql database
conn = create_connection("cis3368.c46eqokjvltp.us-east-2.rds.amazonaws.com", "admin", "Technologic7!", "CIS3368Fall2021")

#Menu is compact and seperated by rows, if value entered is not an option menu is printed again
option = ''

while option.upper() != 'Q':


    print('\nMENU\na - Add car\nd - Remove car\nu - Update car details\nr1 - Output all cars sorted by year(ascending)\n'
         'r2 - Output all cars of a certain color\nq - Quit')

    option = input('Choose and option\n')


    if option == "a":

        addmake = input("Input Make: ")
        addmodel = input("Input Model: ")
        addyear = input("Input Year: ")
        addcolor = input("Input Color: ")

        add_query = "INSERT INTO garage (make, model, year, color) VALUES ('%s','%s',%s,'%s')" % (addmake, addmodel, addyear, addcolor)
        execute_query(conn,add_query)

    elif option =='d':
        #Delete entry
        
        #Cursor picks up everything from table, runs it through a query to turn it into a dictionary, is printed by user
        #makes dictionary appear neater, easier on the eyes
        garagelistdict = "SELECT * FROM garage"
        better_dict = execute_read_query(conn,garagelistdict)
        for user in better_dict:
            print(user)

        #User inputs ID to select item, this way there is less chance of syntax error occuring
        #Input noted as item_to_delete, inserted as a dynamic value into delete_statement, query is then run
        #item_to_delete is searched for in id, if found then contents in row are deleted
        item_to_delete = input('Select Item to remove by ID:\n')
        delete_statement = "DELETE FROM garage WHERE id = %s" % (item_to_delete)
        execute_query(conn,delete_statement)

    elif option =='u':

            #Cursor picks up everything from table, runs it through a query to turn it inot a dictionary, is printed by user
            #makes dictionary appear neater, easier on the eyes
            garagelistdict = "SELECT * FROM garage"
            better_dict = execute_read_query(conn,garagelistdict)
            for user in better_dict:
                print(user)

            #User inputs ID to select item to adjust, then chooses what trait to adjust
            item_to_update = input('Select item to update by ID:\n')

            #Prints a sub menu to allow choice of what detail to delete
            print('Update Menu:\n1 - Make\n2- Model\n3 - Year\n4 - Color')
            
            detail_update = (input('Select detail to update: '))
            
            #Query replaces old detail with new one provided, repeated for the rets of the sub query
            if detail_update == "1":
                new_make = input("Input New Make: ")
                item_update = """
                UPDATE garage
                SET make = '%s'
                WHERE id = %s""" % (new_make,item_to_update)

                execute_query(conn,item_update)

            elif detail_update == "2":
                new_model = input("Input New Model: ")
                item_update = """
                UPDATE garage
                SET model = '%s'
                WHERE id = %s""" % (new_model,item_to_update)

                execute_query(conn,item_update)

            elif detail_update == "3":
                new_year = input("Input New Year: ")
                item_update = """
                UPDATE garage
                SET year = %s
                WHERE id = %s""" % (new_year,item_to_update)

                execute_query(conn,item_update)
           
            elif detail_update == "4":
                new_color = input("Input New Color: ")
                item_update = """
                UPDATE garage
                SET color = '%s'
                WHERE id = %s""" % (new_color,item_to_update)
                execute_query(conn,item_update)

    elif option == "r1":
        #Prints garage table after sorting cars by year in ascending order
        select_garage_order = "Select * FROM garage ORDER BY year"
        garage_alph = execute_read_query(conn,select_garage_order)

        for user in garage_alph:
            print(user)

    elif option == "r2":
        #Selects cars of a certain color to show
        color_select = input("Select car color: ")
        #Searchs color column for selected color, case sensitive
        color_group = "Select * FROM garage WHERE color = '%s'" %(color_select)
        garage_co = execute_read_query(conn,color_group)

        for user in garage_co:
            print(user)
