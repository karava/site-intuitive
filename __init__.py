from flask import Flask, render_template, request, session, redirect, url_for
import pymysql.cursors

app = Flask(__name__)

# Check if database is on local server
localserver = False

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
    # print(project)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `weather_station`"
        cursor.execute(sql)
        # returns a list of dictionaries
        data = cursor.fetchall()
        cursor.close()
        # print(data[1]['temperature'])
        # print(data)

    # return render_template('projects/booknotes.html',data=data)
    return render_template('/{}.html'.format(project),data=data)


if __name__ == '__main__':
    app.run(debug=True)
