from flask import Flask, Request, Response
import serverless_http

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# Wrap the Flask app with serverless-http
handler = serverless_http(app)

# Alternative explicit handler (try this if above doesn't work)
# def handler(request: Request) -> Response:
#     return serverless_http(app)(request) 