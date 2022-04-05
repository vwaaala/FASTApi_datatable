from typing import Optional

from fastapi import APIRouter

from database import cursor

router = APIRouter()


def query_maker(search, filter_name, filter_position, filter_office, filter_extension, filter_startdate, filter_salary):
    filter_query = ''
    if search != '':
        filter_query = '''
            AND name LIKE '%{0}%'
            OR position LIKE '%{0}%'
            OR office LIKE '%{0}%'
            OR extension LIKE '%{0}%'
            OR startdate LIKE '%{0}%'
            OR salary LIKE '%{0}%'
            '''.format(search)
    else:
        if filter_name != '':
            filter_query += 'AND name LIKE "%{name}%"'.format(name=filter_name)
        if filter_position != '':
            filter_query += 'AND name LIKE "%{position}%"'.format(position=filter_position)
        if filter_office != '':
            filter_query += 'AND name LIKE "%{office}%"'.format(office=filter_office)
        if filter_extension != '':
            filter_query += 'AND name LIKE "%{extension}%"'.format(extension=filter_extension)
        if filter_startdate != '':
            filter_query += 'AND name LIKE "%{startdate}%"'.format(startdate=filter_startdate)
        if filter_salary != '':
            filter_query += 'AND name LIKE "%{salary}%"'.format(salary=filter_salary)
    return filter_query


@router.get("/employee", tags=["employee"])
async def employees(
        limit: Optional[int],
        offset: Optional[int],
        sort_col: Optional[str],
        sort_by: Optional[str],
        search: Optional[str],
        filter_name: Optional[str],
        filter_position: Optional[str],
        filter_office: Optional[str],
        filter_extension: Optional[str],
        filter_startdate: Optional[str],
        filter_salary: Optional[str]
):
    filter_query = query_maker(search, filter_name, filter_position, filter_office, filter_extension, filter_startdate,
                               filter_salary)

    sql_query = 'SELECT * FROM blog.employee WHERE  id != 0 {4} ORDER BY {2} {3} LIMIT {0} OFFSET {1}' \
        .format(limit, offset, sort_col, sort_by, filter_query)
    cursor.execute(sql_query)
    read_employees = cursor.fetchall()
    list_employees = []
    for employee in read_employees:
        list_employees.append(dict(
            id=employee[0],
            name=employee[1],
            position=employee[2],
            office=employee[3],
            extension=employee[4],
            startdate=employee[5],
            salary=employee[6]
        ))
    return {
        'status': 200,
        'data': list_employees,
        'message': 'Employee data retrieved successfully'
    }


@router.get('/employee/pages/{limit}', tags=["pages"])
async def pages(limit: int = 10):
    cursor.execute('SELECT CEIL(COUNT(*) / {0}) as pages FROM employee'.format(limit))
    read_employee = cursor.fetchall()
    return {
        'status': 200,
        'pages': read_employee[0][0],
        'message': 'Employee table pages count data retrieved successfully'
    }


@router.get('/employee/length', tags=['length'])
async def length(
        search: Optional[str],
        filter_name: Optional[str],
        filter_position: Optional[str],
        filter_office: Optional[str],
        filter_extension: Optional[str],
        filter_startdate: Optional[str],
        filter_salary: Optional[str]
):
    filter_query = query_maker(search, filter_name, filter_position, filter_office, filter_extension, filter_startdate,
                               filter_salary)
    cursor.execute('SELECT COUNT(*) as length FROM employee where id != 0 {0}'.format(filter_query))
    read_employee = cursor.fetchall()
    return {
        'status': 200,
        'length': read_employee[0][0],
        'message': 'Employee length retrieved successfully'
    }


@router.get('/employee/total', tags=['total'])
async def total():
    cursor.execute('SELECT SUM(salary) AS total FROM employee')
    read_employee = cursor.fetchall()
    return {
        'status': 200,
        'total': read_employee[0][0],
        'message': 'Employee salary sum data retrieved successfully'
    }
