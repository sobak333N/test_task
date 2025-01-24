from aiogram import F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from .router import product_router
from keyboards import main_menu_kb
from states import EnterProductDataState
from utils import ChatInfo


@product_router.callback_query(F.data == "get_data")
async def product_get_data(clbck: CallbackQuery, state: FSMContext):
    msg = clbck.message
    await clbck.message.delete()

    text_ = '<b>Введите артикул товара</b>\nИли вернитесь в главное меню'

    await msg.message.delete()
    message = await msg.answer(
        text=text_,
        reply_markup=main_menu_kb
    )
    await state.set_state(EnterProductDataState.artikul)
    await state.update_data(msg_id=message.message_id)


@product_router.message(EnterProductDataState.artikul, F.text)
async def handle_artikul(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    chat_info = ChatInfo(msg)

    await msg.delete()
    await bot.delete_message(
        chat_id=chat_info.chat_id,
        message_id=data['msg_id']
    )
    print(msg.text)