import functools
from telethon import events
from morphobot import *

bothandler = Config.BOT_HANDLER


def morphobot_cmd(add_cmd, is_args=False):
    def cmd(func):
        morphobot = bot.tgbot
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        elif is_args == "simp":
            pattern = bothandler + add_cmd + " (.*)"
        elif is_args == "nope":
            pattern = bothandler + add_cmd
        elif is_args == "snips":
            pattern = bothandler + add_cmd + " (\S+)"
        else:
            pattern = bothandler + add_cmd + "$"
        morphobot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd


def is_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            morphobot = bot.tgbot
            perms = await morphobot.get_permissions(event.chat_id, event.sender_id)
            user = event.sender_id
            ForGo10 = bot.uid
            if perms.is_admin:
                await func(event)
            if event.sender_id == ForGo10:
                pass
            elif not user:
                pass
            if not perms.is_admin:
                await event.reply("Only Admins Can Use This..")

        return wrapper

    return decorator


def is_bot_admin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            morphobot = bot.tgbot
            boat = await morphobot.get_me()
            perms = await morphobot.get_permissions(event.chat_id, boat)
            if perms.is_admin:
                await func(event)
            else:
                await event.reply("Need Admin privileges to do this...")

        return wrapper

    return decorator


def allowed_users():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            minna = list(Config.SUDO_USERS)
            minna.append(bot.uid)
            if event.sender_id in minna:
                await func(event)
            else:
                await event.reply("This command can only be used by Owner and Sudo Users..")

        return wrapper

    return decorator


def owner_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            watashi = bot.uid
            if event.sender_id == watashi:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def only_groups():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                await event.reply("I don't think this is a group !!")

        return wrapper

    return decorator


def only_group():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def allowed_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            minna = list(Config.SUDO_USERS)
            minna.append(bot.uid)
            if event.sender_id in minna:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


def privates():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                pass
            else:
                await func(event)

        return wrapper

    return decorator
