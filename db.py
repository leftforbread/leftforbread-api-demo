import logging
import os
import random
import time
from argparse import ArgumentParser, RawTextHelpFormatter

from datetime import date

import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row, dict_row

DATABASE_URL="postgresql://jaycee:_JyGFbsyg9IvjclwMKOeNQ@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"

cur_user = " "

def create_accounts(conn, username, password):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO user_info (username, pass, health_tag, diet_tags) VALUES (%s, %s, ARRAY[], ARRAY[])", (username, password,))
        logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)


def delete_accounts(conn, username):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM user_info WHERE username == %s", (username,))
        logging.debug("delete_accounts(): status message: %s",
                      cur.statusmessage)

def add_htag(conn, username, tag):
    with conn.cursor() as cur:
        cur.execute("UPDATE user_info SET health_tag = array_append(health_tag, %s) WHERE username = %s", (tag, username,))
    logging.debug("add_htag(): status message: %s",
                      cur.statusmessage)

def add_dtag(conn, username, tag):
    with conn.cursor() as cur:
        cur.execute("UPDATE user_info SET diet_tags = array_append(diet_tags, %s) WHERE username = %s", (tag, username,))
    logging.debug("add_dtag(): status message: %s",
                      cur.statusmessage)

def get_htag(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT health_tag FROM user_info WHERE username = %s", (username,))
        return cur.fetchone()[0]

def get_dtag(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT diet_tags FROM user_info WHERE username = %s", (username,))
        return cur.fetchone()[0]
    
def add_favorite(conn, username, recipie):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO favorites (user, recipie) VALUES (%s, %s)", (username, recipie,))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

def remove_favorite(conn, username, recipie):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM favorites WHERE username == %s AND recipie == %s", (username, recipie,))

def create_plan(conn, user):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO weekly_plans (b_1, b_2, b_3, b_4, b_5, b_6, b_7, l_1, l_2, l_3, l_4, l_5, l_6, l_7, d_1, d_2, d_3, d_4, d_5, d_6, d_7, username, d) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', %s, CURRENT_DATE)", (user,))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

def get_plan(conn, user):
    with conn.cursor() as cur:
        cur.execute("SELECT b_1, b_2, b_3, b_4, b_5, b_6, b_7, l_1, l_2, l_3, l_4, l_5, l_6, l_7, d_1, d_2, d_3, d_4, d_5, d_6, d_7 FROM weekly_plans WHERE d = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (user,))
        return cur.fetchall()[0]

def get_favorites(conn, user):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM favorites WHERE username = %s", (user,))
        return cur.fetchall()[0]

def add_to_plan(conn, user, recipie, position):
    with conn.cursor() as cur:
        if position == "b_1":
            cur.execute("UPDATE weekly_plans SET b_1 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_2":
            cur.execute("UPDATE weekly_plans SET b_2 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_3":
            cur.execute("UPDATE weekly_plans SET b_3 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_4":
            cur.execute("UPDATE weekly_plans SET b_4 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_5":
            cur.execute("UPDATE weekly_plans SET b_5 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_6":
            cur.execute("UPDATE weekly_plans SET b_6 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "b_7":
            cur.execute("UPDATE weekly_plans SET b_7 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_1":
            cur.execute("UPDATE weekly_plans SET l_1 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_2":
            cur.execute("UPDATE weekly_plans SET l_2 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_3":
            cur.execute("UPDATE weekly_plans SET l_3- = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_4":
            cur.execute("UPDATE weekly_plans SET l_4 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_5":
            cur.execute("UPDATE weekly_plans SET l_5 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_6":
            cur.execute("UPDATE weekly_plans SET l_6 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "l_7":
            cur.execute("UPDATE weekly_plans SET l_7 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_1":
            cur.execute("UPDATE weekly_plans SET d_1 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_2":
            cur.execute("UPDATE weekly_plans SET d_2 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_3":
            cur.execute("UPDATE weekly_plans SET d_3 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_4":
            cur.execute("UPDATE weekly_plans SET d_4 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_5":
            cur.execute("UPDATE weekly_plans SET d_5 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_6":
            cur.execute("UPDATE weekly_plans SET d_6 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))
        elif position == "d_7":
            cur.execute("UPDATE weekly_plans SET d_7 = %s WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (recipie, user, user,))


def remove_plan(conn, user, position):
    with conn.cursor() as cur:
        cur.execute("UPDATE weekly_plans SET %s = "" WHERE username = %s AND d  = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (position, user,))

def get_ingredients(conn, user):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM weekly_plans WHERE username = %s", (user,))
        jj = cur.fetchone()
        print(jj)
        print("jj above yoooooo")
        ret = []
        i = 1
        while i < 28:
            temp = []
            if jj[i] != '':
                name = jj[i]["recipe"]["ingredients"]
                for i in ret:
                    if i[0] == name:
                        i[1] += jj[i]["recipe"]["quantity"]
                else:
                    temp[0] = name
                    temp[1] = jj[i]["recipe"]["quantity"]
            ret.append(temp)
            i += 1
        return ret


def login(conn, name, passw):
    with conn.cursor() as cur:
        cur.execute("SELECT username FROM user_info WHERE (username = %s AND pass = %s)", (name, passw,))
        ret = cur.fetchone()
        if ret == None:
            print("Login Failed")
        else:
            print("Login Success")
            return ret

# for sqlite3 only
# def dict_factory(cursor, row):
#     fields = [column[0] for column in cursor.description]
#     return {key: value for key, value in zip(fields, row)}

def start():
    opt = parse_cmdline()
    logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)
    db_url = "postgresql://jaycee:_JyGFbsyg9IvjclwMKOeNQ@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"
    conn = psycopg.connect(db_url, 
                            application_name="$ docs_simplecrud_psycopg3", 
                            row_factory=namedtuple_row)
    # import sqlite3
    # conn = sqlite3.connect('temp.sqlite')
    # conn.row_factory = dict_factory
    return conn

def main():
    conn = start()
    create_accounts(conn, "tester", "a")
    create_plan(conn, "tester")
    add_to_plan(conn, "tester", '{"h": "1"}', "b_7")
    plan = get_plan(conn, "tester")
    print(get_ingredients(conn, "tester"))
    print(plan)

def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    parser.add_argument(
        "dsn",
        default=os.environ.get("DATABASE_URL"),
        nargs="?",
        help="""\
database connection string\
 (default: value of the DATABASE_URL environment variable)
            """,
    )

    opt = parser.parse_args()
    if opt.dsn is None:
        parser.error("database connection string not set")
    return opt


if __name__ == "__main__":
    main()