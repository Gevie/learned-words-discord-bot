"""Command placeholder"""


class Command:
    def __init__(self, bot):
        self.bot = bot

    async def execute(self, ctx, *args):
        pass
