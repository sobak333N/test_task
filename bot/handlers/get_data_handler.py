from aiogram import F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from .router import product_router
from keyboards import main_menu_kb
from states import EnterProductDataState
from utils import ChatInfo
from logic import ProductService
from errors import ProductDoesntExitstsExc, NotValidArtikulExc


product_service = ProductService()


@product_router.callback_query(F.data == "get_data")
async def product_get_data(clbck: CallbackQuery, state: FSMContext):
    msg = clbck.message
    await clbck.message.delete()

    text_ = '<b>Введите артикул товара</b>\nИли вернитесь в главное меню'

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
    artikul = msg.text
    try:
        product = await product_service.get_product(artikul)
    except (ProductDoesntExitstsExc, NotValidArtikulExc) as e:
        message = await msg.answer(
            text=f"{e.detail}\nВведите другой артикул",
            reply_markup=main_menu_kb
        )
        await state.update_data(msg_id=message.message_id)
        return

    # Форматирование текста с использованием HTML
    text = (
        f"<b>Информация о товаре:</b>\n"
        f"<b>Артикул:</b> {product.artikul}\n"
        f"<b>Название:</b> {product.name}\n"
        f"<b>Цена:</b> {product.cost / 100:.2f} ₽\n"
        f"<b>Рейтинг:</b> {product.rating} ⭐️\n"
        f"<b>Общее количество:</b> {product.total_quantity} шт.\n"
    )

    message = await msg.answer(
        text=text,
        reply_markup=main_menu_kb,
        parse_mode="HTML"  # Указание режима разметки HTML
    )
    