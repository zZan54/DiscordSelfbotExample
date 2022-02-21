# Discord Selfbot Example by zZan54
# github.com/zZan54

import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style

client = commands.Bot(command_prefix = ".", self_bot = True, help_command = None) #edit your prefix here
token= "TOKEN HERE"

#where to find the ascii font: https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=EXAMPLE
ex1 = Fore.RED + "                       ███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗"
ex2 = Fore.RED + "                       ██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝"
ex3 = Fore.RED + "                       █████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗  "
ex4 = Fore.GREEN + "                       ██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  "
ex5 = Fore.GREEN + "                       ███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗"
ex6 = Fore.GREEN + "                       ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝"

READY = "Example selfbot is running!"
eql = Fore.YELLOW + "═══════════════════════════════════════════════════════════════════════════════════════════════════════"
helper = Fore.WHITE + "Type .help for list with commands."
by = "selfbot example by zZan54"
gitpage = "https://github.com/zZan54"


@client.event
async def on_ready():
        print(ex1)
        print(ex2)
        print(ex3)
        print(ex4)
        print(ex5)
        print(ex6)
        print(eql)
        print("                                     ",READY)
        print(eql)
        print("                                  ",helper)
        print(eql)
        print(Fore.WHITE)
        print(by)
        print(gitpage)


@client.command()
async def help(ctx): #name of command is going here
    await ctx.message.delete() #deletes the sent msg
    await ctx.send("Hello this is just an example.") #what should bot send after the command is sent

client.run(token, bot = False)
