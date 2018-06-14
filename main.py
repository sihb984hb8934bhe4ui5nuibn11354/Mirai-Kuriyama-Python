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
async def twitch():
	while True:
		#await client.change_presence(game=discord.Game(name='Estou atualmente em {} servidores'.format(str(number)), url='https://www.twitch.tv/deivizin_', type=1))
		time.sleep(10)
		await client.change_presence(game=discord.Game(name='Estou atualmente em {} servidores'.format(str(number)), url='https://www.twitch.tv/deivizin_', type=1))
		
	
@client.event
async def on_ready():
	thread.start_new_thread(twitch, ())
	
	wikipedia.set_lang("pt")
	number = 0
	
	for number_f in client.servers:
		number = number+1
	
	print("")
	print("LIGADA COM SUCESSO!")
	print("")
	
	
@client.event
async def on_message(message):
	if message.content.lower() == "<@454018497995997184>" or "Direct Message" in str(message.channel):
		if "Direct Message" in str(message.channel):
			if "<@454018497995997184>" in message.content:
				pass
		else:
			await client.send_message(message.channel, "{} -- Meu prefixo atual desse servidor é `k>`".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().split()[0] == "k>secret":
		if "Direct Message" in str(message.channel):
			 pass
		else:
			await client.send_message(message.channel, "{} -- ErRoR 4o4".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().split()[0] == "k>wiki":
		if "Direct Message" in str(message.channel):
			pass
		else:
			await client.send_message(message.channel, "{} -- Pesquisando na wikipedia, aguarde...".format("<@"+str(message.author.id)+">"))
			try:
				argumentos = message.content[7:]
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
	
	if message.content.lower().split()[0] == 'k>ajuda':
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
			ajudaembedf.add_field(name="k>avatar `(usuario)`", value="Use para capturar uma imagem de certo perfil", inline=False)
			ajudaembedff.add_field(name="k>invite", value="Para poder me adicionar em seu servidor", inline=False)
			#ajudaembedff.add_field(name="k>botinfo", value="Para conhecer um pouco mais de mim", inline=False)
			ajudaembedff.add_field(name="k>ping", value="Usado para mostrar meu ping atual", inline=False)
			ajudaembedfff.add_field(name="k>wiki `(enciclopédia)`", value="Faz uma pesquisa na wikipedia", inline=False)
			ajudaembedfff.add_field(name="k>fofoca", value="Fala de umas fofoquinhas que estão acontecendo `(Indisponível)`", inline=False)

				#ajudaembed.set_image(url="https://cdn.discordapp.com/attachments/454350443276140586/455106888506540032/Image__198761_1517969068.jpeg")
			ajudaembedfff.set_footer(text="ATT: DEIVIZIN e CentenoBR")
			await client.send_message(message.author, embed=ajudaembedf)	
			await client.send_message(message.author, embed=ajudaembedff)
			await client.send_message(message.author, embed=ajudaembedfff)
		
	if message.content.lower().split()[0] == "k>avatar":
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
					escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.content[9:]))
					avatarembed = discord.Embed(title="",color=0x0000ff,description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!**")
					avatarembed.set_author(name=message.author.name)
					avatarembed.set_image(url=escolhido_a.avatar_url)
					await client.send_message(message.channel, embed=avatarembed)
				
			except:
				avatarembed = discord.Embed(title="",color=0x0000ff,description="**[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!**")
				avatarembed.set_author(name=message.author.name)
				avatarembed.set_image(url=message.author.avatar_url)
				await client.send_message(message.channel, embed=avatarembed)
			
	if message.content.lower().split()[0] == "k>invite":
		if "Direct Message" in str(message.channel):
			pass	
		else:
			await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=454018497995997184&permissions=8&scope=bot {}".format(str("<@"+message.author.id+">")))
			
	if message.content.lower().split()[0] == 'k>ping':
		if "Direct Message" in str(message.channel):
			pass
		else:
			now = datetime.datetime.now()
			p = now - message.timestamp
			ping_embed = discord.Embed(title=message.author.name, color=0xcd0000, description=' :bar_chart: = **{} ms!**'.format(p.microseconds // 10000))
			await client.send_message(message.channel, embed=ping_embed)
		

		
		
		
client.run(token_a)














