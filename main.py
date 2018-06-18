import discord
import asyncio
import wikipedia
import random
import datetime
import os
import _thread as thread
import time

token_a = str(os.environ.get('TOKEN', None))

kcolor = 0x7219ff

#if message.content.lower().startswith("k!fofoca"):
	#fofocas = ["{} -- Coitado(a) do(a) **__{}__** foi flagrado(a) na escola! :scream: ","{} -- Eu ouvir dizer que o(a) **__{}__** faltou a aula para fazer coisas com o(a) prim... :rolling_eyes:","{} -- Os relacionamentos estão indo bem para o(a) **__{}__** ( ͡° ͜ʖ ͡°) :laughing:","{} -- **__{}__** Fez um mijão numa festa e não tinha roupa reserva :confused:","{} -- **__{}__** Olhou-se no espelho e saiu correndo :laughing:"]
	#lom = []
	#for members_f in message.server.members:
		#if members_f.id == message.author.id or str(members_f.id) == "454018497995997184":
			#pass
		#else:
			#lom.append(str(members_f.id))
	#escolhido_random = random.choice(lom)
	#escolhido = discord.utils.get(client.get_all_members(), id=str(escolhido_random))
	#fofoca_random = random.choice(fofocas)
	#await client.send_message(message.channel, fofoca_random.format("<@"+str(message.author.id)+">",escolhido.name))
	#a

client = discord.Client()
	
@client.event
async def on_ready():
	wikipedia.set_lang("pt")
	print("")
	print("LIGADA COM SUCESSO!")
	print("")
	

	while True:
		await client.change_presence(game=discord.Game(name='utilize ,ajuda', url='https://www.twitch.tv/deivizin_', type=1))
		await asyncio.sleep(15)
		script = "para "+str(len(client.servers))+" servidores | "+str(len(set(client.get_all_members())))+" usuários."
		await client.change_presence(game=discord.Game(name=script, type=1, url='https://www.twitch.tv/deivizin_'),status='streaming')
		await asyncio.sleep(15)
		script2 = "estou em desenvolvimento! ;u;"
		await client.change_presence(game=discord.Game(name=script2, type=1, url='https://www.twitch.tv/deivizin_'),status='streaming')
		await asyncio.sleep(15)
		script3 = "tem alguma dica? entre em meu servidor: ,servidor"
		await client.change_presence(game=discord.Game(name=script3, type=1, url='https://www.twitch.tv/deivizin_'),status='streaming')
		await asyncio.sleep(15)
		script4 = "prefixo padrão é ,"
		await client.change_presence(game=discord.Game(name=script4, type=1, url='https://www.twitch.tv/deivizin_'),status='streaming')
		await asyncio.sleep(15)

	
@client.event
async def on_message(message):
	if message.content.lower() == "<@454018497995997184>" or "Direct Message" in str(message.channel):
		if "Direct Message" in str(message.channel):
			if "<@454018497995997184>" in message.content:
				pass
		else:
			await client.send_message(message.channel, "{} -- Meu prefixo é `,`".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().split()[0] == ",secret":
		if "Direct Message" in str(message.channel):
			 pass
		else:
			await client.send_message(message.channel, "{} -- ErRoR 4o4".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().split()[0] == ",wiki":
		if "Direct Message" in str(message.channel):
			pass
		else:
			await client.send_message(message.channel, "{} -- Pesquisando na wikipedia, aguarde...".format("<@"+str(message.author.id)+">"))
			try:
				argumentos = message.content[6:]
				sf = wikipedia.page(argumentos)
				embed = discord.Embed(title="Pesquisa da Wikipedia",description="",color=0xf6d612)
				try:
					embed.set_image(url=sf.images[0])
				except:
					pass
				embed.add_field(name="Título", value=sf.title, inline=False)
				embed.add_field(name="Link", value=sf.url, inline=False)
				embed.add_field(name="Conteúdo", value=sf.content[:1000].strip()+"...", inline=False)
				await client.send_message(message.channel, embed=embed)
			except:
				await client.send_message(message.channel, "{} -- Desculpe mais algo deu errado ou está pagina do wikipédia não existe :tired_face:".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().split()[0] == ',ajuda':
		if "Direct Message" in str(message.channel):
			pass
		else:
			await client.send_message(message.channel, "{} -- Enviei meus comandos no seu **privado** :inbox_tray:".format("<@" + str(message.author.id) + ">"))
			ajudaembedf=discord.Embed(color=kcolor,icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedff=discord.Embed(color=kcolor,icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedfff=discord.Embed(color=kcolor,icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedf.set_author(name="Comandos sobre o discord", icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedff.set_author(name="Comandos sobre mim", icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedfff.set_author(name="Comandos diversos", icon_url="https://i.imgur.com/rdm3W9t.png")
			ajudaembedf.add_field(name=",avatar `(usuario)`", value="Use para capturar uma imagem de certo perfil", inline=False)
			ajudaembedff.add_field(name=",minvite", value="Para poder me adicionar em seu servidor", inline=False)
			#ajudaembedff.add_field(name="!mbotinfo", value="Para conhecer um pouco mais de mim", inline=False)
			ajudaembedff.add_field(name=",ping", value="Usado para mostrar meu ping atual", inline=False)
			ajudaembedfff.add_field(name=",wiki `(enciclopédia)`", value="Faz uma pesquisa na wikipedia", inline=False)
			ajudaembedfff.add_field(name=",fofoca", value="Fala de umas fofoquinhas que estão acontecendo `(Indisponível)`", inline=False)
			#ajudaembed.set_image(url="https://cdn.discordapp.com/attachments/454350443276140586/455106888506540032/Image__198761_1517969068.jpeg")
			ajudaembedfff.set_footer(text="ATT: DEIVIZIN e CentenoBR")
			await client.send_message(message.author, embed=ajudaembedf)	
			await client.send_message(message.author, embed=ajudaembedff)
			await client.send_message(message.author, embed=ajudaembedfff)
		
	if message.content.lower().split()[0] == ",avatar":
		if "Direct Message" in str(message.channel):
			pass
		else:
			try:
				#argumentos_f = message.content[:9]
				#argumentos = argumentos_f.split()[1]
				#escolhido = discord.utils.get(client.get_all_members(), id=str(escolhido_random))
				try:
					escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.mentions[0].id))
					avatarembed = discord.Embed(title="",color=0x0000ff,description="**[Clique aqui](" + escolhido_a.avatar_url + ") para acessar o link do avatar!**")
					avatarembed.set_author(name=message.author.name)
					avatarembed.set_image(url=escolhido_a.avatar_url)
					await client.send_message(message.channel, embed=avatarembed)
				except:
					escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.content[8:]))
					avatarembed = discord.Embed(title="",color=0x0000ff,description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!**")
					avatarembed.set_author(name=message.author.name)
					avatarembed.set_image(url=escolhido_a.avatar_url)
					await client.send_message(message.channel, embed=avatarembed)
				
			except:
				avatarembed = discord.Embed(title="",color=0x0000ff,description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!**")
				avatarembed.set_author(name=message.author.name)
				avatarembed.set_image(url=message.author.avatar_url)
				await client.send_message(message.channel, embed=avatarembed)
			
	if message.content.lower().split()[0] == ",invite":
		if "Direct Message" in str(message.channel):
			pass	
		else:
			await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=454018497995997184&permissions=8&scope=bot {}".format(str("<@"+message.author.id+">")))
			
	if message.content.lower().split()[0] == ',ping':
		if "Direct Message" in str(message.channel):
			pass
		else:
			now = datetime.datetime.now()
			p = now - message.timestamp
			ping_embed = discord.Embed(title=message.author.name, color=0xcd0000, description=' :bar_chart: = **{} ms!**'.format(p.microseconds // 10000))
			await client.send_message(message.channel, embed=ping_embed)
		
    	if message.content.lower().split()[0] == ',comandos':
		if "Direct Message" in str(message.channel):
			pass
		else:
        		embedcomandos = discord.Embed(description="**,avatar** `(usuário)` - para fazer download de algum avatar\n"
                                                  "**,invite** - para pegar meu link de invite\n"
                                                  "**,ping** - para ver meu ping(latência)\n"
                                                  "**,wiki** `(enciclopédia)` - para fazer uma pesquisa na Wikipédia\n"
                                                  "**,fofoca** `indisponível`- para saber de algumas coisas que acontecem com os usuários\n"
                                                  "**,devs** `indisponível` - para saber alguma informações sobre meus criadores\n"
                                                  "**,bug** - para saber o que fazer se encontrou algum bug em mim\n"
                                                  "**,servidor** - para poder entrar em meu servidor\n"
                                                  "**,musica** `indisponível` - para ver meus comandos de música\n"
                                                  "**,site** `indisponível` - para entrar no meu site\n"
                                                  "**,social** `indisponível` - para acessar as rede sócias mais rapidamente\n"
                                                  "**,donete** - para ver a formas de me ajudar a comprar um lanche\n"
                                                  "**,trans**(lingua)(mensagem) - para traduzir uma mensagem", color=0x4F0A89)
        		embedcomandos.set_author(name="Meus comandos!")
        		embedcomandos.set_image(url="http://i2.wp.com/haruhichan.com/wpblog/wp-content/uploads/Misaka-Mikoto-%E2%80%93-Toaru-Majutsu-no-Index-tsundere.gif")
        		embedcomandos.set_footer(text="Mikoto", icon_url="https://cdn.discordapp.com/avatars/454018497995997184/0207e69104c285b921b18117bd6bf6ef.webp?size=1024")
        		await client.send_message(message.channel, "{}, enviei no seu privado :inbox_tray:".format(str("<@"+message.author.id+">")))
        		await client.send_message(message.author, embed=embedcomandos)
		
		
		
client.run(token_a)
