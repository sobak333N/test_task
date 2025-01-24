from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .router import product_router
from keyboards import get_data_kb


@product_router.message(Command("start"))
@product_router.callback_query(F.data == "menu")
async def product_menu(msg: Message | CallbackQuery, state: FSMContext):
    await state.clear()
    text_ = '<b>Главное меню </b>\nНажмите на кнопку'
    if isinstance(msg, Message):
        await msg.delete()
    if isinstance(msg, CallbackQuery):
        await msg.message.edit_text(
            text=text_,
            reply_markup=get_data_kb
        )
        return

    await msg.answer(
        text=text_,
        reply_markup=get_data_kb
    )
