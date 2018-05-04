import pymysql.cursors

port = "3306"
hostname = "localhost"	 # 127.0.0.1
username = 'root'
password = '26029823O3d'
database = 'Botishal'

myConnection = pymysql.connect(host = hostname,
                               user = username,
                               password = password,
                               db=database,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)


def make_a_query(query):
    cursor = myConnection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row['email'])
    cursor.close()


def query(query, numOfFields):
    curs = myConnection.cursor()
    qury = query
    table = []

    for i in range(numOfFields):
        cur = curs.execute(qury,params=None,multi=True)
        for (email) in cur:
            field = []
            for x in email:
                if(x):
                    field.append(x[i])
        table.append(field)
    curs.close()
    return table


make_a_query("SELECT email FROM Teachers")
