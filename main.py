def my_func(token, guild, channel, invite):
	import dm
	import discum.gateway.session

	bot = discum.Client(token=token)

	def close_after_fetching(resp, guild_id):
		if bot.gateway.finishedMemberFetching(guild_id):
			bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
			bot.gateway.close()

	def get_members(guild_id, channel_id):
		bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
		bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.run()
		bot.gateway.resetSession()
		return bot.gateway.session.guild(guild_id).members

	members = get_members(guild, channel)
	memberslist = []

	for memberID in members:
		memberslist.append(memberID)

	f = open('users.txt', "w")
	for element in memberslist:
		f.write(element + '\n')

	f.close()

	dm.send_mp(token, invite)

