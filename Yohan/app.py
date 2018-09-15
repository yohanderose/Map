from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd

################################################################################
# METHODS

def openDB():
    conn = sqlite3.connect('DCC.db')
    return conn,conn.cursor()

# def addLocation(lat, long):
#     conn, c = openDB()
#
#     insert = ([float(lat), float(long)])
#     c.execute("""INSERT INTO Locations VALUES(?,?)""", insert)
#
#     conn.commit()
#     conn.close()


################################################################################
# MAIN

if __name__== "__main__":

    conn,c = openDB()

    c.execute("""DROP TABLE IF EXISTS Locations""")

    c.execute("""CREATE TABLE Locations (
    lat numeric,
    long numeric
    )""")

    conn.commit()
    conn.close()
    #
    # addLocation(2,3.5)
    # addLocation(4,5)


################################################################################
# WEB
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def main():
        return render_template('map.html')

    @app.route('/locations')
    def printLoc():
        pass

    @app.route('/api/locations', methods=['GET'])
    def getLocations():
        conn, c = openDB()
        c.execute("""SELECT * FROM Locations""")
        locations = c.fetchall()

        df = pd.DataFrame(columns="Longitude Latitude".split())
        for i in range(len(locations)):
            df.loc[i] = locations[i]

        conn.commit()
        conn.close()
        return df.to_json(orient='records')


    @app.route('/api/locations', methods=['POST'])
    def addLocation():
        content = request.json
        print(content)
        coordinates = request.json

        conn, c = openDB()

        for coordinate in coordinates:
            test = coordinate["Latitude"]
            label = coordinate["Label"]
            insert = ([float(coordinate["Latitude"]), float(coordinate["Longitude"])])
            c.execute("""INSERT INTO Locations VALUES(?,?)""", insert)

        conn.commit()
        conn.close()
        return ('', 204)

    app.run(debug=True)
