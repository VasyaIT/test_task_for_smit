# Test_task_for_SMIT (not William)
**REST API service for calculating the cost of insurance**

## Clone repository
```commandline
git clone https://github.com/VasyaIT/test_task_for_smit.git
```
## Before start, set settings in the .env and .env.test files
.env
```
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
```
.env.test
```
POSTGRES_HOST=db_test
POSTGRES_PORT=5432
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
```
## ! Not require to create .evn files because in config.py everything is already set up
# Start
```commandline
docker compose up --build
```
# Tests
```commandline
docker compose -f docker-compose.tests.yml up --build
```
# Warning!
![Image](https://github.com/VasyaIT/test_task_for_smit/blob/main/image.png)  
Since Tortoise cannot delete all tables, does not delete the entire database, the last rows are commented out, since Docker cannot delete the current database  
If you are going to run tests outside of Docker, then uncomment these lines
