import discord
from discord.ext import commands
import random
from quote import quotes
from pokemon import pokemon
import psycopg2
import urbandictionary as u
import esto as e
import psycopg2

client = discord.Client()
bot = commands.Bot(command_prefix='%', pm_help=True)
conn = psycopg2.connect(dbname="quotes")
cursor = conn.cursor()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print('------')
    await bot.change_presence(activity=discord.Game(name='%help'))

@bot.command()
async def quote(ctx):
    cursor.execute("""SELECT * from quotes""")
    rows = cursor.fetchall()
    x = random.choice(rows)
    await ctx.send('"' + x[1] + '" - ' + x[0])

quote.brief = "Displays a random quote by a user in the server."
quote.help = "Displays a random quote by a user in the server."

# @bot.listen()
# async def on_message(message):
#     if (str(message.author) == "Dalton Y Amaura Series#0698"):
#         channel = message.channel
#         await channel.send("*hugs Ama*")

@bot.command()
async def echo(ctx, *, arg):
    channel = bot.get_channel(427941608428797954)
    echo_log = "**" + ctx.author.name + ":** " + arg
    await ctx.send(arg)
    await channel.send(echo_log)
    await ctx.message.delete()

echo.brief = "Repeats the text inputted by the user."
echo.help = "Repeats the text inputted by the user."

@bot.command()
async def vote(ctx, *, arg):
    await ctx.message.add_reaction('👍')
    await ctx.message.add_reaction('👎')
    await ctx.message.add_reaction('🤔')

vote.brief = "Adds voting reactions to message."
vote.help = "Adds reactions to message to vote on a particular topic."

@bot.command()
async def ud(ctx, *args):
    if (len(args) == 0):
        temp = u.random()[0]
        await ctx.send("**" + temp.word + "\n" + "**" + temp.definition)
    else:
        temp = u.define(args[0])
        if (len(temp) == 0):
            await ctx.send("This word or phrase could not be found on Urban Dictionary.")
        else:
            if (len(temp[0].definition) < 2000):
                await ctx.send("**" + temp[0].word + "\n" + "**" + temp[0].definition)
            else:
                await ctx.send("This word's top definition is too long for Discord.")

ud.usage = '"word or phrase"'
ud.brief = "Returns an Urban Dictionary definition."
ud.help = "Returns Urban Dictionary definition of supplied word. If no word is supplied, returns a random word and definition."

@bot.command()
async def e621(ctx, *, args):
    if ((isinstance(ctx.channel, discord.TextChannel) and ctx.channel.is_nsfw()) or isinstance(ctx.channel, discord.abc.PrivateChannel)):
        if "random" in args:
            args = args.replace("random ", "")
            args = args.replace(" random", "")
            if (len(args.split(" ")) == 4):
                pic = e.getdata(args + " order:random" + " -rating:s")
            else:
                pic = e.getdata(args + " order:random" + " -rating:s -scat")
        else:
            if (len(args.split(" ")) == 5):
                pic = e.getdata(args + " -rating:s")
            else:
                pic = e.getdata(args + " -rating:s -scat")
    elif (ctx.channel.name == "bot_spam" or ctx.channel.name == "spam"):
        if "random" in args:
            args = args.replace("random", "")
            pic = e.getdata(args + " order:random" + " rating:s")
        else:
            pic = e.getdata(args + " rating:s")

    if (pic.file_url == None):
        await ctx.send("An image matching this query could not be found on E621.")
    else:
        x = discord.Embed(title="#" + pic.id + ": " + pic.author, url=pic.file_url, colour=0x453399)
        x.set_image(url=pic.file_url)
        x.set_footer(text="https://e621.net/post/show/" + pic.id + "/")
        if (len(pic.artists) != 0):
            artists = ", ".join(pic.artists)
            x.add_field(name="Artist(s)", value=artists)
        x.add_field(name="Score", value=pic.score)
        x.add_field(name="URL", value=pic.file_url)
        await ctx.send(embed = x)

@bot.command()
async def nuke(ctx):
    is_mod = False
    for x in ctx.author.roles:
        if (x.name == "Auxiliary"):
            is_mod = True
    if (ctx.channel.name == "the_wall" and is_mod):
        await ctx.channel.purge();

nuke.usage = '%nuke'
nuke.brief = "Auxiliary-only."
nuke.help = "Purges the messages of one specific channel."

@bot.command()
async def bf(ctx, *, args):
    inp = args[args.find("(")+1:args.find(")")]
    "".join(inp.split())
    args = args.split()
    arr = [0] * 30000
    index = 0
    res = ""
    await helper(inp, arr, index, args[1:], ctx, res)

async def helper(inp, cells, index, args, ctx, res):
    if not inp:
        if (res == ""):
            return
        await ctx.send(res)
        return
    elif (inp[0] == '+'):
        cells[index] += 1
        await helper(inp[1:], cells, index, args, ctx, res)
    elif (inp[0] == '-'):
        cells[index] -= 1
        await helper(inp[1:], cells, index, args, ctx, res)
    elif (inp[0] == '>'):
        await helper(inp[1:], cells, index+1, args, ctx, res)
    elif (inp[0] == '<'):
        await helper(inp[1:], cells, index-1, args, ctx, res)
    elif (inp[0] == '.'):
        res += chr(cells[index])
        await helper(inp[1:], cells, index, args, ctx, res)
    elif (inp[0] == ','):
        if (args == []):
            await ctx.send("Too few arguments supplied.")
            return
        cells[index] = ord(args[0])
        await helper(inp[1:], cells, index, args[1:], ctx, res)
    elif (inp[0] == '['):
        new_str = inp[1:inp.find("]")]
        for i in range(int(cells[index])):
            await helper(new_str, cells, index, args, ctx, res)
        await helper(inp[inp.find("]")+1:], cells, index, args, ctx, res)
    else:
        await ctx.send("BrainFuck code not recognized.")
        return



#################################################################
#                                                               #
#                                                               #
#                                                               #
#                                                               #
# This section contains all of the code for generating sprites. #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#################################################################




@bot.command()
async def add(ctx, arg1, arg2):
    is_mod = False
    for x in ctx.author.roles:
        if (x.name == "Auxiliary"):
            is_mod = True
    if (is_mod):
        query = "INSERT INTO quotes (username, quote, id) VALUES (%s, %s, %s);"
        cursor.execute("""SELECT * from quotes""")
        rows = cursor.fetchall()
        data = (arg1, arg2, int(rows[len(rows)-1][2]) + 1)
        cursor.execute(query, data)
        conn.commit()
        await ctx.send("Quote added!")
    else:
        await ctx.send("You do not have the correct permissions to use this command.")

add.usage = '[User] "quote"'
add.brief = "Adds a quote to Gary."
add.help = "Adds a quote to Gary's database."

@bot.command()
async def delete(ctx, arg):
    is_mod = False
    for x in ctx.author.roles:
        if (x.name == "Auxiliary"):
            is_mod = True
    if (is_mod):
        cursor.execute("DELETE FROM quotes WHERE id={};".format(arg))
        conn.commit()
        await ctx.send("Quote deleted!")
    else:
        await ctx.send("You do not have the correct permissions to use this command.")

delete.usage = '[ID #]'
delete.brief = "Deletes a quote from Gary."
delete.help = "Deletes a quote from Gary's database."

@bot.command()
async def ids(ctx):
    is_mod = False
    for x in ctx.author.roles:
        if (x.name == "Auxiliary"):
            is_mod = True
    if (is_mod):
        cursor.execute("""SELECT quote, id from quotes""")
        rows = cursor.fetchall()
        lst = []
        for r in rows:
            t = str(r[1])
            x = t + ": " + r[0]
            lst.append(x)
        s = "\n".join(lst)
        conn.commit()
        await ctx.send(s[0:1967])
        await ctx.send(s[1968:])
    else:
        await ctx.send("You do not have the correct permissions to use this command.")

ids.brief = "Lists the quote IDs."
ids.help = "Lists the quote IDs from Gary's database."




#################################################################
#                                                               #
#                                                               #
#                                                               #
#                                                               #
# This section contains all of the code for generating sprites. #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#################################################################




@bot.command()
async def pmd(ctx, arg):
    if (int(arg) < 1 or int(arg) > 807):
        await ctx.send("Index out of bounds.")
        return
    elif (int(arg) == 721):
        await ctx.send("Volcanion has not appeared in a PMD game.")
        return
    elif (int(arg) > 721 and int(arg) < 808):
        await ctx.send("Gen VII Pokemon have not yet appeared in PMD games.")
        return
    elif (int(arg) < 10):
        arg = "00" + str(arg)
    elif (int(arg) < 100):
        arg = "0" + str(arg)
    x = "https://serebii.net/supermysterydungeon/pokemon/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

ud.usage = "[PokeDex #]"
ud.brief = "Displays the given Pokemon's Mystery Dungeon icon."
ud.help = "Displays the given Pokemon's Mystery Dungeon icon."

@bot.command()
async def rb(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/red-blue/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    if arg in pokemon:
        if (int(pokemon[arg]) > 151):
            await ctx.send("This Pokemon did not exist in Red/Blue.")
            return
        await ctx.send(embed = y)
    else:
        await ctx.send("Your input is either not a Pokemon or not yet added to the list of Pokemon.")

rb.usage = "[Pokemon]"
rb.brief = "Displays the given Pokemon's sprite from Red/Blue."
rb.help = "Displays the given Pokemon's sprite from Red/Blue."

@bot.command()
async def yellow(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/yellow/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    if arg in pokemon:
        if (int(pokemon[arg]) > 151):
            await ctx.send("This Pokemon did not exist in Yellow.")
            return
        await ctx.send(embed = y)
    else:
        await ctx.send("Your input is either not a Pokemon or not yet added to the list of Pokemon.")

yellow.usage = "[Pokemon]"
yellow.brief = "Displays the given Pokemon's sprite from Yellow."
yellow.help = "Displays the given Pokemon's sprite from Yellow."

@bot.command()
async def silver(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/silver/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    if arg in pokemon:
        if (int(pokemon[arg]) > 251):
            await ctx.send("This Pokemon did not exist in Silver.")
            return
        await ctx.send(embed = y)
    else:
        await ctx.send("Your input is either not a Pokemon or not yet added to the list of Pokemon.")

silver.usage = "[Pokemon]"
silver.brief = "Displays the given Pokemon's sprite from Silver."
silver.help = "Displays the given Pokemon's sprite from Silver."

@bot.command()
async def gold(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/gold/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    if arg in pokemon:
        if (int(pokemon[arg]) > 251):
            await ctx.send("This Pokemon did not exist in Gold.")
            return
        await ctx.send(embed = y)
    else:
        await ctx.send("Your input is either not a Pokemon or not yet added to the list of Pokemon.")

gold.usage = "[Pokemon]"
gold.brief = "Displays the given Pokemon's sprite from Gold."
gold.help = "Displays the given Pokemon's sprite from Gold."

@bot.command()
async def crystal(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/crystal/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    if arg in pokemon:
        if (int(pokemon[arg]) > 251):
            await ctx.send("This Pokemon did not exist in Crystal.")
            return
        await ctx.send(embed = y)
    else:
        await ctx.send("Your input is either not a Pokemon or not yet added to the list of Pokemon.")

crystal.usage = "[Pokemon]"
crystal.brief = "Displays the given Pokemon's sprite from Crystal."
crystal.help = "Displays the given Pokemon's sprite from Crystal."

@bot.command()
async def rse(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/ruby-sapphire/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

rse.usage = "[Pokemon]"
rse.brief = "Displays the given Pokemon's sprite from R/S/E."
rse.help = "Displays the given Pokemon's sprite from Ruby/Sapphire/Emerald."

@bot.command()
async def frlg(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/firered-leafgreen/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

frlg.usage = "[Pokemon]"
frlg.brief = "Displays the given Pokemon's sprite from FR/LG."
frlg.help = "Displays the given Pokemon's sprite from FireRed/LeafGreen."

@bot.command()
async def dppt(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/diamond-pearl/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

dppt.usage = "[Pokemon]"
dppt.brief = "Displays the given Pokemon's sprite from D/P/Pt."
dppt.help = "Displays the given Pokemon's sprite from Diamond/Pearl/Platinum."

@bot.command()
async def hgss(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/heartgold-soulsilver/normal/" + arg + ".png"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

hgss.usage = "[Pokemon]"
hgss.brief = "Displays the given Pokemon's sprite from HG/SS."
hgss.help = "Displays the given Pokemon's sprite from HeartGold/SoulSilver."

@bot.command()
async def bw(ctx, arg):
    arg = arg.lower()
    x = "https://img.pokemondb.net/sprites/black-white/anim/normal/" + arg + ".gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

bw.usage = "[Pokemon]"
bw.brief = "Displays the given Pokemon's sprite from Black/White."
bw.help = "Displays the given Pokemon's sprite from Black/White."

@bot.command()
async def xy(ctx, arg):
    arg = arg.lower()
    if arg in pokemon:
        if (int(pokemon[arg]) > 721):
            await ctx.send("This Pokemon did not exist in X/Y.")
            return
    await xysm(ctx, arg)

xy.usage = "[Pokemon]"
xy.brief = "Displays the given Pokemon's sprite from X/Y."
xy.help = "Displays the given Pokemon's sprite from X/Y."

@bot.command()
async def sm(ctx, arg):
    arg = arg.lower()
    await xysm(ctx, arg)

sm.usage = "[Pokemon]"
sm.brief = "Displays the given Pokemon's sprite from Sun/Moon."
sm.help = "Displays the given Pokemon's sprite from Sun/Moon."

async def xysm(ctx, arg):
    x = "https://play.pokemonshowdown.com/sprites/xyani/" + arg + ".gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)



####################################################################
#                                                                  #
#                                                                  #
#                                                                  #
#                                                                  #
# The following section contains commands for each individual user #
#                                                                  #
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################



@bot.command()
async def sig(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/gliscor.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def flames(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/lopunny.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def diamond(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/glaceon.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def odd(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/slowpoke.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def hecc(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani-shiny/gourgeist.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def fluffy(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def surv(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/luxray.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def dom(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/charizard.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def psych(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/slaking.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def ama(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/amaura.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def bounty(ctx):
    x = "http://play.pokemonshowdown.com/sprites/xyani-shiny/porygon-z.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def mako(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/primarina.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def timo(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/shaymin-sky.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def cell(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/gengar.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def dragon(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani-shiny/latios.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def gex(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/treecko.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def tallow(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/zangoose.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def frogger(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def alaska(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/lurantis.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def minty(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/archen.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def meth(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/mawile.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def hayden(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/infernape.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def nas(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/leafeon.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def nathan(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/goodra.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def zytomic(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/lurantis.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def testin(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/serperior.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def gary(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/gyarados.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def ivee(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/ditto.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def patrician(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/bronzong.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def drag(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/sylveon.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def curtis(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/reuniclus.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def seymour(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/altaria.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def fooni(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/froslass.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def ace(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/suicune.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def cones(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/vanillite.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def coco(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/plusle.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def kyro(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/espurr.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def snivez(ctx):
    x = "https://play.pokemonshowdown.com/sprites/xyani/braixen.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def sea(ctx):
    x = "http://play.pokemonshowdown.com/sprites/xyani-shiny/litten.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def cross(ctx):
    x = "http://play.pokemonshowdown.com/sprites/xyani/gallade.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

@bot.command()
async def fox(ctx):
    x = "http://play.pokemonshowdown.com/sprites/xyani/ninetales.gif"
    y = discord.Embed()
    y.set_image(url=x)
    await ctx.send(embed = y)

bot.run('NDEwMjM1NjgxMTA2MDM0Njg5.DVqNRA.5hICSESXedjhaue_vwXYu0JqVDY')
