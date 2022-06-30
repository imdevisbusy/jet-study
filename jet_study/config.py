import os


token = os.getenv('API_TOKEN')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
print(token)