import sqlite3

from aiogram import Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from config import Kiber
from config import Kiber1
from config import Kiber2
from config import Kiber4
from config import Updatee
from config import Send
from config import Zakaz
from config import Tcodee
from config import Tcodee1
from keyboard import keyboard12, online, offers_add, adminpanel, under, offers_del, updater, reply
from main import dp


joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

con = sqlite3.connect("offers.db")
cursor = con.cursor()

n = 0

# --------------------------------------------
@dp.callback_query(F.data == 'info')
async def info(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='Этот бот создан для того , что-бы вам друзья было удобнее смотреть ассортимент предоставленный в нашем Телеграмм Канале👌\n\nДля того , что-бы заказать модель можно воспользоваться ботом , а так же переслать сообщение администратору и он поможет вам быстрее подобрать размер и оформить заказ‼️\n\nДоставка осуществляется :\nЕвропочта:2/4 дня \nБелпочта:2/4 дня \nМинск , курьер с примеркой 15 рублей🙌\n\nГарантия на всю обувь 31 календарный день 🔥\n\nОбмен-Возврат не ношенной обуви в течении 14 дней🤝')


@dp.callback_query(F.data == 'get_code')
async def code(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='📲Напишите ваш номер телефона в международном формате без "+" вначале: 375331111111')
    await state.set_state(Tcodee1.name)


@dp.message(Tcodee1.name)
async def code(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute(f"SELECT * FROM code WHERE number={str(callback.text)}")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"Ваш трек код:   {off[2]}")
    if not callback.text in cursor.fetchall():
        await bot.send_message(callback.from_user.id, text='Записей не найдено')

    con.commit()


# --------------------------------------------
@dp.callback_query(F.data == 'tcode')
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Введите номер телефона покупателя без "+" в начале')
    await state.set_state(Tcodee.name)


@dp.message(Tcodee.name)
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(num=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите трек код')
    await state.set_state(Tcodee.name1)


@dp.message(Tcodee.name1)
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f"INSERT INTO code (number, trek) VALUES ({str(data1['num'])}, {str(callback.text)})")
    con.commit()
    await bot.send_message(callback.from_user.id, text='Добавлено')
    await state.clear()


# -------------------------------------------
@dp.callback_query(F.data == 'update')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Выберите фирму', reply_markup=updater)


@dp.callback_query(F.data == 'nike_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM nike")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='nike')
    con.commit()


@dp.callback_query(F.data == 'adidas_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM adidas")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='adidas')
    con.commit()


@dp.callback_query(F.data == 'puma_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM puma")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='puma')
    con.commit()


@dp.callback_query(F.data == 'balance_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM balance")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='balance')
    con.commit()


@dp.callback_query(F.data == 'reebok_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM reebok")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='reebok')
    con.commit()


@dp.callback_query(F.data == 'other_up')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM other")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    await state.update_data(firm='other')
    con.commit()


@dp.message(Updatee.name)
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(id=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите новые размеры')
    await state.set_state(Updatee.name1)


@dp.message(Updatee.name1)
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f'UPDATE {data1["firm"]} SET size ={str(callback.text)} WHERE id={str(data1["id"])}')
    con.commit()
    await bot.send_message(callback.from_user.id, text='обновлено')
    await state.clear()


# ------------------------------------------
@dp.callback_query(F.data == 'delete')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Выберите откуда удалить', reply_markup=offers_del)


@dp.callback_query(F.data == 'nike_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM nike")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='nike')
    con.commit()


@dp.callback_query(F.data == 'adidas_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM adidas")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='adidas')
    con.commit()


@dp.callback_query(F.data == 'balance_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM balance")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='balance')
    con.commit()


@dp.callback_query(F.data == 'reebok_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM reebok")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='reebok')
    con.commit()


@dp.callback_query(F.data == 'puma_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM puma")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='puma')
    con.commit()


@dp.callback_query(F.data == 'other_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM other")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(firm='other')
    con.commit()


@dp.message(Kiber4.name)
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f'DELETE FROM {data1["firm"]} WHERE id = ?', (int(callback.text),))
    con.commit()

    await bot.send_message(callback.from_user.id, text='Удалено')
    await state.clear()


# -----------------------------------------
@dp.callback_query(F.data == 'offersss')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           'Это начало оформления заказа\n\nУ вас обязательно должен быть тег профиля в телеграм\n\n')
    await bot.send_message(callback.from_user.id, text='Введите название товара')
    await state.set_state(Zakaz.name)


@dp.message(Zakaz.name)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if callback.text == '/start':
        await state.clear()
    else:
        await state.update_data(name=callback.text)
        await bot.send_message(callback.from_user.id, text='Введите количество пар обуви')
        await state.set_state(Zakaz.name1)


@dp.message(Zakaz.name1)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    wse = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    if not str(callback.text) in wse:
        await bot.send_message(callback.from_user.id, text='Введите количество пар обуви')
        await state.set_state(Zakaz.name1)
    elif str(callback.text) in wse:
        await state.update_data(count=callback.text)
        await bot.send_message(callback.from_user.id, text='Введите размер')
        await state.set_state(Zakaz.name3)


@dp.message(Zakaz.name3)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    s = ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',
         '48', '49', '50']
    if not str(callback.text) in s:
        await bot.send_message(callback.from_user.id, text='Введите размер')
        await state.set_state(Zakaz.name3)
    elif str(callback.text) in s:
        await state.update_data(size=callback.text)
        await bot.send_message(callback.from_user.id, text='Выберите способ доставки', reply_markup=reply)
        await state.set_state(Zakaz.name4)


@dp.callback_query(F.data == 'bel')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='Запишите данные по форме:\n1:ФИО\n2:Полный адрес проживания \n3:Номер телефона \n4:Индекс')
    await state.set_state(Zakaz.name2)
    await state.update_data(p='Бел')


@dp.callback_query(F.data == 'euro')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='Запишите данные по форме:\n1:ФИО\n2:Номер Телефона \n3:Адрес или номер отделения в городе Европочты')
    await state.set_state(Zakaz.name2)
    await state.update_data(p='Eвро')


@dp.message(Zakaz.name2)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if callback.text == '/start':
        await state.clear()
    else:
        await bot.send_message(callback.from_user.id,
                               'Ждите подтверждения заказа от администратора\n\n\nГарантия на всю обувь 31 календарный день 🔥\nОбмен-Возврат не ношенной обуви в течении 14 дней🤝')
        data1 = await state.get_data()
        await bot.send_message(chat_id=1488076193,
                               text=f'Название: {data1["name"]}\nКоличество: {data1["count"]}\nРазмер: {data1["size"]}\nПокупатель: @{callback.from_user.username}, {callback.from_user.full_name}\n\n{data1["p"]}почта: \n{callback.text}')
        await state.clear()


# ----------------------------------------------
@dp.callback_query(F.data == 'home')
async def home(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Kiber2.name)
    await bot.send_message(callback.from_user.id, text='Выберите бренд', reply_markup=keyboard12)


@dp.callback_query(F.data == 'offerss')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Выберите бренд', reply_markup=online)


# ---------------------------------------------------------------------
@dp.callback_query(F.data == 'nike')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM nike')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM nike")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='nike')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'adidas')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM adidas')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM adidas")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='adidas')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'reebok')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM reebok')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM reebok")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='reebok')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'puma')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM reebok')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM puma")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='puma')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'balance')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM balance')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM balance")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='balance')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'other')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM other')
    total = cursor.fetchone()[0]
    await bot.send_message(callback.from_user.id, text=f'1 из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM other")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(fir='other')
    await state.update_data(n=0)


# ---------------------------------------------------------------------------------
@dp.callback_query(F.data == 'wpered')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data11 = await state.get_data()
    n1 = data11['n']
    n1 += 1

    cursor.execute(f'SELECT COUNT(*) FROM {data11["fir"]}')
    total = cursor.fetchone()[0]
    a = n1 + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute(f"SELECT * FROM {data11['fir']}")
    off = cursor.fetchall()[n1]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    if a == total:
        await state.clear()
    if a < total:
        await state.set_state(Kiber1.name)
        await state.update_data(n=n1)


# @dp.callback_query(F.data == 'nazad' or Kiber1.name1)
# async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     global n
#     n -= 1
#     data11 = await state.get_data()
#     cursor.execute(f'SELECT COUNT(*) FROM nike')
#     total = cursor.fetchone()[0]
#     a=n+1
#     await bot.send_message(callback.from_user.id,text=f'[{a} из {total}]')
#     con.commit()
#
#     cursor.execute(f"SELECT * FROM {data11['fir']}")
#     off = cursor.fetchall()[n]
#
#     await bot.send_photo(callback.from_user.id, photo=off[4])
#     await bot.send_message(callback.from_user.id, text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
#                            reply_markup=under)
#     con.commit()
#     await state.set_state(Kiber1.name1)

@dp.message(Command('admin'))
async def admin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if callback.from_user.id == 1488076193 or callback.from_user.id == 681734057:
        await bot.send_message(callback.from_user.id, text='Здравствуйте, администратор', reply_markup=adminpanel)


@dp.callback_query(F.data == 'plus')
async def plus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Выберите куда добавить', reply_markup=offers_add)


@dp.callback_query(F.data == 'nike_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='nike')


@dp.callback_query(F.data == 'adidas_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='adidas')


@dp.callback_query(F.data == 'puma_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='puma')


@dp.callback_query(F.data == 'balance_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='balance')


@dp.callback_query(F.data == 'reebok_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='reebok')


@dp.callback_query(F.data == 'other_add')
async def nike(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(firma='other')


@dp.message(Kiber.name)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):

    await state.update_data(name=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите цену')
    await state.set_state(Kiber.name1)



@dp.message(Kiber.name1)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(price=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите размеры')
    await state.set_state(Kiber.name3)


@dp.message(Kiber.name3)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(size=callback.text)
    await bot.send_message(callback.from_user.id, text='Отправьте фотографию')
    await state.set_state(Kiber.name4)


@dp.message(Kiber.name4)
async def zakaz(message: Message, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f"INSERT INTO {data1['firma']} (name, price,size,link) VALUES (?, ?, ?,?)",
                   (data1['name'], data1['price'], data1['size'], str(message.photo[-1].file_id)))
    con.commit()
    await bot.send_message(message.from_user.id, text='Успешно добавлено')
    await state.clear()


@dp.message(Command('start'))
async def music(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if not str(callback.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(callback.chat.id) + "\n")
        joinedUsers.add(callback.chat.id)

    await bot.send_message(callback.from_user.id,
                           f'Приветствую @{callback.from_user.username}✌🏾\nРады представить наш бот king kross⤵️\n\nВсе новинки и тренды этого сезона здесь 🫰🏽, и теперь вы можете максимально просто выбирать и заказывать любую понравившуюся вам пару 👟\n\nРадуйте себя и своих близких !\nВаш King kross 😈',
                           reply_markup=keyboard12)


@dp.message(Command('sendall'))
async def mess(callback: CallbackQuery, bot: Bot, state: FSMContext):
    if callback.from_user.id == 1488076193 or 681734057:
        await bot.send_message(callback.from_user.id, text='Отправьте фотографию')
        await state.set_state(Send.name)
    else:
        await bot.send_message(callback.from_user.id, text='Вы ввели неизвестную команду')


@dp.message(Send.name)
async def send(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(link=message.photo[-1].file_id)
    await bot.send_message(message.from_user.id, text='Введите текст рассылки')
    await state.set_state(Send.name2)


@dp.message(Send.name2)
async def send(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    for user in joinedUsers:
        await bot.send_photo(chat_id=user, photo=f'{data1["link"]}')
        await bot.send_message(chat_id=user, text=callback.text)
    await state.clear()


@dp.message(F.text)
async def error_msg(message: Message, bot: Bot, state: FSMContext):
    price = await state.get_data()
    print(price.get("price"))
    await bot.send_message(chat_id=message.from_user.id, text="Вы ввели неизвестную команду")
