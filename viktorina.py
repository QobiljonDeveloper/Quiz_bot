import logging

from aiogram import Bot, Dispatcher, executor, types
import asyncio
from buttons import *

API_TOKEN = '6133318403:AAGRz8nIkrGBU0NQHyPff1GMc40dTojJzOg'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(""" Hi bud!
 To start a quiz tap here -> "/start_quiz"
 But every 5 second the new quiz will send!
 So, you should choose faster!
 That will be fun!""")


@dp.message_handler(commands=['start_quiz'])
async def echo(message: types.Message):
    await message.answer_poll(
        question="What do you think about me?",
        options=["You're great", "Normal", "Not really good"],
        is_anonymous=False
    )

    await asyncio.sleep(5)

    await message.answer_poll(
        question="What do you like about me?",
        options=["Name", "Quizes", "A lot of things", "Nothing"],
        is_anonymous=False,
        allows_multiple_answers=True,
    )

    await asyncio.sleep(5)

    await message.answer_poll(
        question="What's my name?",
        options=["Viktorina", "Viktor_Inskiy_bot", "No name"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await message.answer('Tap here to continue -> "/menu"')


@dp.message_handler(commands=['menu'])
async def echo(message: types.Message):
    await message.answer("Quizes menu:", reply_markup=quiz_menu_in_menu)


@dp.message_handler(text=["Maths"])
async def send_welcome(message: types.Message):

    await message.answer('Start!')

    await asyncio.sleep(5)
    
    # 1sav math
    await message.answer_poll(
        question="What you can call the half of the diametr of a skeletons bone?",
        options=["Apotalamus", "Radius", "It's not about math!"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 2sav math
    await message.answer_poll(
        question="2 + 2 * 2 = ...",
        options=["6", "8", "4"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await asyncio.sleep(5)

    # 3sav math
    await message.answer_poll(
        question="8 % 0 = ...",
        options=["8", "0", "Impossible"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)

    # 4sav math
    await message.answer_poll(
        question="If the turtle walks 1km per hour, how many meters he'll walk in three hours?",
        options=["3,000", "3", "300"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await asyncio.sleep(5)

    # 5sav math
    await message.answer_poll(
        question="18 * 2 % 6 * 5 = ...",
        options=["6", "30", "32"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )







@dp.message_handler(text=["Uzbek 🇺🇿"])
async def send_welcome(message: types.Message):

    await message.answer('Start!')

    await asyncio.sleep(5)
    
    # 1sav uzb
    await message.answer_poll(
        question="What is the capital of Uzbekistan?",
        options=["Bishkek", "Tashkent", "Samarkand"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 2sav uzb
    await message.answer_poll(
        question="Traditionally, Uzbek bread is decorated with intricate patterns made with a metal stamp called:",
        options=["Chekich", "Shashlik", "Tandir"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await asyncio.sleep(5)

    # 3sav uzb
    await message.answer_poll(
        question="Which is the tallest Minaret in Uzbekistan?",
        options=["The Kalyan minaret in Bukhara", "The Islom-Hoja Minaret in Khiva", "The minaret of the Hazrat Imam Ensemble in Tashkent"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 4sav uzb
    await message.answer_poll(
        question="The Kalyan minaret in Bukhara was also known as",
        options=["The tower of death", "The leaning tower", "The indestructible tower"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await asyncio.sleep(5)

    # 5sav uzb
    await message.answer_poll(
        question="Plov is Uzbekistan's national dish. What does it consist of?",
        options=["Rice with lamb", "Rice with olives", "Rice with beans and chicken"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )








@dp.message_handler(text=["Logic"])
async def send_welcome(message: types.Message):

    await message.answer('Start!')

    await asyncio.sleep(5)
    
    # 1sav log
    await message.answer_poll(
        question="Who will go home first, bunny or turtle?",
        options=["Bunny", "Turtle", "No one"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 2sav log
    await message.answer_poll(
        question="There were 6 doves on the tree. a man shot and killed 2 pigeons. How many doves are left on the tree?",
        options=["6", "4", "0"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)

    # 3sav log
    await message.answer_poll(
        question="Question: What is always coming, but never arrives?",
        options=["Day", "Doniyor", "Tomorrow"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)

    # 4sav log
    await message.answer_poll(
        question="Question: What can be broken, but is never held?",
        options=["Air", "Promise", "Water"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 5sav log
    await message.answer_poll(
        question="Question: What is it that lives if it is fed, and dies if you give it a drink?",
        options=["Computer", "Fire", "Chicken"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )






@dp.message_handler(text=["Random"])
async def send_welcome(message: types.Message):

    await message.answer('Start!')

    await asyncio.sleep(5)
    
    # 1sav rdm
    await message.answer_poll(
        question="If A is for alpha, B is for bravo what is C?",
        options=["Cecil", "Charlie", "Cash"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )

    await asyncio.sleep(5)

    # 2sav rdm
    await message.answer_poll(
        question="What is the slowest competitive swimming stroke?",
        options=["Butterfly", "Freestyle", "Breast stroke"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)

    # 3sav rdm
    await message.answer_poll(
        question="What is the capital city of Denmark?",
        options=["Copenhagen", "Stockholm", "Oslo"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )

    await asyncio.sleep(5)

    # 4sav rdm
    await message.answer_poll(
        question="Who discovered penicillin?",
        options=["Louis Pasteur", "Marie Curie", "Alexander Fleming"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)

    # 5sav rdm
    await message.answer_poll(
        question="Which is the hardest bone to break in the human body?",
        options=["Femur (thigh bone)", "Jaw bone", "Collar bone"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )
    
    await asyncio.sleep(5)

    # 6sav rdm
    await message.answer_poll(
        question="Poseidon was the Greek god of what?",
        options=["The sea", "Mountains", "Winds"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )
    
    await asyncio.sleep(5)

    # 7sav rdm
    await message.answer_poll(
        question="What country has Nuuk as its capital city?",
        options=["Iceland", "Alaska", "Greenland"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )

    await asyncio.sleep(5)
    
    # 8sav rdm
    await message.answer_poll(
        question="What name is given to the widow of a king?",
        options=["A consort", "A dowager", "A spinster"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=1
    )
        
    await asyncio.sleep(5)

    # 9sav rdm
    await message.answer_poll(
        question="What is the olfactory sense?",
        options=["Smell", "Taste.", "Touch"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )
        
    await asyncio.sleep(5)

    # 10sav rdm
    await message.answer_poll(
        question="Who wrote “Annie’s Song”?",
        options=["Dolly Parton", "John Denver", "Willie Nelson"],
        is_anonymous=False,
        type='quiz',
        correct_option_id=0
    )
    


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer(""" Hi bud!
 I see you need some help!
 To see what I can tap here -> "/start".

 If you have some problems or advices you can talk to admin.
 Here is his username -> "https://t.me/SeySomething"
 Anyway! Good luck!""")
    











@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)