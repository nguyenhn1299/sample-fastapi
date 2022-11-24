# Sample FastAPI Project 

## Setup

1. Create a Postgres Database
2. Install necessary packages
```commandline
pip install -r requirements.txt
```
3. Create `.env` file and fill out environment variables listed in `env.example` file

## Run

```commandline
uvicorn main:app --reload --port 5000
```

API Documentation is available at `http://127.0.0.1:5000/redoc` or `http://127.0.0.1:5000/docs`


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
