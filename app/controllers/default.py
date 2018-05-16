from app import app


@app.route("/")  # rota page
def index():
    return "Hello World!"
