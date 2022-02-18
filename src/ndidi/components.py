from __future__ import annotations

import types
import typing

import tanjun


CommandProtocolT = typing.TypeVar("CommandProtocolT", bound="CommandProtocol")


class BindingSlashCommand(tanjun.SlashCommand):
    __slots__ = ()

    def load_into_component(self, component: tanjun.abc.Component) -> None:
        super().load_into_component(component)
        self._callback = tanjun.injecting.CallbackDescriptor(
            types.MethodType(self._callback.callback, component),
        )


class BindingMessageCommand(tanjun.MessageCommand):
    __slots__ = ()

    def load_into_component(self, component: tanjun.abc.Component) -> None:
        super().load_into_component(component)
        self._callback = tanjun.injecting.CallbackDescriptor(
            types.MethodType(self._callback.callback, component),
        )


class BindingMessageCommandGroup(tanjun.MessageCommandGroup):
    __slots__ = ()

    def load_into_component(self, component: tanjun.abc.Component) -> None:
        super().load_into_component(component)
        self._callback = tanjun.injecting.CallbackDescriptor(
            types.MethodType(self._callback.callback, component),
        )
