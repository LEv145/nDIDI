from __future__ import annotations

import inspect
import typing

import tanjun


class BaseComponent(tanjun.Component):
    __slots__ = ()

    def load_commands(self, cls: typing.Any | None = None) -> None:
        if cls is None:
            cls = self

        self.load_from_scope(scope=dict(inspect.getmembers(cls)))
