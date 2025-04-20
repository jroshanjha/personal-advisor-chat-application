# import aiomysql
# import asyncio
# import os 
# from asyncio import sleep, wait_for
# async def db_operations():
#     conn = await aiomysql.connect(host='http://127.0.0.1:8000/', user='root', password='jroshan@98',db="learning_model",port='3306') # db
#     async with conn.cursor() as cur:
#         await cur.execute("SELECT * FROM users")
#         result = await cur.fetchall()
#         print(result)
#     conn.close()

# asyncio.run(db_operations())
# wait_for(asyncio.sleep(5))

# await asyncio.sleep(5)
# await conn.close()
