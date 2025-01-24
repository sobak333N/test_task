from aiogram.fsm.state import State, StatesGroup


class EnterProductDataState(StatesGroup):
    artikul = State()