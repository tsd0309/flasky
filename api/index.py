from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# Vercel requires this handler
def handler(request):
    return app(request) 