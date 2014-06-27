from flask import Flask, request
from bustime.stopmonitoring import StopMonitor
from os import getenv

app = Flask(__name__)

BUSTIME_API_KEY = getenv("BUSTIME_API_KEY")

@app.route("/")
def stop_monitor():
    stop = request.args.get('stop', None)
    route = request.args.get('route', None)
    max_visits = request.args.get('max_visits', 2)
    return StopMonitor(BUSTIME_API_KEY, stop, route, max_visits).json()

if __name__ == "__main__":
    app.run(debug=True)
