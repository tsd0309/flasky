from flask import Flask, Request, Response
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# Vercel-specific handler with proper typing
def handler(request: Request) -> Response:
    return app(request) 