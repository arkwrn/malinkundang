# Malinkundang

> STILL IN DEVELOPMENT

Malinkundang is Backend for Sangkuriang Project, A security analyzer tools
You find the Frontend in https://github.com/Proyek-Sangkuriang/sangkuriang

# Project flow
![Login](flow/Tech-Flowchart.jpg)
## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication

## How To Use

Clone this repository and make a virtual environment in it. Install the modules listed in the `requirements.txt` file:

```console
pip3 install -r requirements.txt
```

To run the starter:

First, set your `PYTHONPATH`:

```console
export PYTHONPATH=$PWD
```

Next:

```console
python3 app/main.py
```

You also need to start your mongodb instance, if you don't have it please install first or use our mongodb docker.

https://github.com/Proyek-Sangkuriang/purbasari/tree/master/mongodb

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0). 


## Deploying to Heroku

To deploy to Heroku, connect your repository to the Heroku application and deploy the branch master.

Ensure you fill up the environment variable `DB_URL` in your `.env` file

## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## TODOS

- [ ] Add a simple bash script file that runs the installation process.

- [ ] Fix Authentication logic

- [ ] Add Dockerfile

- [x] Deploying to Heroku

- [ ] Write a concise README

- [x] Add NMAP module

- [x] Add OWASP ZAP module

- [x] Add Subdomain enumeration module

# Tested in

@arkwrn :
-- OS       : MacOS Catalina
-- Database : https://github.com/Proyek-Sangkuriang/purbasari/tree/master/mongodb
-- Python   : 3.7.2
## License

This project is licensed under the terms of MIT license.
