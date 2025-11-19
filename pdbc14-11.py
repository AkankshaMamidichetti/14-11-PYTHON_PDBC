import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="****************",
    database="56r",
    port="3306" 
)
print(conn.is_connected())
cur=conn.cursor()


# cur.execute("SHOW TABLES")
# ----------------------------------------------
# creating a table


# cur.execute("""
# CREATE TABLE STUDENT(
#             ID INT PRIMARY KEY AUTO_INCREMENT,
#             NAME VARCHAR(50),
#             MARKS INT
#             )
# """)
# -----------------------------------------------
# inserting values
# cur.execute("""
# INSERT INTO STUDENT(NAME,MARKS) VALUES (%s,%s) 
# """, ("AKANKSHA",85))

# cur.execute( """ 
# INSERT INTO STUDENT (NAME,MARKS) VALUES (%s,%s)""",("NAVYA",90))
# cur.execute("""
# INSERT INTO STUDENT (NAME,MARKS ) VALUES (%s,%s)""",("MYTHRI",70))

# -----------------------------------------------------
# cur.execute("SELECT*FROM STUDENT")  -----------> GIVE ALL THE ROWS IN THE TABLE STUDENTS
# print(cur.fetchall())
# -----------------------------------------------------
# cur.execute("SELECT * FROM STUDENT")
# print(cur.fetchone())
# # conn.commit()
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())
# ------------------------------------------------------
# cur.execute("SELECT * FROM STUDENT WHERE ID=4")
# print(cur.fetchall())
# -------------------------------------------------
# cur.execute("DROP TABLE LOGIN")
# -----------------------------------------------------
# cur.execute("""
#    CREATE TABLE LOGIN(
#             ACCOUNT VARCHAR(50),
#             USERNAME VARCHAR(50),
#             USER_PASSWORD VARCHAR(50)
#             )

# """)
# cur.execute("""
# INSERT INTO LOGIN (ACCOUNT,USERNAME,USER_PASSWORD) VALUES (%s,%s,%s)
# """,("INSTA","INSTA.COM","INSTA_ABC"))
# cur.execute("""
# INSERT INTO LOGIN (ACCOUNT,USERNAME,USER_PASSWORD) VALUES (%s,%s,%s)""",("FB","FB.COM","FB_ABC"))
# conn.commit()
# --------------------------------------------------------------------------
cur.execute("SELECT * FROM LOGIN")
print(cur.fetchall())
# conn.commit() ---> to need of commit to fetch ,the commit is used to make the query permanent
conn.close()