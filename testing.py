import aiomysql
import asyncio
async def db_operations():
    conn = await aiomysql.connect(host='http://127.0.0.1:8000/', user='root', password='jroshan@98',db="learning_model",port='3306') # db
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM users")
        result = await cur.fetchall()
        print(result)
    conn.close()

await db_operations()