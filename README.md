# No Context Bot

What is No Context Bot? It is a bot that randomly picks a new discord message every 10 minutes, and tweets that to twitter. 
It is exclusively for the No Context Discord server, which can be joined right here: discord.gg/tStrPZB

How does the selective process work? First, it uses the `client.logs_from()` to pick the most recent 25 posts, and then turns
it into a list, in which `random.choice(logs)` is now used. After that, it gets a random item in the list, and tweets it to twitter using the 
imported twitter package, by doing `TwitApi.PostUpdate(message.content or " ",media=attaches)`. This process allows
new posts to be added and old posts to be burried or discovered, but also for the twitter account to keep on posting, non-stop every 10 minutes.

**README Keys**
RSCL = Reserved for Client Owner(Robuyasu)

**Current Version: 1.2.5**

## Commands
The current commands for the bot are as shows:

### _ClientOwnerOnly_
**!bootdown**
RSCL, and stops the process of tweeting. Only used for emergencies or reworkings.
Example: 
`!bootdown`

**!bootup**
RSCL, and starts/recontinues the process of tweeting. 
Example: 
`!bootup`

**!post**
RSCL, and posts a message to twitter.
Example: 
`!post This is a test message.`

**!ppost**
RSCL, and is used to check/test the post command and its properties.
Example:
`!ppost This is a test message.`

**!getmessages**
RSCL, and returns all recent 100 messages in #discord-says
example:
`!getmessages`

### _ModeratorOnly_
**!kick**
Kicks the chosen player out of the server.
Example:
`!kick @robuyasu#3100`

**!ban**
Bans the chosen player out of the server.
Example:
`!ban @robuyasu#3100`

### _UserAccessible_
**!version**
Returns the version of the bot, by responding back to the user.
Example:
`!version`

**!about**
DMs the message author of the bot credentials, which shows the bot version, github page, and more info.
Example: 
`!about`
