## Installation

1. create `venv` first

    `python -m venv env`
2. change directory to `app_api/`
3. RUN 
```
python manage.py migrate
python manage.py runserver
```

## Testing
- You can access it via a browser http://127.0.0.1:8000 

available routes is:
Endpoint CRUD:

`GET /species/ → List all species`

`POST /species/ → Create new species`

`PUT /species/<id>/ → Update data species`

`DELETE /species/<id>/ → Delete species`

