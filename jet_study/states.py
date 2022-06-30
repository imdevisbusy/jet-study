from aiogram.dispatcher.filters.state import StatesGroup, State


class Timetable(StatesGroup):
    ITS_REPEAT = State()
    TEXT = State()
    SAVE = State()

# #"""
# # Оно будет повторяться каждую неделю?
#     да / нет
# # Напишите текст в формате: номер_урока:предмет
# # ""
