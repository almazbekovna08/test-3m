from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
from config import token
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random
import logging

logging.basicConfig(level=logging.INFO)

bot=Bot(token=token)
dp=Dispatcher()

buttons = [
     [KeyboardButton(text='Игра'), KeyboardButton(text='Наши новости')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')


game_keyboard=ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Камень, ножницы, бумага'), KeyboardButton(text='Рандомайзер')]
], input_field_placeholder='Выберите кнопку')

game1_keyboard=ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Камень'), KeyboardButton(text='Ножницы')],
     [KeyboardButton(text='Бумага')]
], input_field_placeholder='Выберите кнопку')

news_keyboard=ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='О нас'), KeyboardButton(text='Адрес')],
     [KeyboardButton(text='Наши курсы')]
], input_field_placeholder='Выберите кнопку')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!', reply_markup=keyboard)

@dp.message(F.text=='Игра')
async def cmd_game(message:Message):
    await message.answer("Выберите игру: ", reply_markup=game_keyboard)

@dp.message(F.text=='Камень, ножницы, бумага')
async def cmd_3(message:Message):
    await message.answer("Выберите: ", reply_markup=game1_keyboard)

@dp.message(F.text.in_({'Камень', 'Ножницы', 'Бумага'}))
async def randomm(message:Message):
    hand=random.choice(['Камень', 'Ножницы', 'Бумага'])
    user_hand=message.text
    if user_hand==hand:
        await message.answer(f'Ничья. Было сгенерировано: {hand}')
    elif user_hand=='Камень' and hand=='Ножницы':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    elif user_hand=='Ножницы' and hand=='Бумага':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    elif user_hand=='Бумага' and hand=='Камень':
        await message.answer(f'Победа. Было сгенерировано: {hand}')
    else:
        await message.answer(f'Поражение.  Было сгенерировано: {hand}')

@dp.message(F.text=='Рандомайзер')
async def cmd_2(message:Message):
    word=random.choice(['Вы победили', 'Вы проиграли', 'Ничья'])
    await message.answer(word)

@dp.message(F.text=='Наши новости')
async def cmd_news(message:Message):
    await message.answer('Выберите что именно хотите узнать: ', reply_markup=news_keyboard) 
  
@dp.message(F.text=='О нас')
async def about(message:Message):
    await message.reply('Geeks - это айти курсы в Оше, в Кара-Балте и в Бишкеке, основанные в 2018г')

@dp.message(F.text=='Адрес')
async def location(message:Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)

@dp.message(F.text=='Наши курсы')
async def courses(message:Message):
    await message.reply('У нас предоставляются 3 направления: 1.Backend 2.Fronted 3.UI-UX дизайн, обучение длится 5 месяцев, стоимость 10.000 сом')

async def main():
        await dp.start_polling(bot)
if __name__=='__main__':
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')