from routes import routes
from flask import *

def main():
    try:
        app = Flask(__name__)
        app.register_blueprint(routes)
        app.run(host="0.0.0.0", port="443", debug=False)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()