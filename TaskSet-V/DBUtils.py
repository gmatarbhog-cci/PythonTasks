import mysql.connector

class DBUtils:
    def __init__(self):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="sa123456#",
            database="python",
            port="3307"
        )
        self.db = db
        self.cursor = db.cursor()

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS `time_log` (`id` INT NOT NULL AUTO_INCREMENT, `type` VARCHAR(45) NOT NULL, `function_name` VARCHAR(45) NOT NULL, `time` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`));"
        self.cursor.execute(sql)

    def insert_data(self, data):
        sql = "INSERT INTO time_log (type, function_name, time) VALUES (%s, %s, %s);"
        self.cursor.executemany(sql, data)
        self.db.commit()
        return self.cursor.rowcount

    def truncate_data(self):
        sql = "TRUNCATE `time_log`;"
        self.cursor.execute(sql)
