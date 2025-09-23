import os
import psycopg2
import logging

from contextlib import contextmanager
from psycopg2.extras import DictCursor

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

_DATABASE_NAME = 'todos'
class DatabasePersistence:

    def __init__(self):
        self._setup_schema()
    
    def _setup_schema(self):
        with self._database_connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS lists (
                        id serial PRIMARY KEY,
                        title text NOT NULL
                    );
                    """
                )
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS todos (
                        id serial PRIMARY KEY,
                        title text NOT NULL,
                        completed boolean NOT NULL DEFAULT false,
                        list_id int NOT NULL REFERENCES lists(id) ON DELETE CASCADE
                    );
                    """
                )
    
    @contextmanager
    def _database_connect(self):
        try:
            if os.environ.get('FLASK_ENV') == 'production':
                connection = psycopg2.connect(os.environ['DATABASE_URL'])
            else:
                connection = psycopg2.connect(dbname=_DATABASE_NAME)
            with connection:
                yield connection
        finally:
            connection.close()

    def _find_todos_for_list(self, list_id):
        query = "SELECT * FROM todos WHERE list_id = %s"
        logger.info("Executing query: %s with list_id: %s", query, list_id)

        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (list_id,))
                return cursor.fetchall()
    
    def find_list(self, list_id):
        query = "SELECT * FROM lists WHERE id = %s"
        logger.info("Executing query: %s with list_id, %s", query, list_id)
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (list_id,))
                lst = dict(cursor.fetchone())
        
        todos = self._find_todos_for_list(list_id)
        lst.setdefault('todos', todos)
        return lst

    
    def find_todo(self, list_id, todo_id):
        pass
    
    def all_lists(self):
        query = "SELECT * FROM lists;"
        logger.info("Executing query: %s", query)
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

        lists = [dict(result) for result in results]            
        for lst in lists:
            todos = self._find_todos_for_list(lst['id'])
            lst.setdefault('todos', todos)
        return lists
    
    def create_new_list(self, title):
        insert_list = (
        """
        INSERT INTO lists
        (title)
        VALUES
        (%s);
        """
        )
        logger.info("Executing insert list query: %s with title %s", insert_list, title)

        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(insert_list, (title,))
        
    def update_list_by_id(self, list_id, new_title):
        query = "UPDATE lists SET title = %s WHERE id = %s"

        logger.info("Executing UPDATE LIST QUERY: %s " \
        "with id %s " \
        "and new title '%s'", query, list_id, new_title)
        
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (new_title, list_id))


    def delete_list(self, list_id):
        query = "DELETE FROM lists WHERE id = %s"
        logger.info("Executing DELETE LIST QUERY: %s" \
        " with id %s", query, list_id)
        
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (list_id,))

    def create_new_todo(self, list_id, todo_title):
        query = (
            """
            INSERT INTO todos
            (title, list_id)
            VALUES
            (%s, %s)
            """
        )
        logger.info("Excuting INSERT TODO QUERY: %s " \
        "with list_id %s " \
        "and todo_tile %s", query, list_id, todo_title)
       
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (todo_title, list_id))


    def delete_todo_from_list(self, list_id, todo_id):
        query = "DELETE FROM todos WHERE list_id = %s AND id = %s"

        logger.info("Executing DELETE TODO: %s with list_id %s and todo_id %s", query, list_id, todo_id)

        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (list_id, todo_id))
    
    def update_todo_status(self, list_id, todo_id, new_status):
        query = "UPDATE todos SET completed = %s WHERE list_id = %s AND id = %s"

        logger.info("Executing UPDATE TODOS: %s, with list_id %s, todo_id %s and status %s",
                    query, list_id, todo_id, new_status)
        
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (new_status, list_id, todo_id))

    def mark_all_todos_completed(self, list_id):
        query = "UPDATE todos SET completed = True WHERE list_id = %s"

        logger.info("Executing MARK ALL DONE query: %s with list_id %s",
                    query, list_id)
        
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query, (list_id,))