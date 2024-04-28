from flask import Flask
from redis import Redis

redis = Redis(host='redis',port=6379)
app = Flask(__name__)

def gethits():
    try:
        redis.incr('hits')
        return redis.get('hits')
    except Exception as e:
        return "Error while retrieving hit count"

@app.route('/')
def mainpage():
    return f"This site have been visited (times): {gethits()}"

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)