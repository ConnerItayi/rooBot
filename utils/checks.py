import os
import discord.utils
from discord.ext import commands
from config import config
from utils.config import Config as conf

class No_Event(commands.CommandError): pass
class No_Appr(commands.CommandError): pass
class No_Mod(commands.CommandError): pass
class No_Super(commands.CommandError): pass
class No_Admin(commands.CommandError): pass
class No_Owner(commands.CommandError): pass
class InvalidUsage(commands.CommandError): pass

config = conf('config/config.ini')

def is_owner_check(message):
    if message.author.id == config.owner or 335677038830682112 or 168141723019640832:
        return True
    raise No_Owner()

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

def is_admin_check(message):
    if "Admin" in [role.name for role in message.author.roles]:
        return True
    elif message.author.id == config.owner:
        return True
    raise No_Admin

def is_admin():
    return commands.check(lambda ctx: is_admin_check(ctx.message))

def is_super_check(message):
    if "Supervisor" in [role.name for role in message.author.roles]:
        return True
    elif "Admin" in [role.name for role in message.author.roles]:
        return True
    elif message.author.id == config.owner:
        return True
    raise No_Super

def is_super():
    return commands.check(lambda ctx: is_super_check(ctx.message))

def is_mod_check(message):
    if "Moderator" in [role.name for role in message.author.roles]:
        return True
    elif "Supervisor" in [role.name for role in message.author.roles]:
        return True
    elif "Admin" in [role.name for role in message.author.roles]:
        return True
    elif message.author.id == config.owner:
        return True
    raise No_Mod

def is_mod():
    return commands.check(lambda ctx: is_mod_check(ctx.message))

def is_appr_check(message):
    if "Apprentice" in [role.name for role in message.author.roles]:
        return True
    elif "Moderator" in [role.name for role in message.author.roles]:
        return True
    elif "Supervisor" in [role.name for role in message.author.roles]:
        return True
    elif "Admin" in [role.name for role in message.author.roles]:
        return True
    elif message.author.id == config.owner:
        return True
    raise No_Appr

def is_appr():
    return commands.check(lambda ctx: is_appr_check(ctx.message))

def is_event_check(message):
    if "Event" in [role.name for role in message.author.roles]:
        return True
    raise No_Event

def is_event():
    return commands.check(lambda ctx: is_event_check(ctx.message))