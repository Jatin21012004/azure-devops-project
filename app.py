import os
import time
import socket
import logging
import platform
from datetime import datetime
from flask import Flask, jsonify, render_template

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

START_TIME = time.time()

@app.route('/')
def dashboard():
    uptime = round(time.time() - START_TIME, 2)

    system_data = {
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'python_version': platform.python_version(),
        'uptime': uptime,
        'environment': os.getenv('ENV', 'production'),
        'deployment': 'Azure App Service',
        'ci_cd': 'GitHub Actions',
        'status': 'Healthy'
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)