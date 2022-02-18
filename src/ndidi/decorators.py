import typing

from .components import (
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
        return BindingMessageCommand(
            callback,
            name,
            *names,
            **kwargs,
        )

    return decorator


def as_binding_message_command_group(
    name: str,
    *names: str,
    strict: bool = False,
    **kwargs: typing.Any,
):
    def decorator(callback):
        return BindingMessageCommandGroup(
            callback,
            name,
            *names,
            strict=strict,
            **kwargs,
        )

    return decorator
