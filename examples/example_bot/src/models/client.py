import typing

import tanjun


class MyClient(tanjun.Client):
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)

        self.set_human_only()
        ...
