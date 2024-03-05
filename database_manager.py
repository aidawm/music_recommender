import json 
import mysql.connector as mysql


class DB:
    def __init__(self) -> None:
        data_address = "configs.json"
        f = open(data_address)
        self.configs = json.load(f)
        self.configs = self.configs["db"]

        self.__connect_to_db_server__()
        
        self.__create_table__()


    def __connect_to_db_server__(self):
        self.mydb = mysql.connect(host=self.configs["HOST"], 
            port=self.configs["PORT"],
            database=self.configs["DATABASE"], 
            user=self.configs["USER"], 
            password=self.configs["PASSWORD"])
    

    def __create_table__(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS requests (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) NOT NULL, status VARCHAR(255) DEFAULT 'pending', songID VARCHAR(255)) ")

    
    def show_tables(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
          print(x)
    
    def new_request(self,email):
        mycursor = self.mydb.cursor()

        sql = "INSERT INTO requests (email) VALUES (%s)"

        mycursor.execute(sql, [email])

        self.mydb.commit()

        mycursor.execute("SELECT LAST_INSERT_ID()")

        myresult = mycursor.fetchall()
        print("id ----> "+str(myresult))
        
        return myresult[0][0]

    def show_requests (self):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT * FROM requests")

        myresult = mycursor.fetchall()

        for x in myresult:
          print(x)

if __name__ == '__main__': 
    db = DB()
    db.show_tables()

    db.new_request("aida.mobli@aut.ac.ir")

    db.show_requests()