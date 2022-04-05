import random

from faker import Faker
from faker.providers import DynamicProvider

from database import cursor, db

print(random.randint(3, 9))

# Create word provider
position_provider = DynamicProvider(
    provider_name="position",
    elements=['doctor', 'assistant', 'surgeon', 'clerk']
)
office_provider = DynamicProvider(
    provider_name="office",
    elements=['Khulna', 'Dhaka', 'Sylhet', 'Rajshahi']
)
salary_provider = DynamicProvider(
    provider_name="salary",
    elements=['85000', '67000', '26555', '15000']
)

fake = Faker()
fake.add_provider(position_provider)
fake.add_provider(office_provider)
fake.add_provider(salary_provider)

for _ in range(1000):
    sql = "INSERT INTO employee (name, position, office, extension, startdate, salary) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (fake.name(), fake.position(), fake.office(), fake.phone_number(), fake.date_this_decade(), fake.salary())
    cursor.execute(sql, val)

    db.commit()

    print(cursor.rowcount, "record inserted.")


# if __name__ == "__main__":
#     for _ in range(1000):
#         sql = "INSERT INTO employee (name, position, office, extension, startdate, salary) VALUES (%s, %s,%s, %s,%s, " \
#               "%s) "
#         val = (fake.name(), fake.position(), fake.office(), fake.phone_number(), fake.date_this_decade(), fake.salary())
#         cursor.execute(sql, val)
#
#         db.commit()
#
#         print(cursor.rowcount, "record inserted.")