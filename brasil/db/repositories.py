from .sqlite_access import Database


async def get_area_by_name(name:str):
    query = '''SELECT * FROM territorios
            WHERE nome = ?'''
    async with await Database.connect_db() as db:
        if db:
            async with db.execute(query, (name,)) as cursor:
                row = await cursor.fetchone()
                return dict(row) if row else None


async def get_area_by_id(id: int):
    query = '''SELECT * FROM territorios
            WHERE id = ?'''
    async with await Database.connect_db() as db:
        if db:
            async with db.execute(query, (id,)) as cursor:
                row = await cursor.fetchone()
                return dict(row) if row else None


async def get_all():
    query = '''SELECT * FROM territorios'''
    async with await Database.connect_db() as db:
        if db:
            async with db.execute(query) as cursor:
                rows = await cursor.fetchall()
                return [dict(rows) for row in rows]


async def insert_territory(id_: int, nome: str, dimensao: float):
    query = '''INSERT INTO territorios (id, nome, dimensao)
            VALUES (?, ?, ?)'''
    async with await Database.connect_db() as db:
        if db:
            try:
                await db.execute(query, (id_, nome, dimensao))
                await db.commit()
            except Exception as e:
                print(f"Erro ao inserir território: {e}")
