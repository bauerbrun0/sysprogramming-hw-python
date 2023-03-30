# Python programming Homework
Python homework for university course "System programming".


## Running the application

#### Setting up virtualenv (optional)

##### Install virtualenv:

    pip install virtualenv

##### Create virtualenv:
Linux:

```bash

path/to/project$ virtualenv .
path/to/project$ source bin/activate
```

Windows:

```
path\to\project> virtualenv .
path\to\project> .\Scripts\activate
```

#### Install dependencies:

```
path/to/project$ pip install -r requirements.txt
```

#### Run the application:
With python 3
```
path/to/project$ python run.py
```
You can also pass the path to the config file as an argument:
```
path/to/project$ python run.py -c path/to/config/file
```