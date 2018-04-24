import discord
from discord.ext import commands


class GeneralCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):
        channel = ctx.message.author.dm_channel
        if (channel == None):
            await ctx.message.author.create_dm()
            channel = ctx.message.author.dm_channel
        await channel.trigger_typing()

        gen = """ `%help`\n Displays this message!\n
`%quote [id (optional)]`\n Displays the quote with the specified ID. If none is given, a random quote is returned.\n
`%echo`\n Repeats the text inputted by the user.\n
`%vote`\n Initiates a vote using the 👍, 👎, and 🤔 reactions.\n
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
        msg.add_field(name="General Commands", value=gen, inline=False)
        msg.add_field(name="Admin Commands", value=db, inline=False)
        msg.add_field(name="Sprite Commands", value=sprites, inline=False)
        msg.add_field(name="User Commands", value=users, inline=False)
        await channel.send(embed = msg)

    @commands.command()
    async def echo(self, ctx, *, arg):
        channel = self.bot.get_channel(427941608428797954)
        echo_log = "**" + ctx.author.name + ":** " + arg
        await ctx.send(arg)
        await channel.send(echo_log)
        await ctx.message.delete()

    @commands.command()
    async def vote(self, ctx, *, arg):
        channel = self.bot.get_channel(427941608428797954)
        echo_log = "**" + ctx.author.name + ":** " + arg
        msg = await ctx.send(arg)
        await channel.send(echo_log)
        await ctx.message.delete()
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('🤔')


def setup(bot):
    bot.add_cog(GeneralCog(bot))
