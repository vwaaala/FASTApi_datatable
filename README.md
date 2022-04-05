
# Data table filter api




## Features

- auto calculation
- table search
- table filter
- table pagination
- table sort
- table order


## Installation

Install my-project with npm

```bash
  cd my-project
  virtualenv venv # activate env
  pip instll -r requirements.txt
  uvicorn main:app
  
```
    
## API Reference

#### Get all items

```http
  GET /employee
```



#### Get item

```http
  GET /?limit=${limit}&offset=${offset}&sort_col=${sort.column}&sort_by=${sort.by}&search=${search}&filter_name=${filter.name}&filter_position=${filter.position}&filter_office=${filter.office}&filter_extension=${filter.extension}&filter_startdate=${filter.startdate}&filter_salary=${filter.salary}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `limit`      | `int` | **Required**. Limit of item to fetch |
| `offset`      | `int` | **Required**. Offset of item to fetch |




## Tech Stack

**Server:** Python, Uvicorn, Pydantic, FastAPI, Mysql, Faker

