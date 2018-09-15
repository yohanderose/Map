from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd

################################################################################
# METHODS

def openDB():
    conn = sqlite3.connect('DCC.db')
    return conn,conn.cursor()

def addLocation(lat, long):
    conn,c = openDB()

    insert = ([float(lat), float(long)])
    c.execute("""INSERT INTO Locations VALUES(?,?)""", insert)

    conn.commit()
    conn.close()

def getLocations():
    conn,c = openDB()
    c.execute("""SELECT * FROM Locations""")
    locations = c.fetchall()

    df = pd.DataFrame(columns="Longitude Latitude".split())
    for i in range(len(locations)):
        df.loc[i] = locations[i]
    return df.to_json(orient='records')

    conn.commit()
    conn.close()
################################################################################
# MAIN

if __name__=="__main__":

    conn,c = openDB()

    c.execute("""DROP TABLE IF EXISTS Locations""")

    c.execute("""CREATE TABLE Locations (
    lat numeric PRIMARY KEY,
    long numeric
    )""")

    conn.commit()
    conn.close()

    addLocation(2,3.5)
    addLocation(4,5)


################################################################################
# WEB
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def main():
        if request.method == 'POST':
                lat = request.document.getElementById('pointLat')
                addLocation(lat, 9999)
                return render_template('templates/json.html')
        return render_template('map.html')

    @app.route('/locations')
    def printLoc():
        pass

    app.run(debug=True)
