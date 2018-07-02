import MySQLdb
aws_ip =  "18.179.74.220"
connection = MySQLdb.connect (host = aws_ip,
                              user = "root",
                              passwd = "root",
                              db = "xproj")

cursor = connection.cursor()

id = 'jy016011'
passwd = '1234'
name = 'Kim-Jun-Young'
email = 'jy016011@naver.com'

staff_data = [(id,passwd,name,email),
              (id, passwd, name, email)]

for p in staff_data:
    format_str = """INSERT INTO members (id , passwd , name , email)
    VALUES ( '{id}' , '{passwd}', '{name}' , '{email}');
    """

    sql_command = format_str.format(id = p[0], passwd = p[1], name = p[2] , email = p[3])
    print(sql_command)
    cursor.execute(sql_command)

connection.commit()
cursor.close()
connection.close()
# Im Gwanghyo, footprint