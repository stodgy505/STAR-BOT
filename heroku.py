prefix = "$"
import discord
import random

client = discord.Client()


@client.event
async def on_message(message):


    # Dont let the bot reply to itself
    if message.author == client.user:
        return

    # Simple Help Command...
    if message.content.startswith(prefix + 'help'):
        msg = '''***```FUN COMMANDS
        $help            ---->  gives the user the commands
        $slap @user#0000 ---->  slaps a user
        $hit @user#0000  ---->  hits a user
        $kill @user#0000 ---->  kills a user
        $hug @user#0000  ---->  hugs a user
        $pat @user#0000  ---->  pats a user
        $connect4        ---->  plays connect4 with computer
        $CTS             ---->  tests ur CPS which is clicks per sec.
        $dieplinks       ---->  sends u to the dieppartylinks page
        $discord         ---->  send u invite to the developers server
        $delmsg          ---->  for spammers or to delete silly stuff
        $guess           ---->  guess the number game

        
               New commands will come soon :).need help , join my discord server```***'''
        await client.send_message(message.channel, msg)

    # Guess the number minigame...

    if message.content.startswith(prefix +'guess'):
        await client.send_message(message.channel, "Guess a number between 1 to 10")
        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=10.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            msg = 'Sorry,it took u over 10 seconds to answer :('
            await client.send_message(message.channel, msg)
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'correct!')
        else:
            await client.send_message(message.channel, 'nope :(. It is actually {}.'.format(answer))

    if message.content.startswith(prefix + 'hit'):
        msg = 'u have been hit by {0.author.mention}\nhttps://www.tenor.co/S2eB.gif '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'hug'):
        msg = 'u have been hugged by {0.author.mention}\nhttps://www.tenor.co/vfFB.gif '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'kill'):
        msg = 'u have been killed by {0.author.mention}\nhttps://www.tenor.co/Mza0.gif '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'pat'):
        msg = 'u have been patted by {0.author.mention}\nhttps://www.tenor.co/rjm5.gif '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'slap'):
        msg = 'u have been slapped by {0.author.mention}\nhttps://www.tenor.co/RTqL.gif'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'CTS'):
        msg = 'https://www.click-test.com/p/clicks-in-60-se.html'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'connect4'):
        msg = 'https://www.mathsisfun.com/games/connect4.html'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'dieplinks'):
        msg = 'https://www.reddit.com/r/DiepioPartyLinks/new/'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith(prefix + 'discord'):
        msg = 'https://discord.gg/SwWEPBm'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(prefix + 'delmsg'):
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    client.run(os.getenv('token'))
        
