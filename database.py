import mysql.connector
import secret

# connects to a specified sql database with a username and password
db = mysql.connector.connect(
    host="localhost",
    user=secret.username,
    passwd=secret.password,
    database="flappybird"
)

# creates a cursor used to write queries
cursor = db.cursor()

# Creates the database in mysql
#cursor.execute("CREATE DATABASE flappybird")

# Drops the specified table
#cursor.execute("DROP TABLE HighScore")

# Creates a table named HighScore with a highscore variable
#cursor.execute("CREATE TABLE HighScore (place smallint UNSIGNED,highscore int UNSIGNED)")

# inserting into the table and committing
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (1, 1))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (2, 9))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (3, 8))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (4, 7))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (5, 6))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (6, 5))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (7, 4))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (8, 3))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (9, 2))
#cursor.execute("INSERT INTO HighScore (place, highscore) VALUES (%s, %s)", (10, 1))
#db.commit()

#updating a specific row
#cursor.execute("UPDATE HighScore SET highscore=0 WHERE place=1")

# Getting all the information in the table Score
#cursor.execute("SELECT * FROM HighScore")

