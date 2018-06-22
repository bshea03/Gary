import discord
from discord.ext import commands
from imgurpython import ImgurClient
import random
from cogs.utils.imgur_key import client_id, client_key

class ImgurCog:
    def __init__(self, bot):
        self.bot = bot
        self.client = ImgurClient(client_id, client_key)

    async def _images(self, ctx, id):
        album = self.client.get_album_images(id)
        image = random.choice(album)
        embed = discord.Embed()
        embed.set_image(url=image.link)
        await ctx.send(embed=embed)

    @commands.command()
    async def baned(self, ctx):
        await self._images(ctx, '72bJM')

    @commands.command(aliases=["loc"])
    async def location(self, ctx):
        await self._images(ctx, 'coJunoC')

    @commands.command(aliases=["zard"])
    async def charizard(self, ctx):
        await self._images(ctx, 'zlShR')

    @commands.command(aliases=["glisc", "scor"])
    async def gliscor(self, ctx):
        await self._images(ctx, 'EG51a5j')

    @commands.command(aliases=["esca"])
    async def escavalier(self, ctx):
        await self._images(ctx, 'WTWC33A')

    @commands.command(aliases=["serp", "snek"])
    async def serperior(self, ctx):
        await self._images(ctx, 'jRy06di')

def setup(bot):
    bot.add_cog(ImgurCog(bot))
