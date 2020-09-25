DBS Tech Track

- Python version: 3.5 & above
- Django version: 3.1

## Prerequisites
- Ensure VirtualEnv is Installed : `pip install virtualenv`

## Set Up
- change directory to 'DBS-TechTrack': `cd DBS-TechTrack`
- create a new virtual environment: `virtualenv venv`
- activate the virtual environment: `venv\Scripts\activate`
- update pip and setuptools to latest version: `python -m pip install --upgrade pip setuptools`
- change directory to 'Enso': `cd TechTrack`
- install dependencies: `pip install -r requirements.txt`
- once done, you can deactivate the virtual environment: `venv\bin\deactivate`

## Verifying Modules Installation
- To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:
```python
import django
django.__version__
```

## Initializing the Server
- change directory to 'DBS-TechTrack': cd `TechTrack`
- run the server: `python manage.py runserver`
- once done, you can deactivate the virtual environment: `venv\bin\deactivate`
