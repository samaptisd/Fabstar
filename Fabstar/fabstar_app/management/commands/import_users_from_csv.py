import pandas as pd
import pymysql
import math
import os
import django

import sys


sys.path.append('/var/www/Fabstar_project')  # or the absolute path to your project root
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fabstar_project.settings')

import django
django.setup()

from django.contrib.auth.hashers import make_password

# Load CSV
df = pd.read_csv('/var/www/Fabstar_project/Dr. Aludecor Credential - data.csv')

# Convert NaN to None
df = df.applymap(lambda x: None if pd.isna(x) or (isinstance(x, float) and math.isnan(x)) else x)

# Hash passwords using Django's hasher
df['password'] = df['password'].apply(lambda pwd: make_password(pwd) if pwd else None)

# Connect to MySQL
import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='DME#aludecor23',
    database='fabstar_db'
)
cursor = connection.cursor()

# Insert users
for index, row in df.iterrows():
    sql = """
    INSERT INTO auth_user (
        id,
        password,
        last_login,
        is_superuser,
        username,
        first_name,
        last_name,
        email,
        is_staff,
        is_active,
        date_joined
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """
    cursor.execute(sql, (
        row['id'],
        row['password'],
        row['last_login'],
        row['is_superuser'],
        row['username'],
        row['first_name'],
        row['last_name'],
        row['email'],
        row['is_staff'],
        row['is_active']
    ))

# Finalize
connection.commit()
cursor.close()
connection.close()
print("Users imported successfully.")