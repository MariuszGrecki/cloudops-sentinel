from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.get("/")
def index():
    return {
        "service": "cloudops-sentinel-backend",
        "status": "running"
    }

@app.get("/health")
def health():
    try:
        conn = psycopg2.connect(
            host="database",
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )

        conn.close()

        return {
            "status": "healthy",
            "database": "connected"
        }, 200

    except Exception as error:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }, 503

app.run(host="0.0.0.0", port=8000)
