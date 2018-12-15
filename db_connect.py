import pymysql.cursors

# sql = """insert into test(id, text) values ( %s, %s, %s)"""
# curs.execute(sql,(5,"test2"))
#curs = conn.cursor(pymysql.cursors.DictCursor)

class mysql_test:
    def __init__(self, host, user, password, db):
        self.conn = pymysql.connect(host=host,
                               user = user,
                               password = password,
                               db = db,
                               charset='utf8')
    def keyword_get(self, type, query, val):
        try:
            if type == "SELECT":
                with self.conn.cursor() as cursor:
                    sql = query
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    return result
                    
            if type == "UPDATE":
                with self.conn.cursor() as cursor:
                    sql = query
                    print(sql)
                    print(val)
                    cursor.execute(sql,val)
                    self.conn.commit()
                    
            if type == "DELETE":
                with self.conn.cursor() as cursor:
                    sql = query
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    
            if type == "INSERT":
                with self.conn.cursor() as cursor:
                    sql = query
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
            # self.conn.close()
        except:
            self.conn.close()
        

if __name__ == '__main__':
    db = mysql_test(host = "210.92.91.236", user = "root",password= "hadoop", db = "yun")
    # keywords = my.keyword_get("SELECT * FROM main_db;")
    # for keyword in keywords:
        # print(keyword)

    db.keyword_get(type="UPDATE", query="UPDATE main_db SET flag=%s WHERE user=%s", val=(0, 1))