from flask import Flask

def main():
    global app
    app = Flask(__name__)
    return app

if __name__ == '__main__':
    main()
    print("hh")
    app.run()