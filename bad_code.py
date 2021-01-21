
from typing import List, Tuple  # Unended code :-(

import psycopg


def get_rows(user: int) -> List[str]:
    assert user == 0  # Check if user is root in assert :-(
    # Really long line :-(
    return ["secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry", "secret_entry"]


def create_list_with(element, base_list=[]) -> List:  # [] as default param :-(
    base_list.append(element)
    return base_list


def sum(x: int, y: int) -> int:
    return x + y


def _get_answer() -> int:  # not needed fnc :-(
    return 42


if __name__ == "__main__":
    print(get_rows(0))
    print(create_list_with("a"))
    print(create_list_with(5))
    print(create_list_with(5, []))

    # Connect to your postgres DB
    conn = psycopg.connect("dbname=test user=postgres")
    cur = conn.cursor()
    id = input("Enter your user ID: ")
    # SQL query without escaping :-(
    cur.execute(f"SELECT * FROM my_data WHERE user_id = '{id}'")
    records = cur.fetchall()

    print(sum(5, "a"))
