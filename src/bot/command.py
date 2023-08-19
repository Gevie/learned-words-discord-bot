"""The command handler of the learned words bot"""

from discord.ext import commands


class Command(commands.Cog):
    """
    Handles Discord commands and Discord events
    """

    def __init__(self, bot):
        """
        Initialize the command class

        Args:
            bot: The discord bot
        """
        self.bot = bot

    @commands.command(name='help', pass_context=False)
    async def help(self, ctx) -> None:
        """
        Displays help regarding the bot, provides all commands and usages.

        Args:
            ctx: Represents the :class:`.Context`

        Returns:
            None
        """
        pass

    @commands.command(name='learn')
    async def learn_word(self, ctx, word, translation, *definition) -> None:
        """
        Saves a new word with its translation and optional definition into the database

        Args:
            ctx: Represents the :class:`.Context`
            word (str): The word to be translated
            translation (str): The translation of the word
            *definition (str): The optional definition of the word
        """
        definition_text = ' '.join(definition) if definition else '*No definition provided*'
        await ctx.send(f'Learned: {word} - {translation}\nDefinition: {definition_text}')

