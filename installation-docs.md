# Text Analyser

Using Flask to build a Text Analyser with Restful API Server.


### Pre-requisites:
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Google Cloud Platform]()
- [Cloud Datastore Emulator]()
- [Perspective API Account]()
- [Google Natural Language V1]()


## Installation

1. Clone the repository

	```sh
	git clone https://github.com/thesouleddev/text-analyser.git
	```
2. Create virtual environment and install requirements with pip

	```sh
	python3 -m venv venv
	pip install -r requirements.txt
	```

3. Create Service Account on Google Cloud Console, we will need this service account json to setup and access Cloud Datastore. The account creation can be done by following the steps given in this [link](https://cloud.google.com/iam/docs/creating-managing-service-accounts).

	After creating the service account, download the service account json (sa.json) from console and move it to the application root directory. 

4. Create account on [Perspective platform](https://developers.perspectiveapi.com/s/?language=en_US), which we will be using to analyse toxicity of the content. After creation the API needs to be enabled on the Google Cloud APIs.

	Update PERSPECTIVE_API_KEY in the config.py under class Config

	```py
	class Config:
		PERSPECTIVE_API_KEY = ""
	```

5. Enable [Google Natural Language API](https://cloud.google.com/natural-language/docs/basics) on the console, this service will be used to analyse context and sentiment of the given document.

6. Export environment variables

	```sh
	source local_env.sh
	```
7. Run the application locally
	```sh
	python main.py
	```

## Flask Application Structure 
```
.
|──────text-analyser/
| |────modules/
| | |────text-analyser/
| | |──────__init__.py
| | |──────analyser.py
| | |──────base.py
| | |──────views.py
| |────models/
| | |────odb/
| | |──────__init__.py
| | |──────ndb.py
| | |────text_analyser.py/
| | |────users.py
| |────static/
| | |────styles/
| | |──────styles.css
| | |──────text-analyser.css
| |────template/
| | |────text_analyser/
| | |──────display.html
| | |──────document_render.html
| | |────header.html
| | |────.gitignore
| | |────Dockerfile
| | |────LICENSE
| | |────README.md
| | |────config.py
| | |────deployment.yaml
| | |────local_env.sh
| | |────main.py
| | |────requirements.txt
| | |────service.yaml
| | |────wsgi.py
| | |────sa.json
```

 
## Run Flask

### Run flask for develop
```
$ python main.py
```
### Run flask for production

** Run with gunicorn **

In  webapp/

```
$ gunicorn -w 4 -b 127.0.0.1:5000 run:app

```

* -w : number of worker
* -b : Socket to bind


### Run with Docker

```
$ docker build -t text-analyser .

$ docker run -p 5000:5000 --name text-analyser text-analyser
 
```

