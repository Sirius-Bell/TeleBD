import aiomysql

from tele_bd.config import config, loop


async def create_pool(loope):
    """

    :ivar loope: Asyncio event loop
    :vartype loope: Asyncio.AbstractLoop
    :return: A pool used to connect to mysql
    :rtype: pool
    """
    return await aiomysql.create_pool(
        host=config.host.get_secret_value(),
        port=int(config.port.get_secret_value()),
        user=config.user.get_secret_value(),
        password=config.password.get_secret_value(),
        db=config.database_name.get_secret_value(),
        loop=loope,
        autocommit=True
    )

db_pool = loop.run_until_complete(create_pool(loop))
