import os
import redis
import time
import socket
import logging
import platform
from datetime import datetime
from flask import Flask, jsonify, render_template
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

START_TIME = time.time()

redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total App Requests'
)

@app.route('/')
def dashboard():
    uptime = round(time.time() - START_TIME, 2)

    visitor_count = redis_client.incr('visitors')

    REQUEST_COUNT.inc()

    system_data = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'python_version': platform.python_version(),
        'uptime': uptime,
        'environment': os.getenv('ENV', 'production'),
        'deployment': 'Azure App Service',
        'ci_cd': 'GitHub Actions',
        'status': 'Healthy',
        'visitors': visitor_count
    }

    return render_template('index.html', data=system_data)

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'uptime_seconds': round(time.time() - START_TIME, 2)
    })

@app.route('/metrics')
def metrics():
    return jsonify({
        'cpu_usage': '24%',
        'memory_usage': '41%',
        'active_connections': 12,
        'requests_per_minute': 87
    })

@app.route('/deployment')
def deployment():
    return jsonify({
        'version': 'v2.0',
        'deployment_time': datetime.utcnow().isoformat(),
        'pipeline': 'GitHub Actions'
    })

@app.route('/logs')
def logs():
    app.logger.info('Logs endpoint accessed')
    return jsonify({
        'logging': 'active',
        'level': 'INFO'
    })

@app.route('/prometheus')
def prometheus_metrics():
    return generate_latest(), 200, {
        'Content-Type': 'text/plain'
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)