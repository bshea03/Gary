import discord
from discord.ext import commands
import random


class GeneralCog:
    def __init__(self, bot):
        self.bot = bot

    async def _lastfm_help(self, ctx):
        channel = ctx.message.author.dm_channel
        if (channel == None):
            channel = await ctx.message.author.create_dm()
        await channel.trigger_typing()
        lfm = """ `%artist [artist name]`\n Displays information on the given artist.\n
`%top_albums [artist name]`\n Displays the top five albums by the given artist.\n
`%top_tracks [artist name]`\n Displays the top five tracks by the given artist.\n
`%album [album name] - [artist name]`\n Displays information on the given album as well as a tracklist.\n
`%track [track name] - [artist name]`\n Displays information on the given track as well as a playable Spotify link.\n\u200b"""

        msg = discord.Embed(description="The following is a list of Last.fm commands that can be used with Gary.", colour=0x33B5E5)
        msg.set_footer(text="For any additional inquiries, please DM Sigma#0472.")
        msg.set_author(name="Gary Help Menu", icon_url="https://i.neoseeker.com/mgv/297579/579/118/lord_garyVJPHT_display.png")
        msg.add_field(name="Last.fm Commands", value=lfm, inline=True)
        await channel.send(embed=msg)

    async def _help_redirect(self, ctx, args):
        if args[0] == 'last.fm':
            await self._lastfm_help(ctx)
        else:
            return

    @commands.command()
    async def userinfo(self, ctx, *args):
        await ctx.channel.trigger_typing()

        author = ctx.author

        if args:
            author = None
            if args[0][0:3] == "<@!":
                author = ctx.guild.get_member(int(args[0][3:len(args[0])-1]))
            elif args[0][0:2] == "<@":
                author = ctx.guild.get_member(int(args[0][2:len(args[0])-1]))
            else:
                args = " ".join(args)
                for m in ctx.guild.members:
                    if args == m.name + "#" + m.discriminator:
                        author = m
                        break
            if author == None:
                await ctx.send("User not found in this server.")
                return

        msg = discord.Embed(colour=author.color)
        msg.set_author(name=author.name, icon_url=author.avatar_url)
        msg.set_thumbnail(url=author.avatar_url)
        msg.add_field(name="User ID", value=author.name + "#" + str(author.discriminator))
        msg.set_footer(text="For help with Gary's commands, use %help.")
        msg.add_field(name="Nickname", value=author.nick)
        msg.add_field(name="Join Date", value=str(author.joined_at)[:10])
        msg.add_field(name="Account Created", value=str(author.created_at)[:10])
        msg.add_field(name="Status", value=str(author.status).title())
        msg.add_field(name="Roles", value=", ".join(r.name for r in reversed(author.roles)))

        await ctx.send(embed=msg)

    @commands.command()
    async def help(self, ctx, *args):
        if args:
            await self._help_redirect(ctx, args)
            return
        channel = ctx.message.author.dm_channel
        if (channel == None):
            channel = await ctx.message.author.create_dm()
        await channel.trigger_typing()

        gen = """ `%help [string (optional)]`\n Displays this message. If given an argument, displays information on the given command(s). Valid arguments are:\n`last.fm` \n
`%quote [id (optional)]`\n Displays the quote with the specified ID. If none is given, a random quote is returned.\n
`%echo [string]`\n Repeats the text inputted by the user.\n
`%vote`\n Initiates a vote using the 👍, 👎, and 🤔 reactions.\n
`%roll [# sides (optional)]`\n Displays a random number in the given range (six by default).\n
`%flip`\n Returns "Heads" or "Tails" at random.\n
`%oracle`\n Magic 8-Ball.\n
`%ud [word or phrase (optional)]`\n Returns Urban Dictionary definition of supplied word. If no word is supplied, returns a random word and definition.\n
`%e621 [query]`\n Returns the top e621 image of the given query. Can only be used in #bot_spam (SFW) and #nsfw_pics (NSFW).\n\u200b"""

        db = """ `%add [user] [quote]`\n Auxiliary only. Adds a new quote to Gary's list.\n
`%delete [id]`\n Auxiliary only. Deletes a quote from Gary's list.\n
`%ids`\n DMs the user a list of quotes and their IDs.\n\u200b"""

        sprites = """`%pmd [pokedex #]`\n Displays the PMD icon of the given Pokemon.\n
`%[pokemon game] [pokemon]`\n Displays the sprite of the given pokemon from the specified game. Valid commands are:
`%rb`, `%yellow`, `%gold`, `%silver`, `%crystal`, `%rse`, `%frlg`, `%dppt`, `%hgss`, `%bw`, `%xy`, `%sm`.\n\u200b"""

        users = """`%[user]`\n Displays the pokemon commonly associated with the specified user.
If your name does not yet have a command, DM Sigma with the pokemon you want.\n\u200b"""

        msg = discord.Embed(description="The following is a list of commands that can be used with Gary.", colour=0x33B5E5)
        msg.set_footer(text="For any additional inquiries, please DM Sigma#0472.")
        msg.set_author(name="Gary Help Menu", icon_url="https://i.neoseeker.com/mgv/297579/579/118/lord_garyVJPHT_display.png")
        msg.add_field(name="General Commands", value=gen, inline=True)
        msg.add_field(name="Admin Commands", value=db, inline=True)
        msg.add_field(name="Sprite Commands", value=sprites, inline=True)
        msg.add_field(name="User Commands", value=users, inline=True)
        await channel.send(embed = msg)

    @staticmethod
    async def _err_catch(ctx, err, format, desc):
        channel = ctx.message.author.dm_channel
        if channel == None:
            channel = await ctx.message.author.create_dm()
        x = discord.Embed(colour=0x33B5E5, title=err, description='`' + format + '`\n')
        x.add_field(name=desc, value="\u200b")
        x.set_author(name="Gary Command Error", icon_url="https://i.neoseeker.com/mgv/297579/579/118/lord_garyVJPHT_display.png")
        x.set_footer(text="Please use %help or DM Sigma#0472 with any further questions.")
        await channel.send(embed = x)

    @commands.command()
    async def roll(self, ctx, *args):
        if (len(args) == 0):
            await ctx.send(random.randint(1,6))
        else:
            try:
                await ctx.send(random.randint(1,int(args[0])))
            except ValueError:
                err = "Invalid argument type."
                format = "%roll [# sides (optional)]"
                desc = "The %roll command displays a random number in the given range (six by default)."
                await self._err_catch(ctx, err, format, desc)

    @commands.command()
    async def flip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @commands.command()
    async def oracle(self, ctx):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes, definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful"]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def bigtext(self, ctx, *args):
        channel = self.bot.get_channel(427941608428797954)
        if not args:
            err = "Missing required argument."
            format = "%echo [string]"
            desc = "The %echo command repeats the text inputted by the user.."
            await self._err_catch(ctx, err, format, desc)
            return
        args = " ".join(args)
        echo_log = "**" + ctx.author.name + ":** " + args
        str = []
        args = args.lower()

        misc = {'0': ":zero:", '1': ":one:",'2': ":two:", '3': ":three:",
                '4': ":four:",'5': ":five:", '6': ":six:", '7': ":seven:",
                '8': ":eight:", '9': ":nine:", ' ': "   ", '*': ":asterisk:",
                '#': ":hash:", '?': ":question:", '!': ":exclamation:"}

        for x in args:
            if (x.isalpha()):
                str.append(":regional_indicator_{}:".format(x.lower()))
            elif x in misc:
                str.append(misc[x])
            else:
                continue

        str = "".join(str)
        await ctx.send(str)
        await channel.send(echo_log)
        await ctx.message.delete()


    @commands.command()
    async def echo(self, ctx, *args):
        channel = self.bot.get_channel(427941608428797954)
        if not args:
            err = "Missing required argument."
            format = "%echo [string]"
            desc = "The %echo command repeats the text inputted by the user.."
            await self._err_catch(ctx, err, format, desc)
            return
        arg = " ".join(args)
        echo_log = "**" + ctx.author.name + ":** " + arg
        await ctx.send(arg)
        await channel.send(echo_log)
        await ctx.message.delete()

    @commands.command()
    async def vote(self, ctx, *args):
        channel = self.bot.get_channel(427941608428797954)
        if not args:
            err = "Missing required argument."
            format = "%vote [string]"
            desc = "The %vote command initiates a vote using the 👍, 👎, and 🤔 reactions."
            await self._err_catch(ctx, err, format, desc)
            return
        arg = " ".join(args)
        echo_log = "**" + ctx.author.name + ":** " + arg
        msg = await ctx.send(arg)
        await channel.send(echo_log)
        await ctx.message.delete()
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('🤔')

    @commands.command(hidden=True)
    async def nuke(self, ctx):
        is_mod = False
        for x in ctx.author.roles:
            if (x.name == "Auxiliary"):
                is_mod = True
        if (ctx.channel.name == "the_wall" and is_mod):
            await ctx.channel.purge();


def setup(bot):
    bot.add_cog(GeneralCog(bot))
