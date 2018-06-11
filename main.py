import discord
import asyncio
import wikipedia
import random

kcolor = 0x5e003e

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

client = discord.Client()


@client.event
async def on_ready():
	wikipedia.set_lang("pt")
	number = 0
	
	for number_f in client.servers:
		number = number+1
	
	print("")
	print("LIGADA COM SUCESSO!")
	print("")
	await client.change_presence(game=discord.Game(name='{} servidores | k>ajuda'.format(str(number)), url='https://www.twitch.tv/deivizin_', type=1))
	
@client.event
async def on_message(message):
	if message.content.lower().startswith("<@454018497995997184>") or "Direct Message" in str(message.channel):
		if "Direct Message" in str(message.channel):
			if "<@454018497995997184>" in message.content:
				await client.send_message(message.channel, "{} -- Eu não gosto de ser mencionada no meu privado :rage: ".format(str("<@"+message.author.id+">")))
		else:
			await client.send_message(message.channel, "{} -- Meu prefixo atual desse servidor é `k>`".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().startswith("k>secret"):
		if "Direct Message" in str(message.channel):
			await client.send_message(message.channel, "{} -- Você não pode usar comandos no meu privado :rage: ".format(str("<@"+message.author.id+">")))
		else:
			await client.send_message(message.channel, "{} -- ErRoR 4o4".format("<@"+str(message.author.id)+">"))
	
	if message.content.lower().startswith("k>wiki"):
		if "Direct Message" in str(message.channel):
			await client.send_message(message.channel, "{} -- Você não pode usar comandos no meu privado :rage: ".format(str("<@"+message.author.id+">")))
		else:
			await client.send_message(message.channel, "{} -- Pesquisando na wikipedia, aguarde...".format("<@"+str(message.author.id)+">"))
			try:
				argumentos = message.content[7:]
				sf = wikipedia.page(argumentos)
				embed = discord.Embed(title="Pesquisa da Wikipedia",description="",color=kcolor)
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
	
	if message.content.startswith('k>ajuda'):
		if "Direct Message" in str(message.channel):
			await client.send_message(message.channel, "{} -- Você não pode usar comandos no meu privado :rage: ".format(str("<@"+message.author.id+">")))
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
			ajudaembedfff.add_field(name="k>wiki `(enciclopédia)`", value="Faz uma pesquisa na wikipedia", inline=False)
			ajudaembedfff.add_field(name="k>fofoca", value="Fala de umas fofoquinhas que estão acontecendo `(Indisponível)`", inline=False)

				#ajudaembed.set_image(url="https://cdn.discordapp.com/attachments/454350443276140586/455106888506540032/Image__198761_1517969068.jpeg")
			ajudaembedfff.set_footer(text="ATT: DEIVIZIN e CentenoBR")
			await client.send_message(message.author, embed=ajudaembedf)	
			await client.send_message(message.author, embed=ajudaembedff)
			await client.send_message(message.author, embed=ajudaembedfff)
		
	if message.content.lower().startswith("k>avatar"):
		if "Direct Message" in str(message.channel):
			await client.send_message(message.channel, "{} -- Você não pode usar comandos no meu privado :rage: ".format(str("<@"+message.author.id+">")))
		else:
			try:
				#argumentos_f = message.content[:9]
				#argumentos = argumentos_f.split()[1]
				#escolhido = discord.utils.get(client.get_all_members(), id=str(escolhido_random))
				try:
					escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.mentions[0].id))
					avatarembed = discord.Embed(title="",color=kcolor,description="[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!")
					avatarembed.set_author(name=message.author.name)
					avatarembed.set_image(url=escolhido_a.avatar_url)
					await client.send_message(message.channel, embed=avatarembed)
				except:
					escolhido_a = discord.utils.get(client.get_all_members(), id=str(message.content[9:]))
					avatarembed = discord.Embed(title="",color=kcolor,description="[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!")
					avatarembed.set_author(name=message.author.name)
					avatarembed.set_image(url=escolhido_a.avatar_url)
					await client.send_message(message.channel, embed=avatarembed)
				
			except:
				avatarembed = discord.Embed(title="",color=kcolor,description="[Clique aqui](" + message.author.avatar_url + ") para acessar o link do avatar!")
				avatarembed.set_author(name=message.author.name)
				avatarembed.set_image(url=message.author.avatar_url)
				await client.send_message(message.channel, embed=avatarembed)
			
	if message.content.lower().startswith("k>invite"):
		if "Direct Message" in str(message.channel):
			await client.send_message(message.channel, "{} -- Você não pode usar comandos no meu privado :rage: ".format(str("<@"+message.author.id+">")))	
		else:
			await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=454018497995997184&permissions=8&scope=bot {}".format(str("<@"+message.author.id+">")))
		

		
		
		
client.run("NDU0MDE4NDk3OTk1OTk3MTg0.DfrwpQ.sDbmb8rOQ1mz4ghAk3lsGYCx-1g")














