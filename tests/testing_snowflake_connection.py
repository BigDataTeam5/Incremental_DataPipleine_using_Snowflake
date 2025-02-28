import pytest
import snowflake.connector
import os
from dotenv import load_dotenv
load_dotenv()
@pytest.fixture
def snowflake_connection():
    """Fixture to establish a connection to Snowflake."""
    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
        )
        yield conn
    finally:
        conn.close()

def test_snowflake_connection(snowflake_connection):
    """Test if Snowflake connection is successful."""
    assert snowflake_connection is not None
    assert snowflake_connection.is_closed() == False

def test_snowflake_query_execution(snowflake_connection):
    """Test if a simple query executes successfully."""
    cursor = snowflake_connection.cursor()
    try:
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        assert result is not None
        assert isinstance(result[0], str)
    finally:
        cursor.close()

if __name__ == "__main__":
    pytest.main()
