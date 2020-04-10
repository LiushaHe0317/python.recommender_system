import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(user='liusha1',
                                                  password='Liusha-test-1234',
                                                  host='localhost',
                                                  database='recommenderData',
                                                  use_pure=False)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def selectAll(self):
        data = []
        users = []
        items = []
        ratings = []

        self.cursor.execute("SELECT rating, Users_idUsers, Recipe_idRecipe from rating;")
        rows = self.cursor.fetchall()

        for r in rows:
            ratings.append(r[0])
            users.append(r[1])
            items.append(r[2])

        data.append(users)
        data.append(items)
        data.append(ratings)

        return data

    def getNames(self, item_id):
        self.cursor.execute("SELECT recipeName FROM recipe WHERE idRecipe = " + str(item_id) + ";")
        rows = self.cursor.fetchall()

        return rows[0]
