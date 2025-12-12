import asyncio

from aiogram import types

from LLM.llm import interpret_query
from LLM.query_builder import build_sql
from bot.dispatcher import dp

from database.session import SessionLocal


@dp.message.register()
async def handle_text_message(message: types.Message):
    user_text = message.text.strip()
    await message.chat.do("typing")

    try:
        interpretation = await interpret_query(user_text)
    except Exception as e:
        await message.answer("Ошибка при интерпретации запроса: " + str(e))
        return

    try:
        sql = build_sql(interpretation)
    except Exception as e:
        await message.answer("Не удалось построить SQL: " + str(e))
        return

    try:
        result = await asyncio.to_thread(run_query, sql)
    except Exception as e:
        await message.answer("Ошибка выполнения запроса: " + str(e))
        return

    await message.answer(str(result))

def run_query(sql: str):
    db = SessionLocal()
    try:
        res = db.execute(sql).scalar()
        return int(res) if res is not None else 0
    finally:
        db.close()