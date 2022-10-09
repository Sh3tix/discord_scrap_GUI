def send_mp(token, invite_link):
	import discord
	from discord.ext.commands import Bot

	TOKEN = token

	client = discord.Client()
	b = Bot(command_prefix="!")
	m = []

	@b.event
	async def on_ready():
		await mp()

		exit()

	async def mp():
		with open("users.txt") as f:
			for line in f:
				m.append(line.rstrip())

			for id in m:
				user = await b.fetch_user(id)

				try:
					await user.send('JOIN ' + invite_link)
				except:
					continue

	b.run(TOKEN, bot=False)
