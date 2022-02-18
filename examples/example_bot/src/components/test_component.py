import tanjun
import ndidi


class TestComponent(ndidi.AutoComponent):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

        help_group = tanjun.slash_command_group("slash_group", "I'm slash group!")
        help_group.add_command(self.test_slash_command)  # type: ignore
        self.add_slash_command(help_group)

        self.load_commands()

    @ndidi.as_slash_command("test", "command")
    async def test_slash_command(self, ctx: tanjun.abc.MessageContext) -> None:
        await ctx.respond("I'm slash command!")

    @ndidi.as_message_command_group("test")
    async def test_message_command_group(self, ctx: tanjun.abc.MessageContext) -> None:
        await ctx.respond("I'm message group command!")

    @test_message_command_group.with_command
    @ndidi.as_message_command("hello")
    async def test_message_command(self, ctx: tanjun.abc.MessageContext) -> None:
        await ctx.respond("I'm message command, too!")
