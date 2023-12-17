from aiomysql import DictCursor, Pool

from tele_bd.database.sql import db_pool
from tele_bd.errors.err import TableNotChosen, DataIsNoneOrNotTuple


class DBc:
    """
    DataBase commands
    """
    def __init__(self):
        self.pool: Pool = db_pool

    async def get_all(self, table):
        """
        Gets all data from database
        :ivar table: table name
        :vartype table: str
        :return: response from database
        :rtype: dict
        """
        if isinstance(table, str) is False:
            raise TableNotChosen("Table not chosen or Table is not a string")
        async with self.pool.acquire() as connect:
            async with connect.cursor(DictCursor) as cursor:
                await cursor.execute(f"SELECT * FROM {table}")
                data = await cursor.fetchall()

        data = [str(i) for i in data]
        return '\n'.join(data)

    async def execute(self, command: str):
        """
        Execute any command from database
        :ivar command: command in SQL style
        :vartype command: str
        :return: response from database
        :rtype: dict
        """
        async with self.pool.acquire() as connect:
            async with connect.cursor(DictCursor) as cursor:
                await cursor.execute(command)
                return await cursor.fetchall()

    async def add_data(self, table_name: str, data: tuple):
        """
        Add data to table from database
        :ivar table_name: table name from database
        :vartype table_name: str
        :ivar data: data to add
        :vartype data: tuple
        :return: response
        :rtype: dict
        """
        if isinstance(data, tuple) is False:
            raise DataIsNoneOrNotTuple
        if isinstance(table_name, str) is False:
            raise TableNotChosen
        async with self.pool.acquire() as connect:
            async with connect.cursor(DictCursor) as cursor:
                cm = f"INSERT INTO {table_name} VALUES {str(data)}"
                await cursor.execute(cm)
                return await cursor.fetchall()

    async def delete_data(self, table_name: str, row_name: str, id_t: int):
        """
        Delete data from table
        :ivar table_name: table name from database
        :vartype table_name: str
        :ivar row_name: row name
        :vartype row_name: str
        :ivar id_t: id from table from first row
        :vartype id_t: int
        :return: response
        :rtype: dict
        """
        async with self.pool.acquire() as connect:
            async with connect.cursor(DictCursor) as cursor:
                cm = f"DELETE FROM {table_name} WHERE {row_name} = {id_t}"
                await cursor.execute(cm)
                return await cursor.fetchall()


db = DBc()
