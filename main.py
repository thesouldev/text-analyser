from flask import Flask
import config

def main():
    global app
    app = Flask(__name__)
    config.app = app
    print(config.ROOT)

    @app.route("/test")
    def hello():
        return f"Hello!"

    return app

if __name__ == '__main__':
    main()
    app.run(debug=True, port=8080)