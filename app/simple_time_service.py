from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def get_time():
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr
    }
    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)