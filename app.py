from flask import Flask, request, render_template
import smtplib
import time

app = Flask(__name__)

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

def send_email(to_email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    msg = f"Subject:{subject}\n\n{message}"
    server.sendmail(EMAIL, to_email, msg)

    server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    send_email(email, subject, message)

    return "Email Sent Successfully!"

@app.route('/schedule', methods=['POST'])
def schedule():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    delay = int(request.form['delay'])

    time.sleep(delay)
    send_email(email, subject, message)

    return "Scheduled Email Sent!"

if __name__ == '__main__':
    app.run(debug=True)
