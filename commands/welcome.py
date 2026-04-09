import discord
from discord.ext import commands
from os import getenv

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(int(getenv("WELCOME_CHANNEL")))
        if not welcome_channel:
            print("Failed to get welcome channel")
            return

        message = "I'm **Boop**, this server's friendly robot. Type `/` to see available commands.\n"
        message += "Please support the project by **leaving us a star on [GitHub](https://github.com/nekename/OpenDeck)** :star:\n"
        message += "If you want to go above and beyond, **please consider [sponsoring](https://github.com/sponsors/nekename) development** :heart:"
        embed = discord.Embed(color = discord.Colour.dark_gray())
        embed.add_field(name = "**Welcome!**", value = message)

        await welcome_channel.send(f"{member.mention}", embed = embed)
