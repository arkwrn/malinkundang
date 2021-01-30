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

### Dependencies

Please install all folowing dependencies to run all the feature in malinkundang

- NMAP - https://nmap.org/download.html
- MongoDB - https://github.com/Proyek-Sangkuriang/purbasari/tree/master/mongodb

### Run

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

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0).

Please refer to http://localhost:8000/docs to check all API route and test it.
## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## TODOS

- [ ] Add a simple bash script file that runs the installation process.

- [ ] Fix Authentication logic

- [ ] Add Dockerfile

- [x] Deploying to Heroku

- [ ] Write a concise README

- [x] Add NMAP module

- [ ] Add OWASP ZAP module

- [ ] Add Subdomain enumeration module

# List tested environment

tested by [@arkwrn](https://github.com/arkwrn) :
- OS       : MacOS Catalina 10.15.7
- Database : https://github.com/Proyek-Sangkuriang/purbasari/tree/master/mongodb
- Python   : 3.7.2

## License

This project is licensed under the terms of MIT license.
