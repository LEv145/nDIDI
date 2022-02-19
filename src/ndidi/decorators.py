import typing

import tanjun

from .binding_commands import (
    BindingSlashCommand,
    BindingMessageCommand,
    BindingMessageCommandGroup,
)


def as_binding_slash_command(
    name: str,
    description: str,
    *,
    always_defer: bool = False,
    default_permission: bool = True,
    default_to_ephemeral: typing.Optional[bool] = None,
    is_global: bool = True,
    sort_options: bool = True,
    **kwargs: typing.Any,
):
    def decorator(callback):
        if isinstance(
            callback,
            (tanjun.abc.MenuCommand, tanjun.abc.MessageCommand, tanjun.abc.SlashCommand)
        ):
            return BindingSlashCommand(
                callback.callback,
                name,
                description,
                always_defer=always_defer,
                default_permission=default_permission,
                default_to_ephemeral=default_to_ephemeral,
                is_global=is_global,
                sort_options=sort_options,
                _wrapped_command=callback,
                **kwargs,
            )

        return BindingSlashCommand(
            callback,
            name,
            description,
            always_defer=always_defer,
            default_permission=default_permission,
            default_to_ephemeral=default_to_ephemeral,
            is_global=is_global,
            sort_options=sort_options,
            **kwargs,
        )

    return decorator


def as_binding_message_command(
    name: str,
    *names: str,
    **kwargs: typing.Any,
):
    def decorator(callback):
        if isinstance(
            callback,
            (tanjun.abc.MenuCommand, tanjun.abc.MessageCommand, tanjun.abc.SlashCommand)
        ):
            return BindingMessageCommand(
                callback.callback,
                name,
                *names,
                _wrapped_command=callback,
            )

        return BindingMessageCommand(callback, name, *names, **kwargs)

    return decorator


def as_binding_message_command_group(
    name: str,
    *names: str,
    strict: bool = False,
    **kwargs: typing.Any,
):
    def decorator(callback):
        if isinstance(
            callback,
            (tanjun.abc.MenuCommand, tanjun.abc.MessageCommand, tanjun.abc.SlashCommand)
        ):
            return BindingMessageCommandGroup(
                callback.callback,
                name,
                *names,
                strict=strict,
                _wrapped_command=callback,
            )

        return BindingMessageCommandGroup(
            callback,
            name,
            *names,
            strict=strict,
            **kwargs,
        )

    return decorator
