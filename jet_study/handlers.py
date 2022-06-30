from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
import time
from commands import Commands
from connection import Session
from states import Timetable
from bot import dp

commands = Commands(Session())

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.answer("<b>Jet Study</b> — Бот для учёбы\n\n"
                           "Расписание уроков: /timetable\n"
                           "Расписание звонков: /bells\n"
                           "Время до следующего звонка: /bell_time\n"
                           "Справочные материалы по предметам: /subject_materials\n"
                           "Настройки: /settings")

@dp.message_handler(commands=['timetable'])
async def get_timetable(message: types.Message):
    username = message.from_user.username
    user_id = message.from_id

    without_timetable = f"Привет, <i>{username}</i>!\n" \
                        "У тебя сейчас нет расписания, создай его командой /create_timetable"
    with_timetable = f"Привет, <i>{username}</i>!\n" \
                    "Вот твоё расписание на день_недели:\n" \
                    "Расписание"

    if commands.user_exists(user_id):
        await message.answer(with_timetable)
    else:
        await message.answer(without_timetable)
        commands.add_user(user_id, username)
        commands.commit()

@dp.message_handler(commands=['create_timetable'], state=None)
async def create_timetable(message: types.Message):
    await message.answer("Оно будет повторяться каждую неделю? (Да, Нет)")
    
    await Timetable.ITS_REPEAT.set()


@dp.message_handler(state=Timetable.ITS_REPEAT)
async def answer_its_repeat(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(itsrepeat=answer)
    await message.answer("Напишите текст в формате: номер_урока:предмет")
    await Timetable.TEXT.set()

@dp.message_handler(state=Timetable.TEXT)
async def answer_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    itsrepeat = data.get('itsrepeat')
    text = message.text
    

    await message.answer('Формируем расписание...')
    time.sleep(.3)
    await message.answer('Готово! Расписание создано, его можно посмотреть командой /timetable')
    await state.finish()

@dp.message_handler(commands=['bells'])
async def bells(message: types.Message):
    await message.answer('Расписание звонков')


@dp.message_handler(commands=['bell_time'])
async def bell_time(message: types.Message):
    await message.answer('Время до следующего звонка')


@dp.message_handler(commands=['subject_materials'])
async def subject_materials(message: types.Message):
    await message.answer('Справочные материалы по предметам')


@dp.message_handler(commands=['settings'])
async def settings(message: types.Message):
    await message.answer('⚙️ Настройки')
