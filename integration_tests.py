# import requests

# def test_get_case():
#     url = 'http://127.0.0.1:5000/healthz'
#     response_get = requests.get(url)
#     response_post = requests.post(url)
#     response_not_found = requests.get(url+'/')
#     assert response_get.status_code == 200
#     assert response_post.status_code == 405
#     assert response_not_found.status_code == 404

import pymysql

def test_mysql_connection():
    try:
        connection = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="rootpassword",
            database="test_db",
            auth_plugin='mysql_native_password'
        )
        connection.close()
        assert True
    except pymysql.MySQLError as e:
        assert False, f"MySQL Error: {e}"

if __name__ == '__main__':
    test_mysql_connection()
