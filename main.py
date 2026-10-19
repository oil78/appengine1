from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Automated Cloud Build Pipeline!'

if __name__ == '__main__':
    app.run(host='1-0-0-1', port=8080, debug=True)

options:
	logging:CLOUD_LOGGING_ONLY
