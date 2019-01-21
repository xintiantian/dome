import psycopg2
import cx_Oracle as CX
import pymysql
import pymongo
from pymongo import MongoClient
import urllib.parse
import psycopg2



def get_paysqlone(sql):
    # 支付数据库,返回一条数据
    conn = psycopg2.connect(database="rock_payment_test", user="rock_test", password="rock_test_pwd",
                            host='172.10.1.57', port="5432")
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchone()
    conn.close()
    return rows[0]

def get_paysqlall(sql):
    # 支付数据库,返回所有数据
    conn = psycopg2.connect(database="rock_payment_test", user="rock_test", password="rock_test_pwd",
                            host='172.10.1.57', port="5432")
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    conn.close()
    conn.commit()
    conn.close()
    #return [i[0] for i in rows]

def get_merchant_id(id):
    # 支付数据库根据id获取merchant_id的key值
    sql = "SELECT key from configs where merchant_id = %d" % id
    return get_paysqlone(sql)

# ------------------------------------------------------支付-----------------------------------------------------------------------

# def get_deposit_sit_one(sql):
#     # 存管sit数据库，返回一条数据
#     conn = psycopg2.connect(database="rock_deposit_sit", user="rock_sit", password="rock_sit_pwd",
#                             host='47.92.87.56', port="5432")
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchone()
#     conn.close()
#     return rows[0]
#
# def get_deposit_sit_all(sql):
#     # 存管sit数据库,返回一组数据
#     conn = psycopg2.connect(database="rock_deposit_sit", user="rock_sit", password="rock_sit_pwd",
#                             host='47.92.87.56', port="5432")
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.close()
#     return [i[0] for i in rows]
#
# def get_deposit_uat_one(sql):
#     # 存管uat数据库，返回一条数据
#     conn = psycopg2.connect(database="rock_deposit_uat", user="rock_uat", password="rock_uat_pwd",
#                             host='47.92.87.56', port="5432")
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchone()
#     conn.close()
#     return rows[0]
#
# def get_deposit_uat_all(sql):
#     # 存管uat数据库,返回一组数据
#     conn = psycopg2.connect(database="rock_deposit_uat", user="rock_uat", password="rock_uat_pwd",
#                             host='47.92.87.56', port="5432")
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.close()
#     return [i[0] for i in rows]

#def get_depositmg_uat_one(table, loct):
    # 存管mongdb uat环境 获取查询最后一条数据
    client = MongoClient("47.92.87.56", 27017)
    db = client['rock_uat']
    db.authenticate("rock_uat", "rock_uat_pwd")
    coll = db['{}'.format(table)]
    a = coll.find(loct)
    client.close()
    return [i for i in a][-1]

#def get_depositmg_uat_all(table, loct):
    # 存管mongdb uat环境 获取查询s.所有数据
    client = MongoClient("47.92.87.56", 27017)
    db = client['rock_uat']
    db.authenticate("rock_uat", "rock_uat_pwd")
    coll = db['{}'.format(table)]
    a = coll.find(loct)
    client.close()
    return a

#def get_depositmg_sit_one(table, loct):
    # 存管mongdb sit环境 获取查询最后一条数据
    client = MongoClient("47.92.87.56", 27017)
    db = client['rock_sit']
    db.authenticate("rock_sit", "rock_sit_pwd")
    coll = db['{}'.format(table)]
    a = coll.find(loct)
    client.close()
    return [i for i in a][-1]

#def get_depositmg_sit_all(table, loct):
    # 存管mongdb sit环境 获取查询所有数据
    client = MongoClient("47.92.87.56", 27017)
    db = client['rock_sit']
    db.authenticate("rock_sit", "rock_sit_pwd")
    coll = db['{}'.format(table)]
    a = coll.find(loct)
    client.close()
    return a

# ------------------------------------------------------存管----------------------------------------------------------------------

#def get_oracleone_uat(sql):
    # oracle 数据库返回一条信息
    conn = CX.connect('reporter', 'password', 'localhost:1521/ORCL')
    cursor = conn.cursor()
    # sql = "select * from test"
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    return data

#def get_oracleall(sql):
    # oracle数据库返回所有信息
    conn = CX.connect('reporter', 'password', 'localhost:1521/ORCL')
    cursor = conn.cursor()
    # sql = "select * from test"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data

#def get_mysqlone(sql):
    # mysql数据库返回一条信息
    db = pymysql.connect("localhost", "testuser", "test123", "TESTDB", "utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 关闭数据库连接
    db.close()
    return data

#def get_mysqlall(sql):
    # mysql数据库返回所有信息
    db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return data

#if __name__ == '__main__':

    # x = {"status":"3"}
    # #
    # client = MongoClient("47.92.87.56", 27017)
    # db = client['rock_uat']
    # db.authenticate("rock_uat","rock_uat_pwd")
    # coll = db['hsbank_deposit_out']
    # a = coll.find(x)
    # for i in a:
    #     print(i)
    # print(a)

    # a = get_depositmg_sit_all('hsbank_deposit_out', {"sequence_id":"c6268dc77addc4e8817a9b39118e96c6"})
    # a = ([i['msg'] for i in a])
    # for i in a:
    #     print(i)
    # if '请求数据有误或账户状态异常' in a:
    #     print(1)
    # else:
    #     print(2)

    # value = get_depositmg_uat_all('hsbank_deposit_out', {"sequence_id": "cca45047cd8634d5a6082afd3acf668b"})
    # a = [i for i in value]
    # print(a[-1])
    # print(len(a))
    # print([i['msg'] for i in value])
    # a = ['交易成功', '交易成功', '开户成功']
    # if '开户成功' in a:
    #     print(True)
    # else:
    #     print(False)
    value1 = get_depositmg_uat_all('hsbank_deposit_out', {"sequence_id": "32ee1bb1fc91d25b3b32a458149e9ae6"})
    for i in value1:
        print(i)
    # card_no = [i for i in value1][-1]['card_no']  # 充值异步产生的card_no
    # amount = [i for i in value1][-1]['amount']  # mongodb中的充值数据
    # print(card_no)
    # print(amount)