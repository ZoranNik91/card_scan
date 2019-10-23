# from __future__ import print_function
import mysql.connector as MC
import sys
from datetime import time
from datetime import datetime #datetime is type of -> class <- datetime
import json


# Global variables
is_in = 1
# Connect to DB and set cursor
db = MC.connect(host='localhost', database='employees', user='admin', password='admin')

def get_by_date(date):
    
    cursor = db.cursor()
    cursor.execute(f"""
            SELECT name, surname, times.time, times.is_in, times.user_id FROM users
            JOIN times ON times.user_id = users.id
            WHERE time BETWEEN '{date} 00:00:00' AND '{date} 23:59:59'
            ORDER BY times.time DESC, times.id DESC
        """)
    
    rows = cursor.fetchall()

    cursor.close()

    res = []
    for row in rows:
        dateTime = row[2]
        formattedTime = dateTime.strftime("%H:%M:%S")
        formattedDate = dateTime.strftime("%Y-%m-%d")
        obj = {
            "name": row[0],
            "surname": row[1],
            "time": formattedTime,
            "date": formattedDate,
            "is_in": row[3]
        }
        # ti = time.format(time(dateTime.hour, dateTime.minute, dateTime.second))
        res.append(obj)
                
    return res



def insert_time(user_id):

    res_obj = {}
    is_in = 1

    cursor = db.cursor()
    # format() - method lets us concatenate elements within a string through positional formatting
    cursor.execute("SELECT * FROM times WHERE user_id = {}".format(user_id))  
    rows = cursor.fetchall()
    cursor.close()
    
    # check if we have any record of user_id in times table (cursor.rowcount == 0)
    if (len(rows) == 0):      # Cursor.rowcount property returns number of fetched rows
        is_in = 1
        res_obj['message'] = "Welcome user "

    # Check if user has entered or is leaving (cursor.rowcount %2 = 0 or 1)
    else:
        is_in = (len(rows) + 1) % 2
        res_obj['message'] = 'Signed in' if is_in else 'Signed out'


        
    # Save new record
    cursor = db.cursor()
    new_query = "INSERT INTO times (is_in, user_id) VALUES (%s, %s)"
    query = (is_in, user_id)
    cursor.execute(new_query, query)
    db.commit()
    cursor.close()

    return res_obj

def insert_user(name,surname,email,phone,card_id):

    cursor = db.cursor()
    res_obj = {}
    res_obj['message'] = "User not inserted"

    new_query = """
    INSERT INTO users (name, surname, email, phone, card_id) 
    VALUES (%s, %s, %s, %s, %s)
    """
    query = (name, surname, email, phone, card_id)
    # query (inputed values) saves in new_query via %s in SQL
    cursor.execute(new_query, query)        
    print(f"User {name} {surname} was created!")
    db.commit()
    cursor.close()

    res_obj['message'] = "User inserted" # TODO: always success kinda sucks

    return res_obj


def get_user_card_id(card_id):
    
    cursor = db.cursor()
    res_obj = {}
    cursor.execute(f"SELECT * FROM users WHERE card_id = {card_id}")
    row = cursor.fetchone()
    cursor.close()

    # Checks if we have user or not, if not posibility to create on
    if (row == None):
       
        res_obj['status'] = "error"
        res_obj['message'] = "User does not exists"
        res_obj['user'] = None

    # if the user exists    
    else:
        user_id = row[0]

        res_obj['status'] = "success"
        res_obj['message'] = "User exists"
        res_obj['user'] = row

        insert_time(user_id)
    
    return res_obj

  
if __name__ == '__main__':

    if len(sys.argv) == 2:

        date = sys.argv[1]
        res = get_by_date(date)
        # json.dumps() takes an object and produces a string
        print(json.dumps(res, indent=4, sort_keys=True))  

    else:

        card_id = input("Your ID: ")
        res_obj = get_user_card_id(card_id)

        if (res_obj['user'] is not None): 

            row = res_obj['user']
            user_id = row[0]
            res = insert_time(user_id)
            print(res)

        else:

            print("Would you like to create a user ? (y/n): ", end = '')
            answer = input()
            
            if (answer == 'y'):
                name = input("Name: ")
                surname = input("Surname: ")
                email = input("Email: ")
                phone = input("Phone number: ")
                insert_user(name, surname, email, phone, card_id)
                print("User created")
            else:
                print("Operation aborted")