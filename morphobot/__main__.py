import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from morphobot import LOGS, bot, tbot
from morphobot.config import Config
from morphobot.utils import load_module
from morphobot.version import __morpho__ as hellver
hl = Config.HANDLER
MORPHO_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/c14f64e88cc9bc3f07f3a.jpg"

# let's get the bot ready
async def morpho

morpho_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"MORPHOBOT_SESSION - {str(e)}")
        sys.exit()


# morphobot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🇮🇳 Starting morphoBot 🇮🇳")
            bot.loop.run_until_complete(morpho_bot(Config.BOT_USERNAME))
            LOGS.info("🔥😈 MorphoBot Startup Completed 😈🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "morphobot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/BIHARIBABUHU/pikachu_userbot"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "morphobot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("😏 Your MorphoBot Is Now Working 😘")
LOGS.info(
    "Head to @team_morpho_userbot for Updates. Also join chat group to get help regarding to Morpho user Bot."
)

# that's life...
async def morpho_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                MORPHO_PIC,
                caption=f"#START \n\nDeployed MORPHOBOT Successfully\n\n**MORPHOBOT - {morphover}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [MORPHOBOT Channel](t.me/team_morpho_userbot) for Updates & [MORPHOBOT Chat](t.me/morpho_userbot_chat) for any query regarding MORPHOBOT†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join MorphoBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@team_morpho_userbot"))
    except BaseException:
        pass

# Why not come here and chat??
    #try:
        #await bot(JoinChannelRequest("@morpho_userbot_chat"))
    #except BaseException:
        #pass


bot.loop.create_task(morpho_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# morphobot
