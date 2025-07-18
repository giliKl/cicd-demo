from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from CI/CD Demo App!",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "version": os.environ.get("APP_VERSION", "1.0.0")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
