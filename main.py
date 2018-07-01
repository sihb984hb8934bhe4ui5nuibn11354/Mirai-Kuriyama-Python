#  ___                                      _
# |_ _|  _ __ ___    _ __     ___    _ __  | |_   ___
#  | |  | '_ ` _ \  | '_ \   / _ \  | '__| | __| / __|
#  | |  | | | | | | | |_) | | (_) | | |    | |_  \__ \
# |___| |_| |_| |_| | .__/   \___/  |_|     \__| |___/
#                   |_|
import discord
import asyncio
import random
import psutil
from random import *
from time import sleep as s
import time, datetime
import requests
import io
import safygiphy
import json
import os
from googletrans import Translator
import wikipedia

token_a = str(os.environ.get('TOKEN', None))

# __     __                 _                          _
# \ \   / /   __ _   _ __  (_)   __ _  __   __   ___  (_)  ___
#  \ \ / /   / _` | | '__| | |  / _` | \ \ / /  / _ \ | | / __|
#   \ V /   | (_| | | |    | | | (_| |  \ V /  |  __/ | | \__ \
#    \_/     \__,_| |_|    |_|  \__,_|   \_/    \___| |_| |___/
client = discord.Client()

seconds = 0
minutes = 0
hour = 0

players = {}

mcolor = 0xBF6021

msg_id = None
msg_user = None
msg_id = None

start_time = int(time.time())
version = 'Beta'
client = discord.Client()
RED = "#000000"
minutes = 0
hour = 0

blacklist = ['']
onwer = ['319567696519888898']

def wiki_summary(arg):
    wikipedia.set_lang('pt-br')
    definition = wikipedia.summary(arg, sentences=1, chars=100,
                                   auto_suggest=True, redirect=True)
    return definition
#  _        ___     ____     _               _        ___
# | |      / _ \   / ___|   | |__     ___   | |_     / _ \   _ __
# | |     | | | | | |  _    | '_ \   / _ \  | __|   | | | | | '_ \
# | |___  | |_| | | |_| |   | |_) | | (_) | | |_    | |_| | | | | |
# |_____|  \___/   \____|   |_.__/   \___/   \__|    \___/  |_| |_|

@client.event
async def on_ready():
    wikipedia.set_lang('pt-br')
    print("=================================")
    print("Nome : %s" % client.user.name)
    print("ID : %s" % client.user.id)
    print("Servidores : %s" % str(len(client.servers)))
    print("Canais : %s" % str(len(set(client.get_all_channels()))))
    print("Emojis : %s" % str(len(set(client.get_all_emojis()))))
    print("Usuários : %s" % str(len(set(client.get_all_members()))))
    print("=================================")
    await client.change_presence(game=discord.Game(name='Estou em desenvolvimento!', url='https://www.twitch.tv/deivizin_', type=1))
    #while True:
        #await client.change_presence(game=discord.Game(name='Estou em desenvolvimento!', url='https://www.twitch.tv/deivizin_', type=1))
        #await asyncio.sleep(15)

        #script = "prefixo padrão: ="
        #await client.change_presence(game=discord.Game(name=script, type=1, url='https://www.twitch.tv/deivizin_'), status='streaming')
        #await asyncio.sleep(15)

        #script2 = str(len(client.servers))+" servidores com "+str(len(set(client.get_all_members())))+" usuários, me utilizando!"
        #await client.change_presence(game=discord.Game(name=script2, type=3), status='watching')
        #await asyncio.sleep(15)

        #script3 = "Utilize =ajuda para mais informações"
        #await client.change_presence(game=discord.Game(name=script3, type=1, url='https://www.twitch.tv/deivizin_'), status='streaming')
        #await asyncio.sleep(15)

        #script4 = "encontrou algum bug? digite =servidor"
        #await client.change_presence(game=discord.Game(name=script4, type=1, url='https://www.twitch.tv/deivizin_'), status='streaming')
        #await asyncio.sleep(15)

        #script5 = "atualmente tenho: 17 comandos"
        #await client.change_presence(game=discord.Game(name=script5, type=1, url='https://www.twitch.tv/deivizin_'), status='streaming')
        #await asyncio.sleep(5)

@client.event
async def on_message(message):

#  _           __  __               _
# / |         |  \/  |   ___     __| |   ___   _ __    __ _    ___    __ _    ___
# | |  _____  | |\/| |  / _ \   / _` |  / _ \ | '__|  / _` |  / __|  / _` |  / _ \
# | | |_____| | |  | | | (_) | | (_| | |  __/ | |    | (_| | | (__  | (_| | | (_) |
# |_|         |_|  |_|  \___/   \__,_|  \___| |_|     \__,_|  \___|  \__,_|  \___/

    if message.content.lower().split()[0] == "=getban":
        if "Direct Message" in str(message.channel):
            pass
        else:
            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel,
                                             "{}, você nao possui permissão!".format(message.author.mention))
            # await client.delete_message(message)
            await client.send_typing(message.channel)
            try:
                banlist = await client.get_bans(message.server)
                if len(banlist) == 0:
                    await client.send_message(message.channel, "Esse servidor não possui usuarios banidos")
                else:
                    banlist1 = discord.Embed(title='`Banimentos do servidor {}`'.format(message.server.name),
                                         color=mcolor, description=None)

                    await client.send_message(message.channel, embed=banlist1)
                    for b in banlist:
                        responses = "{}".format(b)

                        banlist = discord.Embed(title=None,
                                            color=mcolor, description=responses)

                        await client.send_message(message.channel, embed=banlist)
            except discord.errors.Forbidden:
                ban = await client.send_message(message.channel, 'Sem permissão de ver banimentos desse servidor')
                await asyncio.sleep(10)
                await client.delete_message(ban)
            except Exception as e:
                await client.send_message(message.channel, 'Ocorreu um error : {}'.format(e))

    if message.content.lower().split()[0] == '=ban':
        if "Direct Message" in str(message.channel):
            pass
        else:
            if not message.author.server_permissions.ban_members:
                return await client.send_message(message.channel,
                                             "** Você precisa da permissão de banir algum membro!**")
            try:
                user = message.mentions[0]
                await client.send_message(message.channel, "**O usuario foi banido com sucesso do servidor.**")
                banemb = discord.Embed(
                    title="Banimento",
                    color=mcolor
                )
                banemb.add_field(name="Banido:", value=user)
                banemb.add_field(name="Motivo:", value=message.content[27:])
                banemb.add_field(name="Autor:", value=message.author.mention)
                banemb.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=banemb)
                await client.ban(user, delete_message_days=7)
            finally:
                pass

    if message.content.lower().split()[0] == '=clear':
        if "Direct Message" in str(message.channel):
            pass
        else:
            numero = str(message.content[7:])
            if not message.author.server_permissions.manage_messages:
                return await client.send_message(message.channel, +message.author.mention+", não foi possivel apagar pois você não tem permissão no servidor.")
            elif int(numero) > 100:
                return await client.send_message(message.channel, "{}, você pode apagar até **100** mensagens.".format(str("<@"+message.author.id+">")))
        msgs = []
        number = int(numero)+1
        async for x in client.logs_from(message.channel, limit=number):
            msgs.append(x)
        await client.delete_messages(msgs)
        await client.send_message(message.channel, "Foram apagadas `{}` messagens por {}!".format(numero, str("<@"+message.author.id+">")))

    if message.content.lower().split()[0] == '=mute':
        if "Direct Message" in str(message.channel):
            pass
        else:
            if not message.author.server_permissions.manage_roles:
                return await client.send_message(message.channel,
                                             "** Você precisa da permissão de gerenciar cargos!**")
            try:
                user = message.mentions[0]
                await client.send_message(message.channel, "**O usuario <@{}> foi mutado com sucesso do servidor.**".format(user.id))
                role = discord.utils.find(lambda r: r.name == "Muted", message.server.roles)
                await client.add_roles(user, role)
            finally:
                pass

    if message.content.lower().split()[0] == '=unmute':
        if "Direct Message" in str(message.channel):
            pass
        else:
            if not message.author.server_permissions.manage_roles:
                return await client.send_message(message.channel, "** Você precisa da permissão de** `gerenciar cargos`**!**")
            try:
                user = message.mentions[0]
                await client.send_message(message.channel, "**O usuario <@{}> foi desmutado com sucesso do servidor.**".format(user.id))
                role = discord.utils.find(lambda r: r.name == "Muted", message.server.roles)
                await client.remove_roles(user, role)
            finally:
                pass

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#  ____            ____                                 _
# |___ \          / ___|    ___    __ _   _ __    ___  | |__
#   __) |  _____  \___ \   / _ \  / _` | | '__|  / __| | '_ \
#  / __/  |_____|  ___) | |  __/ | (_| | | |    | (__  | | | |
# |_____|         |____/   \___|  \__,_| |_|     \___| |_| |_|

    if message.content.lower().split()[0] == "=google":
        if "Direct Message" in str(message.channel):
            pass
        else:
            #  await client.delete_message(message)
            words = 'https://www.google.com/search?q=' + message.content[8:].strip().replace(' ', '+')
            await client.send_message(message.channel, words)

    if message.content.lower().split()[0] == "=youtube":
        if "Direct Message" in str(message.channel):
            pass
        else:
            #  await client.delete_message(message)
            words = 'https://www.youtube.com/results?search_query=' + message.content[9:].strip().replace(' ', '+')
            await client.send_message(message.channel, words)

    if message.content.lower().split()[0] == "=wiki":
        if "Direct Message" in str(message.channel):
            pass
        else:
            messagewiki1 = message.channel
            messagewiki2 = message.channel
            await client.send_message(messagewiki1, "{}, pesquisando na wikipedia, aguarde...".format("<@"+str(message.author.id)+">"))
            try:
                argumentos = message.content[6:]
                sf = wikipedia.page(argumentos)
                embedwiki = discord.Embed(title="Pesquisa da Wikipedia", description="", color=mcolor)
                try:
                    embedwiki.set_image(url=sf.images[0])
                except:
                    pass
                embedwiki.add_field(name="Título", value=sf.title, inline=False)
                embedwiki.add_field(name="Link", value=sf.url, inline=False)
                embedwiki.add_field(name="Conteúdo", value=sf.content[:1000].strip()+"...", inline=False)
                embedwiki.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedwiki)
            except:
                await client.send_message(messagewiki2, "{}, desculpe mais algo deu errado ou está pagina do wikipédia não existe".format("<@"+str(message.author.id)+">"))
#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#  _____           _   _   _     _   _
# |___ /          | | | | | |_  (_) | |  ___
#   |_ \   _____  | | | | | __| | | | | / __|
#  ___) | |_____| | |_| | | |_  | | | | \__ \
# |____/           \___/   \__| |_| |_| |___/

    if message.content.lower().split()[0] == '=py':
        if "Direct Message" in str(message.channel):
            pass
        else:
            usermsgcod = message.content[4:]
            await client.send_message(message.channel,
                                  '<:python:462612832341590016> {} enviou o seguinte código:\n```python\n{} \n```'.format(
                                      message.author.mention, usermsgcod))
            await client.delete_message(message)

    if message.content.lower().split()[0] == '=js':
        if "Direct Message" in str(message.channel):
            pass
        else:
            usermsgcod = message.content[4:]
            await client.send_message(message.channel,
                                  '<:js:462612805699371011> {} enviou o seguinte código:\n```javascript\n{} \n```'.format(
                                      message.author.mention, usermsgcod))

            await client.delete_message(message)

    if message.content.lower().split()[0] == '=votar':
        if "Direct Message" in str(message.channel):
            pass
        else:
            await client.delete_message(message)
            try:
                msg = message.content[7:]
                embedvote = discord.Embed(
                    title="**VOTAÇÃO**"
                    , color=mcolor, description=None
                )
                embedvote.set_thumbnail(url=message.author.avatar_url)
                embedvote.add_field(name='`📝 Votação iniciada por:`', value=message.author.mention, inline=False)
                embedvote.add_field(name='`🖋 Titulo:`', value="{}".format(msg), inline=False)
                await client.send_typing(message.channel)
                gg = await client.send_message(message.channel, embed=embedvote)
                await client.add_reaction(gg, '✔')
                await client.add_reaction(gg, '❌')
            except discord.errors.HTTPException:
                await client.send_message(message.channel, "Insira um texto para iniciar a votação")

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#  _  _             ___            __
# | || |           |_ _|  _ __    / _|   ___
# | || |_   _____   | |  | '_ \  | |_   / _ \
# |__   _| |_____|  | |  | | | | |  _| | (_) |
#    |_|           |___| |_| |_| |_|    \___/

    if message.content.lower().split()[0] == '=botinfo':
        if "Direct Message" in str(message.channel):
            pass
        else:
            #  await client.delete_message(message)

            embedbot = discord.Embed(
                title='**<:botlogo:462620708493852698> Info do Bot**',
                color=mcolor,
                description='\n'
            )
            embedbot.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
            embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
            embedbot.add_field(name='`◼ | Id bot`', value=client.user.id, inline=True)
            embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
            embedbot.add_field(name='📛 | Tag', value=client.user)
            embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))
            embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))
            embedbot.add_field(name='‍⚙️ | Programador', value="`DEIVIZIN希望#7751`")
            embedbot.add_field(name='<:python:462612832341590016> | Version', value="`3.6.5`")
            embedbot.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)

            await client.send_message(message.channel, embed=embedbot)

    if message.content.lower().split()[0] == '=serverinfo':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            try:
                member_list = list(message.server.members)
                status_list = [member.status.value for member in member_list]
                membersinfo = (f"<:online:462622794786799619> {status_list.count('online')}"
                               f"<:idle:462622759093141505> {status_list.count('idle')}"
                               f"<:dnd:462622780857384970> {status_list.count('dnd')}"
                               f"<:offline:462622770161909770>️{status_list.count('offline')}")
                server = message.server
                text_channels = len([x for x in message.server.channels if x.type == discord.ChannelType.text])
                voice_channels = len([x for x in message.server.channels if x.type == discord.ChannelType.voice])
                passed = (message.timestamp - server.created_at).days
                created_at = ("{}  | Há {} dias!""".format(server.created_at.strftime("%d %b %Y %H:%M"), passed))
                embedbot = discord.Embed(title='`Server Info`', color=mcolor, description=None)
                embedbot.set_thumbnail(url=message.server.icon_url)
                embedbot.add_field(name='`☣ | Nome`', value=message.server.name, inline=True)
                embedbot.add_field(name='`👑 | Dono`', value=message.server.owner.mention)
                embedbot.add_field(name='`🕳️ | Id`', value=message.server.id)
                embedbot.add_field(name='`📅 | Criado em`', value=created_at, inline=False)
                embedbot.add_field(name='`👥 | Cargos`', value=len(message.server.roles), inline=True)
                embedbot.add_field(name='`🌐 | Região`', value=message.server.region, inline=True)
                embedbot.add_field(name='`👾 | Canais`', value=(len(list(channel for channel in message.server.channels if
                                                                     channel.type == discord.ChannelType.text or channel.type == discord.ChannelType.voice))),
                                inline=True)
                embedbot.add_field(name='`🧐 | Emojis`', value=(len(message.server.emojis)), inline=True)
                embedbot.add_field(name="`💬 | Canais de Texto`", value=text_channels)
                embedbot.add_field(name="`🗣️ | Canais de Voz`", value=voice_channels)
                embedbot.add_field(name='`🔇 | Canal de afk`', value=message.server.afk_channel, inline=True)
                embedbot.add_field(name='🔐 | Segurança', value=message.server.verification_level, inline=True)
                embedbot.add_field(name='`👨‍👦‍👦 | Membros`', value=len(message.server.members), inline=True)
                embedbot.add_field(name='`ﾠ👨‍👦‍👦 | Membros Status`', value=membersinfo, inline=True)
                embedbot.add_field(name='<:botlogo:462620708493852698> | Bots',
                                value=str(len(list(member for member in message.server.members if member.bot))))
                embedbot.add_field(name='📷 | Icon server', value='[Link direto](' + message.server.icon_url + ')\n',
                               inline=True)
                embedbot.set_footer(
                    text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedbot)
            except discord.errors.HTTPException as e:
                await client.send_message(message.channel, "⚠️Erro : {}".format(e))

    if message.content.lower().split()[0] == '=userinfo':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            try:
                user = message.author
                membro = message.mentions[0]
                embedinfo = discord.Embed(
                    title=' informações', color=mcolor,
                    description='\n ')
                embedinfo.set_thumbnail(url=membro.avatar_url)
                embedinfo.add_field(name='`☣ | Usuário`', value=membro.name)
                embedinfo.add_field(name='`🤬  | Apelido`', value=membro.nick)
                embedinfo.add_field(name='`🕳️ | Id`', value=membro.id)
                embedinfo.add_field(name='`📅 | Desde de`', value=membro.created_at.strftime("%d %b %Y %H:%M"))
                embedinfo.add_field(name='`🗓️ | Entrou em`', value=membro.joined_at.strftime("%d %b %Y %H:%M"))
                embedinfo.add_field(name='`🎮 | Jogando`', value=membro.game)
                embedinfo.add_field(name='`💎 | Cargos`', value=len(([role.name for role in membro.roles if role.name != "@everyone"])))
                embedinfo.set_footer(
                    text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedinfo)
            except:
                user = message.author
                embedinfo = discord.Embed(
                    title=' informações', color=mcolor,
                    description='\n ')
                embedinfo.set_thumbnail(url=user.avatar_url)
                embedinfo.add_field(name='`☣ | Usuário`', value=user.name)
                embedinfo.add_field(name='`🤬  | Apelido`', value=user.nick)
                embedinfo.add_field(name='`🕳️ | Id`', value=user.id)
                embedinfo.add_field(name='`📅 | Desde de`', value=user.created_at.strftime("%d %b %Y %H:%M"))
                embedinfo.add_field(name='`🗓️ | Entrou em`', value=user.joined_at.strftime("%d %b %Y %H:%M"))
                embedinfo.add_field(name='`🎮 | Jogando`', value=user.game)
                embedinfo.add_field(name='`💎 | Cargos`', value=len(([role.name for role in user.roles if role.name != "@everyone"])))
                embedinfo.set_footer(
                    text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedinfo)

    if message.content.lower().split()[0] == '=uptime':
        if "Direct Message" in str(message.channel):
            pass
        else:
            #  await client.delete_message(message)
            uptimeemb = discord.Embed(color=mcolor, description=message.author.mention+", estou online a : `{0}` Horas e `{1}` Minutos.".format(hour, minutes))
            await client.send_message(message.channel, embed=uptimeemb)

    if message.content.lower().split()[0] == '=bitcoin':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            await client.send_typing(message.channel)
            imgbtc = ('http://pngimg.com/uploads/bitcoin/bitcoin_PNG47.png')
            try:
                requeget = requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=BTC&alt=json')
                btc = json.loads(requeget.text)
                nomebtc = (str(btc['valores']['BTC']['nome']))
                precobtc = (str(btc['valores']['BTC']['valor']))
                fontebtc = (str(btc['valores']['BTC']['fonte']))

                embedbtc = discord.Embed(color=mcolor, )
                embedbtc.set_author(name='Bitcoin!'.format(message.author.name))
                embedbtc.add_field(name='Nome:', value="{}".format(nomebtc))
                embedbtc.add_field(name='Valor:', value="{}".format(precobtc))
                embedbtc.add_field(name='fonte:', value="{}".format(fontebtc))
                embedbtc.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                embedbtc.set_thumbnail(url=imgbtc)
                await client.send_message(message.channel, embed=embedbtc)
            except:
                await client.send_message(message.channel, 'ERROR!')

    if message.content.lower().split()[0] == "=cargos":
        if "Direct Message" in str(message.channel):
            pass
        else:
            cargos = [role.name for role in message.server.roles if role.name != "@everyone"]
            role = discord.Embed(title='Cargos do servidor {}'.format(message.server.name),
                             description='Total [{}] Cargos'.format(len(message.server.roles)), color=mcolor)
            role.set_thumbnail(url=message.server.icon_url)
            role.add_field(name="`Lista`", value='{}'.format(cargos).replace("'", " ").replace("[", " ").replace("]", " "))
            role.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=role)

    if message.content.lower().split()[0] == "=avatar":
        if "Direct Message" in str(message.channel):
            pass
        else:
            try:
                # argumentos_f = message.content[:9]
                # argumentos = argumentos_f.split()[1]
                # escolhido = discord.utils.get(client.get_all_members(), id=str(escolhido_random))
                try:
                    escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.mentions[0].id))
                    avatarembed = discord.Embed(title="", color=mcolor,
                                                description="**[Clique aqui](" + escolhido_a.avatar_url + ") para fazer download!**")
                    avatarembed.set_author(name=message.author.name)
                    avatarembed.set_image(url=escolhido_a.avatar_url)
                    avatarembed.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
                    await client.send_message(message.channel, embed=avatarembed)
                except:
                    escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.content[9:]))
                    avatarembed = discord.Embed(title="", color=mcolor,
                                                description="**[Clique aqui](" + message.author.avatar_url + ") para fazer download!**")
                    avatarembed.set_author(name=message.author.name)
                    avatarembed.set_image(url=escolhido_a.avatar_url)
                    avatarembed.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
                    await client.send_message(message.channel, embed=avatarembed)

            except:
                avatarembed = discord.Embed(title="", color=mcolor,
                                            description="**[Clique aqui](" + message.author.avatar_url + ") para fazer download!**")
                avatarembed.set_author(name=message.author.name)
                avatarembed.set_image(url=message.author.avatar_url)
                avatarembed.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=avatarembed)

    if message.content.lower().split()[0] == '=ping':
        if "Direct Message" in str(message.channel):
            pass
        else:
            channel = message.channel
            t1 = time.perf_counter()
            await client.send_typing(channel)
            t2 = time.perf_counter()
            now = datetime.datetime.now()
            p = now - message.timestamp
            ping_embed = discord.Embed(
                                          title=message.author.name,
                                          color=mcolor,
                                          description=":bar_chart: meu ping: `{} ms!`\n"
                                                      ":bar_chart: seu ping: `{} ms!`".format(p.microseconds // 10000, round((t2 - t1) * 1000)))
            ping_embed.set_thumbnail(url=client.avatar_url)
            ping_embed.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=ping_embed)

    if message.content.lower().split()[0] == "=teste":
        if "Direct Message" in str(message.channel):
            pass
        else:
            await client.send_message(message.channel, "Testando:1... 2... 3... Estou online {}!".format(str("<@"+message.author.id+">")))

    if message.content.lower().split()[0] == "=emojis":
        if "Direct Message" in str(message.channel):
            pass
        else:
            server = message.server
            emojis = [str(x) for x in server.emojis]
            lista = " ".join(emojis)
            embedemoji = discord.Embed(colour=mcolor)
            embedemoji.add_field(name="Emojis [" + str(len(emojis)) + "]", value=lista[:993])
            embedemoji.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedemoji)

    if message.content.lower().split()[0] == '=canal':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            await client.send_typing(message.channel)
            channel = message.channel
            channel = channel or message.channel
            embed = discord.Embed(color=0x83f68a,
                              description=channel.mention)
            embed.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
            embed.add_field(name="Nome", value=message.channel.name, inline=True)
            embed.add_field(name="Server", value=message.channel.server.name, inline=True)
            embed.add_field(name="ID", value=channel.id)
            embed.add_field(name="Posição", value=channel.position + 1)
            embed.add_field(name="Tipo", value=channel.type)
            embed.add_field(name="Criado em", value=message.channel.created_at.strftime("%d %b %Y %H:%M"))
            embed.set_footer(
                text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)
#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#  ____            _____
# | ___|          |  ___|  _   _   _ __
# |___ \   _____  | |_    | | | | | '_ \
#  ___) | |_____| |  _|   | |_| | | | | |
# |____/          |_|      \__,_| |_| |_|

    if message.content.lower().split()[0] == '=virus':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            user = message.mentions[0]
            v = await client.send_message(message.channel, "initializing...")
            await asyncio.sleep(3.0)
            await client.edit_message(v, "[▓                         ] / -virus.bat Packing files.")
            await asyncio.sleep(0.5)
            await client.edit_message(v, "[▓▓                    ] - -virus.bat Packing files..")
            await asyncio.sleep(0.7)
            await client.edit_message(v, "[▓▓▓            ] | -virus.bat Packing files..")
            await asyncio.sleep(1.0)
            await client.edit_message(v, "[▓▓▓▓        ] / -virus.bat Packing files..")
            await asyncio.sleep(0.5)
            await client.edit_message(v, "[▓▓▓▓▓    ] - -virus.bat Packing files..")
            await asyncio.sleep(0.8)
            await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
            await asyncio.sleep(4.0)
            await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
            await asyncio.sleep(0.8)
            await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
            await asyncio.sleep(0.5)
            await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
            await asyncio.sleep(1.2)
            await client.edit_message(v, "[▓▓▓▓▓▓] / -virus.bat Packing files..")
            await asyncio.sleep(1.0)
            await client.edit_message(v, "[▓▓▓▓▓▓] - -virus.bat Packing files..")
            await asyncio.sleep(0.8)
            await client.edit_message(v, "[▓▓▓▓▓▓] \ -virus.bat Packing files..")
            await asyncio.sleep(0.8)
            await client.edit_message(v, "Successfully downloaded virus...")
            await asyncio.sleep(0.5)
            await client.edit_message(v, "Installing 'Keylogger'...")
            await asyncio.sleep(2.0)
            ss = await client.edit_message(v, "Successfully injected Keylogger into **{}**!".format(user.name))
            await asyncio.sleep(1.0)
            await client.delete_message(ss)

    if message.content.split == '=moeda':
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            choice = random.randint(1, 2)
            if choice == 1:
                await client.add_reaction(message, '👑')
            if choice == 2:
                await client.add_reaction(message, '😃')

    if message.content.split()[0] == "=dado":
        if "Direct Message" in str(message.channel):
            pass
        else:
            # await client.delete_message(message)
            choice = random.randint(1, 6)
            embeddad = discord.Embed(title='🎲 Dado', description=' Joguei o dado, o resultado foi :   {}'.format(choice),
                                 colour=mcolor)
            embeddad.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embeddad)

    try:
        if message.content.lower().split()[0] == '=say':
            if "Direct Message" in str(message.channel):
                pass
            else:
                sayemb = discord.Embed(
                                      title=message.author.name,
                                      color=mcolor,
                                      description="{}".format(message.content[5:])
                                      )
                sayemb.set_thumbnail(url=message.author.avatar_url)
                await client.send_message(message.channel, embed=sayemb)
                await client.delete_message(message)
    finally:
        pass

    if message.content.lower().split()[0] == '=ppt':
        if "Direct Message" in str(message.channel):
            pass
        else:
            pptemb = discord.Embed(
                                     title=message.author.name,
                                     description="O que você escolhe?\n"
                                                 "`pedra` :full_moon: , `papel` :page_with_curl: ou `tesoura` :scissors: ?",
                                     color=mcolor
                                     )
            await client.send_message(message.channel, embed=pptemb)
            parametros = ['pedra', 'papel', 'tesoura']
            wait = await client.wait_for_message(author=message.author)
            if wait.content == 'pedra':
                pedra = randint(1, 3)
                pedraemb1 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu pedra :full_moon: e eu escolhi tesoura ✂️\n"
                                                     ":tada: Você venceu! Parabéns :clap: ".format(message.author.mention)
                                         )
                pedraemb2 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu pedra :full_moon: e eu escolhi papel :page_with_curl:\n"
                                                               ":tada: Eu ganhei! :stuck_out_tongue_winking_eye: ".format(message.author.mention)
                                         )
                pedraemb3 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu pedra :full_moon: e eu escolhi pedra :full_moon:\n"
                                                     ":tada: Empate!".format(message.author.mention)
                                          )
                if pedra == 1:
                    await client.send_message(message.channel, embed=pedraemb1)
                if pedra == 2:
                    await client.send_message(message.channel, embed=pedraemb2)
                if pedra == 3:
                    await client.send_message(message.channel, embed=pedraemb3)

            if wait.content == 'tesoura':
                tesoura = randint(1, 3)
                tesouraemb1 = discord.Embed(
                                           color=mcolor,
                                           description="{}, você escolheu tesoura ✂️ e eu escolhi papel :page_with_curl:\n"
                                                      ":tada: Você venceu! Parabéns :clap: ".format(message.author.mention)
                                           )
                tesouraemb2 = discord.Embed(
                                           color=mcolor,
                                           description="{}, você escolheu tesoura ✂️ e eu escolhi pedra :full_moon:\n"
                                                       ":tada: Eu ganhei! :stuck_out_tongue_winking_eye: ".format(message.author.mention)
                                           )
                tesouraemb3 = discord.Embed(
                                           color=mcolor,
                                           description="{}, você escolheu tesoura ✂️ e eu escolhi tesoura ✂️\n"
                                                       ":tada: Empate!".format(message.author.mention)
                                           )
                if tesoura == 1:
                    await client.send_message(message.channel, embed=tesouraemb1)
                if tesoura == 2:
                    await client.send_message(message.channel, embed=tesouraemb2)
                if tesoura == 3:
                    await client.send_message(message.channel, embed=tesouraemb3)
            if wait.content == 'papel':
                papel = randint(1, 3)
                papelemb1 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu papel :page_with_curl: e eu escolhi pedra :full_moon:\n"
                                                     ":tada: Você venceu! Parabéns :clap: ".format(message.author.mention)
                                         )
                papelemb2 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu papel :page_with_curl: e eu escolhi tesoura ✂️\n"
                                                     ":tada: Eu ganhei! :stuck_out_tongue_winking_eye: ".format(message.author.mention)
                                         )
                papelemb3 = discord.Embed(
                                         color=mcolor,
                                         description="{}, você escolheu papel :page_with_curl: e eu escolhi papel :page_with_curl:\n"
                                                     ":tada: Empate!".format(message.author.mention)
                                         )
                if papel == 1:
                    await client.send_message(message.channel, embed=papelemb1)
                if papel == 2:
                    await client.send_message(message.channel, embed=papelemb2)
                if papel == 3:
                    await client.send_message(message.channel, embed=papelemb3)

            pptemberro = discord.Embed(
                                      color=mcolor,
                                      description="{}, você escolheu merda :poop: e eu um humano :spy:\n"
                                                  ":tada: Eu ganhei! Esmaguei você :stuck_out_tongue_winking_eye:!".format(message.author.mention)
                                      )
            if not wait.content in parametros:
                await client.send_message(message.channel, embed=pptemberro)

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#   ____           _               _
#  / ___|         | |__     ___   | |_
# | |___   _____  | '_ \   / _ \  | __|
# |     \ |_____| | |_) | | (_) | | |_
#  \____/         |_.__/   \___/   \__|

    if message.content.lower() == "<@461322896065953808>" or "Direct Message" in str(message.channel):
        if "Direct Message" in str(message.channel):
            if "<@461322896065953808>" in message.content:
                pass
        else:
            embedmention = discord.Embed(title="Não sabe meu prefixo?",
                                         description="Meu prefixo padrão é `=`\n"
                                                     "No momento eu não tenho um sistema de prefixo personalizado",
                                         color=mcolor
                                         )
            embedmention.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedmention)
            await client.delete_message(message)

    if message.content.lower().split()[0] == '=ajuda':
        if "Direct Message" in str(message.channel):
            pass
        else:
            ajudaemb = discord.Embed(title="Precisa de ajuda?",
                                     description="Olá eu sou a <@461322896065953808>, bem isso você ja deve saber.\n"
                                                 "Eu sou um bot com script feito em python no momento.\n"
                                                 "Espero dar um bom entretenimento a você!\n"
                                                 "Infelizmente meu servidor não esta pronto, meu criador esta trabalhando nele.\n"
                                                 "Se quiser me adicional apenas digitar `=invite` não no meu privado.\n"
                                                 "Se quiser saber meus comandos digite `=comandos`.\n"
                                                 "Bem, espero que seja apenas isto que deveria te dizer!\n"
                                                 "Obrigada por estar me utilizando :3",
                                     color=mcolor
                                     )
            ajudaemb.set_image(url="https://78.media.tumblr.com/1359a5e9c870ba66941f685d3ea2a500/tumblr_ohywm3htfb1tlcfymo1_500.gif")
            ajudaemb.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
            await client.send_message(message.channel, "{}, enviei no seu privado :envelope_with_arrow:".format(str("<@"+message.author.id+">")))
            await client.send_message(message.author, embed=ajudaemb)

    if message.content.lower().split()[0] == '=invite':
        if "Direct Message" in str(message.channel):
            pass
        else:
            inviteemb = discord.Embed(title="Meu invite(clique aqui)", url="https://discordapp.com/api/oauth2/authorize?client_id=461322896065953808&permissions=8&scope=bot",
                                      color=mcolor,
                                      description="Obrigada "+message.author.mention+", por me escolher.\n"
                                                  "Se você quer me escolher, isso que dizer que você gostou de mim?\n"
                                                  "bem de qualquer maneira, meu criador esta muito grato a você por me escolher :D"
                                     )
            inviteemb.set_image(url="http://78.media.tumblr.com/0feb00aab45cd4041bcde81f94a4e629/tumblr_njrd41DNxK1rf0dpio1_500.gif")
            inviteemb.set_author(name="Quer me adicionar?")
            inviteemb.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
            await client.send_message(message.channel, "{}, enviei no seu privado :envelope_with_arrow:".format(str("<@"+message.author.id+">")))
            await client.send_message(message.author, embed=inviteemb)

    if message.content.lower().split()[0] == '=comandos':
        if "Direct Message" in str(message.channel):
            pass
        else:
            ct = discord.Embed(
                          title="reaja para trocar de embed!",
                          color=mcolor,
                          description="👮 - Moderação\n"
                                      "🔎 - Search\n"
                                      "🗂 - Uteis\n"
                                      "📖 - Informações\n"
                                      "😜 - Diversão\n"
                                      "🤖 - Bot\n"
                                      "🎵 - Música\n"
                                      "⬅ - para retomar o embed"
                          )
            ct.set_author(name="Meus comandos!")
            ct.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
            ct.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)

            botmsghelp = await client.send_message(message.channel, embed=ct)

            await client.add_reaction(botmsghelp, "👮")
            await client.add_reaction(botmsghelp, "🔎")
            await client.add_reaction(botmsghelp, "🗂")
            await client.add_reaction(botmsghelp, "📖")
            await client.add_reaction(botmsghelp, "😜")
            await client.add_reaction(botmsghelp, "🤖")
            await client.add_reaction(botmsghelp, "🎵")
            await client.add_reaction(botmsghelp, "⬅")

            msg_id = botmsghelp.id
            msg_user = message.author

        @client.event
        async def on_reaction_add(reaction, user):
            msg = reaction.message

            if reaction.emoji == "👮" and msg.id == msg_id and user == msg_user:
                comandemdmoderação = discord.Embed(
                                     title="Comandos de moderações!",
                                     description="`=getban` - remove todos os banimentos do servidor;\n"
                                                 "`=ban` - banir um usúario com motivo;\n"
                                                 "`=unban` - para retirar o ban de um usúario\n"
                                                 "`=clear` - para apagar até 100 mensagens\n"
                                                 "`=mute` - para mutar um usúario(cargo *Muted* necessário)\n"
                                                 "`=unmute` - para retirar o ban de um usúario",
                                     color=mcolor
                                     )
                comandemdmoderação.set_author(name="Meus comandos!",)
                comandemdmoderação.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandemdmoderação.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandemdmoderação)

            if reaction.emoji == "🔎" and msg.id == msg_id and user == msg_user:
                comandembsearch = discord.Embed(
                                     title="Comandos de search!",
                                     description="`=google` - fazer uma pesquisa no google\n"
                                                 "`=ban` - fazer uma pesquisa no youtube\n"
                                                 "`=wiki` - fazer uma pesquisa no wikipédia",
                                     color=mcolor
                                     )
                comandembsearch.set_author(name="Meus comandos!")
                comandembsearch.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembsearch.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembsearch)

            if reaction.emoji == "🗂" and msg.id == msg_id and user == msg_user:
                comandembuteis = discord.Embed(
                                              title="Comandos uteis",
                                              description="`=py` - enviar uma mensagem no formato python\n"
                                                          "`=js` - enviar uma mensagem no formato javascript\n"
                                                          "`=votar` - fazer uma votação",
                                              color=mcolor
                                              )
                comandembuteis.set_author(name="Meus comandos!")
                comandembuteis.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembuteis.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembuteis)

            if reaction.emoji == "📖" and msg.id == msg_id and user == msg_user:
                comandembinfo = discord.Embed(
                                            title="Comandos de informação",
                                            description="`=botinfo` - ver as informações do bot\n"
                                                        "`=serverinfo` - ver as informações do servidor\n"
                                                        "`=userinfo` - mostra asa informações do usúarios\n"
                                                        "`=uptime` - ver o tempo em que estou online\n"
                                                        "`=bitcoin` - ver o preço do bitcoin\n"
                                                        "`=cargos` - ver os cargos do servidor\n"
                                                        "`=avatar` - ver o avatar do usúario\n"
                                                        "`=ping` - ver o meu e o seu ping\n"
                                                        "`=teste` - ver se estou online\n"
                                                        "`=emojis` - ver os emojis do servidor(menos os animados)\n"
                                                        "`=canal` - vai mostrar as informações de um canal selecionado",
                                            color=mcolor
                                            )
                comandembinfo.set_author(name="Meus comandos!")
                comandembinfo.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembinfo.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembinfo)

            if reaction.emoji == "😜" and msg.id == msg_id and user == msg_user:
                comandembfun = discord.Embed(
                                              title="Comandos de diversão!",
                                              description="`=virus` - vai colocar um virus no usúario mencionado\n"
                                                          "`=moeda` - vai girar um moeda\n"
                                                          "`=dado` - ver em qual dos de um dado vai cair\n"
                                                          "`=say` - repetirar sua mensagem\n"
                                                          "`=ppt` - joquempô(pedra, papel, tesoura)",
                                              color=mcolor
                                              )
                comandembfun.set_author(name="Meus comandos!")
                comandembfun.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembfun.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembfun)

            if reaction.emoji == "🤖" and msg.id == msg_id and user == msg_user:
                comandembbot = discord.Embed(
                                                title="Comandos do bot!",
                                                description="<@461322896065953808> - para ver o prefixo\n"
                                                            "`=ajuda` - para ver o embed de ajuda\n"
                                                            "`=invite` - para pegar o link de invite\n"
                                                            "`=servidor` - para pegar o link do servidor\n"
                                                            "`=comandos` - para ve o embed de ajuda",
                                                color=mcolor
                                                )
                comandembbot.set_author(name="Meus comandos!")
                comandembbot.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembbot.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembbot)

            if reaction.emoji == "🎵" and msg.id == msg_id and user == msg_user:
                comandembmusica = discord.Embed(
                                                title="Comandos de música!",
                                                description="No momento não tenho comandos de músicas",
                                                color=mcolor
                                                )
                comandembmusica.set_author(name="Meus comandos!")
                comandembmusica.set_thumbnail(url="https://cdn.discordapp.com/avatars/461322896065953808/377ea01d8931cfe22dad25fc552dc3ba.webp?size=1024")
                comandembmusica.set_footer(text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
                    icon_url=message.author.avatar_url)
                await client.edit_message(msg, embed=comandembmusica)

            if reaction.emoji == "⬅" and msg.id == msg_id and user == msg_user:
                await client.edit_message(msg, embed=ct)

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

#  _____
# |  ___|  _   _   _ __     ___    ___     ___   ___
# | |_    | | | | | '_ \   / __|  / _ \   / _ \ / __|
# |  _|   | |_| | | | | | | (__  | (_) | |  __/ \__ \
# |_|      \__,_| |_| |_|  \___|  \___/   \___| |___/
#

def a7x():
    r = requests.get('https://nekos.life/api/neko')
    if r.status_code == 200:
        js = r.json()
        return js['neko']


async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1


client.loop.create_task(uptime())

#  _____   _____   _____   _____   _____   _____   _____   _____   _____
# |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|
#

client.run(token_a)
