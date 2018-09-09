async def bootup(message):
    if message.author.id == RobId:
        ContextOn = True
        await client.send_message(message.channel,"Successfully booted up.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


async def bootdown(message):
    if message.author.id == RobId:
        ContextOn = False
        await client.send_message(message.channel,"Successfully booted down.")
    else:
        await client.send_message(message.channel,"You do not have the permissions to do that, %s!" % (message.author.mention))


async def post(message):
    if message.author.id == RobId:
        Content = message.content.split(" ")
        await client.send_message(message.channel,"Posting message..")
        TwitApi.PostUpdate(" ".join(Content[1:]))
        await client.send_message(message.channel,"Posted message to twitter!")

async def version(message):
    await client.send_message(message.channel,"Version: 1.0.0")

async def about(message):
    await client.send_message(message.author,'''
Hey There! I'm No Context Bot.
I was programmed by @robuyasu#3100, and was created September 9, 2018.

My purpose is to select recent messages, and tweet one of the many random recent messages.
I am coded in Python, and hosted at heroku.

Want to view my source code or help out? View https://github.com/Robuyasu/noContextBot

    ''')
