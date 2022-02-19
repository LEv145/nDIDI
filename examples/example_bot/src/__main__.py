import os

import hikari

from .models import MyClient
from .components import TestComponent


def main() -> None:
    token = os.getenv("BOT_TOKEN")

    if token is None:
        raise RuntimeError("'BOT_TOKEN' not specified in env")

    bot = hikari.GatewayBot(token=token)
    client = MyClient.from_gateway_bot(
        bot, declare_global_commands=[867344761970229258],
    ).add_prefix("!")

    client.add_component(TestComponent("test"))  # Pure dependency injection!

    bot.run()


if __name__ == "__main__":
    main()
