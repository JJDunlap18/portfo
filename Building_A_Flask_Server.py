from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

# To run this after closing out of pycharm:
# 1) do set FLASK_APP=Building_A_Flask_Server.py
# 2) FLASK_ENV=development
# 3) then flask run



@app.route('/')  # This is a decorator that adds extra tools for us
def my_home():
    return render_template('index.html')

# To turn on Debug mode do set FLASK_ENV=development in terminal,
# then do flask run - this allows changes to be seen when the page is refreshed


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'