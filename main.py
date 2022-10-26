from flask import Flask
import config

def main():
    global app
    app = Flask(__name__)
    config.app = app
    
    config.register_urls()

    return app

if __name__ == '__main__':
    main()
    app.run(debug=True, port=8080)