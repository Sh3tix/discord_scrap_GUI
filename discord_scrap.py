import tkinter as tk
from main import my_func

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title("Discord Scraper")
		self.master.resizable(False, False)
		self.widgets()

	def widgets(self):
		# Variables
		self.token = tk.StringVar()
		self.guild_token = tk.StringVar()
		self.channel_token = tk.StringVar()
		self.invite = tk.StringVar()

		# Widgets
		self.options_frame = tk.LabelFrame(self.master, text="options")

		label_channel = tk.Label(self.options_frame, text="CHANNEL ID")
		self.entry_channel = tk.Entry(self.options_frame, textvariable=self.channel_token)

		label_guild = tk.Label(self.options_frame, text="GUILD ID")
		self.entry_guild = tk.Entry(self.options_frame, textvariable=self.guild_token)

		label_token = tk.Label(self.options_frame, text="TOKEN")
		self.entry_token = tk.Entry(self.options_frame, textvariable=self.token)

		label_invite = tk.Label(self.options_frame, text="Lien d'invitation")
		self.entry_invite = tk.Entry(self.options_frame, textvariable=self.invite)

		self.buton = tk.Button(self.options_frame, text="Scrap", command=self.get_all_token)

		self.preset_frame = tk.LabelFrame(self.master, text="IDs")
		self.preset_list = tk.Listbox(self.preset_frame, width=25)

		# Positionnements
		label_guild.grid(row=0, column=0, padx=20)
		self.entry_guild.grid(row=1, column=0, padx=20, pady=10)

		label_channel.grid(row=0, column=1, padx=10)
		self.entry_channel.grid(row=1, column=1, padx=10, pady=10)

		label_token.grid(row=2, column=0)

		self.entry_token.grid(row=3, column=0)

		self.buton.grid(column=0, row=4, columnspan=2, pady=25)

		self.preset_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.S)
		self.preset_list.grid(row=0, column=0, padx=5, columnspan=2)

		label_invite.grid(row=2, column=1)
		self.entry_invite.grid(row=3, column=1, columnspan=2)

		self.options_frame.grid(row=0, column=1, sticky=tk.N + tk.S)

	def get_all_token(self):
		token = self.token.get()
		guild = self.guild_token.get()
		channel = self.channel_token.get()
		invite = self.invite.get()

		if token != "" and guild != "" and channel != "" and invite != "":
			try:
				my_func(token, guild, channel, invite)
			except SystemExit:
				pass

			with open("users.txt", "r") as file:
				lignes = file.readlines()
				for ligne in lignes:
					self.preset_list.insert(0, ligne)


if "__main__" == __name__:
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()
