from flask import Flask, render_template, request, session, redirect, url_for
import pymysql.cursors

app = Flask(__name__)

# Check if database is on local server
localserver = True

#creating connection with mysql database
if(localserver):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kishan123',
                                 db='Kish',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
else:
    connection = pymysql.connect(host='139.59.228.125',
                                 user='root',
                                 password='kishan123',
                                 db='Kish',
                                 charset='',
                                 cursorclass=pymysql.cursors.DictCursor)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:project>")
def dynamic(project):
    print("1 Now opening page for this project - " + project)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `weather_station`"
        print("2 about to execute a sql command")
        cursor.execute(sql)
        print("3 executed a sql command")
        # returns a list of dictionaries
        data = cursor.fetchall()
        print("4 fetched sql data")
        connection.close()
        print("5 closed connection")
        # print(data[1]['temperature'])
        # print(data)

    # return render_template('projects/booknotes.html',data=data)
    return render_template('/{}.html'.format(project),data=data)


if __name__ == '__main__':
    app.run(debug=True)
