import aiosqlite
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

DB_PATH = Path(os.getenv("DB_PATH", "database.db"))


async def get_db_connection():
    conn = await aiosqlite.connect(DB_PATH)
    conn.row_factory = aiosqlite.Row
    return conn

async def get_all_territories():
    # conn = await get_db_connection();
    # cursor = await conn.execute(
    #     "SELECT * FROM territorios"
    # )
    # result = await cursor.fetchall()
    # return {row["id"]: row["nome"] for row in result} if result else None
    async with aiosqlite.connect(DB_PATH) as conn:
        conn.row_factory = aiosqlite.Row
        async with conn.execute("SELECT * FROM territorios") as cursor:
            result = await cursor.fetchall()
            return {row["id"]: row["nome"] for row in result} if result else None

async def get_dimensao_from_db(territory_id: str) -> Optional[float]:
    id = int(territory_id)
    # conn = await get_db_connection()
    # cursor = await conn.execute("SELECT * FROM territorios WHERE id = ?", (id,))
    # result = await cursor.fetchone()
    # await conn.close()
    # return result["dimensao"] if result else None
    async with aiosqlite.connect(DB_PATH) as conn:
        conn.row_factory = aiosqlite.Row
        async with conn.execute("SELECT * FROM territorios WHERE id = ?", (id,)) as cursor:
            result = await cursor.fetchone()
            return result["dimensao"] if result else None


async def save_territory_db(territory_id: int, nome: str, dimensao: float):
    # conn = await get_db_connection()
    # await conn.execute(
    #     "INSERT INTO territorios (id, nome, dimensao) VALUES (?, ?, ?)",
    #     (territory_id, nome, dimensao)
    # )
    # await conn.commit()
    # await conn.close()
    # return "deu certo?????"
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            await conn.execute(
                "INSERT INTO territorios (id, nome, dimensao) VALUES (?, ?, ?)",
                (territory_id, nome, dimensao)
            )
            await conn.commit()
            return True
    except aiosqlite.Error as e:
        print(f"Erro ao salvar no banco de dados: {e}")
        return False
