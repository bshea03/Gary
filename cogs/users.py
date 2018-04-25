import discord
from discord.ext import commands


class UserCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["sig", "swiggy"])
    async def sigma(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/gliscor.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["flames", "flam"])
    async def flamesonfire(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/lopunny.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["dia", "diamy_waimy"])
    async def diamond(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/glaceon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["odd"])
    async def oddball(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/slowpoke.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def hecc(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani-shiny/gourgeist.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["fluff"])
    async def fluffy(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["surv"])
    async def survivalist(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/luxray.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["dommy"])
    async def dom(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/charizard.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["psych", "vap", "pro_spy", "hungery", "giv_food"])
    async def kingpsych(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/vaporeon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def ama(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/amaura.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def bounty(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani-shiny/porygon-z.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def mako(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/primarina.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["min"])
    async def timo(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/shaymin-sky.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def cell(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/gengar.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def dragon(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani-shiny/latios.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def gex(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/treecko.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["tal"])
    async def tallow(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/zangoose.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["frogger"])
    async def captainfrogger(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def alaska(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/lurantis.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def minty(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/archen.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["meth", "mawile", "maw"])
    async def metheria(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/mawile.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["nape"])
    async def hayden(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/infernape.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def nas(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["lube_dragon"])
    async def nathan(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/goodra.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["zytom"])
    async def zytomic(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/lurantis.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def testin(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/serperior.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["shitbot", "gay"])
    async def gary(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/gyarados.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def ivee(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/ditto.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["pat"])
    async def patrician(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/bronzong.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["drag"])
    async def dragtarded(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/sylveon.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["110percent"])
    async def curtis(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/reuniclus.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["sey"])
    async def seymour(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/altaria.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def fooni(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/froslass.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["ace"])
    async def acefyre(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/suicune.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def cones(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/vanillite.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["coco"])
    async def cocoba(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/plusle.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def kyro(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/espurr.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["snive"])
    async def snivez(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/braixen.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["sea"])
    async def seacasro(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani-shiny/litten.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["cross"])
    async def crossbow(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/gallade.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["foccs"])
    async def fox(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/ninetales.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["teal"])
    async def navy(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/escavalier.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["run"])
    async def runtime(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/lapras.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["insig"])
    async def insigturtle(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/quilava.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def daven(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani/samurott.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command(aliases=["min2"])
    async def mewn(self, ctx):
        x = "https://play.pokemonshowdown.com/sprites/xyani/shaymin-sky.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

    @commands.command()
    async def bunches(self, ctx):
        x = "http://play.pokemonshowdown.com/sprites/xyani-shiny/chimchar.gif"
        y = discord.Embed()
        y.set_image(url=x)
        await ctx.send(embed = y)

def setup(bot):
    bot.add_cog(UserCog(bot))
