from flask import Flask
import config


def main():
    global app
    app = Flask(__name__, template_folder="template")
    config.app = app

    config.register_urls()

    return app


main()
app.config.from_object("config.Config")
app.run(debug=False)
