import psutil
from flask import Flask

app = Flask(__name__)

@app.route('/')
def os_info():
    cpu_percent = psutil.cpu_percent()
    return f'CPU Usage: {cpu_percent}%'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6600)
