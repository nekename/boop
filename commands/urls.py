import discord
from discord.ext.commands import Cog
from discord.app_commands import command

class Urls(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(description = "Gives you the OpenDeck GitHub repository URL")
    async def github(self, ctx):
        embed = discord.Embed(color = discord.Colour.dark_gray(), title = "https://github.com/nekename/OpenDeck")
        embed.set_author(name = "GitHub", icon_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the OpenDeck issues page URL")
    async def issues(self, ctx):
        embed = discord.Embed(color = discord.Colour.red(), title = "https://github.com/nekename/OpenDeck/issues")
        embed.set_author(name = "Issues", icon_url = "https://img.icons8.com/fluency/344/error.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the OpenDeck pull requests page URL")
    async def pulls(self, ctx):
        embed = discord.Embed(color = discord.Colour.blurple(), title = "https://github.com/nekename/OpenDeck/pulls")
        embed.set_author(name = "Pull Requests", icon_url = "https://img.icons8.com/fluency/344/merge-git.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the OpenDeck releases page URL")
    async def releases(self, ctx):
        embed = discord.Embed(color = discord.Colour.dark_green(), title = "https://github.com/nekename/OpenDeck/releases")
        embed.set_author(name = "Releases", icon_url = "https://img.icons8.com/fluency/344/downloads.png")
        await ctx.response.send_message(embed = embed)
