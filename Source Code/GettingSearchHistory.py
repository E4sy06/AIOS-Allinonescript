from msilib.schema import File
import os
import sqlite3


def GettingSearchHistory():
    try:
        con = sqlite3.connect(
            '/home/manivannan/.config/google-chrome/Default/History')
        c = con.cursor()
        c.execute("select url, title, visit_count, last_visit_time from urls")
        results = c.fetchall()
        for r in results:
            print(r)

    except:
        print("No Chrome Searching History")

    try:
        path = os.path.expanduser(
            '~')+"/.mozilla/firefox/0mttxac9.default"
        files = os.listdir(path)
        history_db = os.path.join(path, 'places.sqlite')
        c = sqlite3.connect(history_db)
        cursor = c.cursor()
        select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
        cursor.execute(select_statement)
        results = cursor.fetchall()
        for url, count in results:
            print(url)

    except:
        print("No Firefox Searching History")

    finally:
        print("No Search History")