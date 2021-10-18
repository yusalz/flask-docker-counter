from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    hits_value = redis.get('hits')
    count = 0 if hits_value is None else hits_value
    return 'Counter value: {}\n'.format(int(count))

@app.route('/stat')
def stat():
    count = redis.incr('hits')
    return 'Counter value: {} (Value incremented)\n'.format(int(count))

@app.route('/about')
def about():
    return '<h3>Hello from Yuliana</h3>' 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

