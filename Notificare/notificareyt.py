# -*- coding: utf-8 -*-
from redbot.core import commands
from datetime import datetime, timedelta, timezone
from pytz import timezone
import discord

class Notificare(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.mod()
    @commands.command(name="blocarechat")
    async def blocarechat(self, ctx):
        data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=False, mention_everyone=False)
        embed = discord.Embed(title="Blocare chat 🤫", color=0xefe125)
        embed.add_field(name="NUME", value="ID", inline=True)
        embed.add_field(name=str(ctx.author.name), value=str(ctx.author.id), inline=True)
        embed.set_footer(text=str(data_log))
        await ctx.message.author.send("Chat-ul a fost blocat!")
        await logs_channel.send(embed=embed)
    
    @commands.mod()
    @commands.command(name="deblocarechat")
    async def deblocarechat(self, ctx):
        data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=None, mention_everyone=False)
        embed = discord.Embed(title="Deblocare chat 🤫", color=0xefe125)
        embed.add_field(name="NUME", value="ID", inline=True)
        embed.add_field(name=str(ctx.author.name), value=str(ctx.author.id), inline=True)
        embed.set_footer(text=str(data_log))
        await ctx.message.author.send("Chat-ul a fost deblocat!")
        await logs_channel.send(embed=embed)
    
    @commands.mod()
    @commands.command(name="notificareyoutube")
    async def notificareyoutube(self, ctx, linkyoutube):
        channel = self.bot.get_channel(440957219593519126)
        await channel.set_permissions(ctx.guild.default_role, send_messages=False, mention_everyone=False)
        mesajfinal = "@everyone, "+linkyoutube+"\n\n:purple_heart:  Nu uitați de like, un share este binevenit și dacă nu ați făcut-o până acum, nu uita să te abonezi și să apeși clopoțelul pentru a fi întotdeauna notificat când IKatheryne face live sau postează! :purple_heart:"
        await channel.send(mesajfinal)
