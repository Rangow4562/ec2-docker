
import pymysql
import aws_credentials as rds
conn = pymysql.connect(
        host= rds.host, #endpoint link
        port = rds.port, # 3306
        user = rds.user, # admin
        password = rds.password, #adminadmin
        db = rds.db, #test
        
        )

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table reg4 (fname varchar(200),lname varchar(200),date nvarchar(10),age nvarchar(5),gender varchar(20),rolno nvarchar(20),email varchar(50),address varchar(500),phone nvarchar(11),course varchar(200),sem varchar(200) )

# """
# cursor.execute(create_table)


def insert_details(fname,lname,date,age,gender,rolno,email,address,phone,course,sem):
    cur=conn.cursor()
    cur.execute("INSERT INTO reg4 (fname,lname,date,age,gender,rolno,email,address,phone,course,sem) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (fname,lname,age,date,gender,rolno,email,address,phone,course,sem))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM reg4")
    details = cur.fetchall()
    return details