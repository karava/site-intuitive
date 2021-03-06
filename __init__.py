from flask import Flask, render_template, request, session, redirect, url_for
import pymysql.cursors

app = Flask(__name__)

#creating connection with mysql database, first try to see if database is local
try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kishan123',
                                 db='Kish',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
except pymysql.err.OperationalError:
    connection = pymysql.connect(host='139.59.228.125',
                                 user='root',
                                 password='kishan123',
                                 db='Kish',
                                 charset='',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("accessing database remotely")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:project>")
def dynamic(project):
    print("1 Now opening page for this project - " + project)

    #treat special case of inventoryApp which is a subdomain
    if project == 'inventoryApp':
        return redirect("http://invapp.intuitive.ai")

    with connection.cursor() as cursor:
        sql = "SELECT * FROM `weather_station`"
        print("2 about to execute a sql command")
        cursor.execute(sql)
        print("3 executed a sql command")
        # returns a list of dictionaries
        data = cursor.fetchall()
        print("4 fetched sql data")
        cursor.close()
        print("5 closed connection")
        # print(data[1]['temperature'])
        # print(data)

    # return render_template('projects/booknotes.html',data=data)
    return render_template('/{}.html'.format(project),data=data)


if __name__ == '__main__':
    app.run(debug=True)
