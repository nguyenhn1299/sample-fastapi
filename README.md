# Sample FastAPI Project 

A boilerplate FastAPI project.

## Codebase Structure 

```
.   
├── main  
│   ├── controllers             // Controller layer - listing endpoints of each router
│   ├── engines                 // Data access layer - CRUD files to interact with DB
│   ├── models                  // Entity layer - defining table schemas 
│   ├── schemas                 // DTO layer - schema for request body & response of endpoints  
│   ├── services                // Service layer - defining business logics
│   ├── config.py               // Application configs and env parameters
│   └── __init__.py             // FastAPI application creation and configuration
├── .env                        // Hidden env file
├── env.example                 // Example env variables 
├── README.md  
└── requirements.txt            // Necessary packages

```

## Prerequisite

### 1. Set up database

1.1. Install PostgresDB

- Download PostgresDB from https://www.postgresql.org/download/

1.2. Create new database

```commandline
createdb <DATABASE_NAME>
```

### 2. Set up codebase

2.1. Install Python

- Download Python from https://www.python.org/downloads/
- Check python version
```commandline
python3 --version
```
2.2. Open project 
- Clone the project
```commandline
git clone https://github.com/nguyenhn1299/sample-fastapi.git
```
- Open it in any IDE

2.3. Create virtual environment for the project.

We want to create a project-specific environment. So packages installed across different projects are not conflicted in versions. In the root directory of this project, run:
```commandline
python3 -m venv env
```
New folder `env` will be created in the root directory

2.4. Activate virtual environment 
```commandline
source env/bin/activate
```

2.5. Install necessary packages
```commandline
pip install -r requirements.txt
```

2.6. Set up server environment variables

Typically, the service needs dynamic values or secret values that shouldn't be disclosed publicly. Those variables are stored in the `.env` file and are ignored by git. To configure one locally,

- Create new file named `.env`
- Fill out values of those environment variables listed in `env.example` file

## Run

Start the web service by running:
```commandline
uvicorn main:app --reload --port 5000
```

`--reload` flag indicates that the service will be reloaded whenever any change is detected in codebase

The service URL is http://127.0.0.1:5000.

FastAPI auto generates interface description for HTTP APIs. 
The API description is available at http://127.0.0.1:5000/redoc or http://127.0.0.1:5000/docs. To interact with APIs, use `/docs`

Note: When running, the service will auto convert all logical ORMs declared in `models` folder to physical tables in PostgresDB.

