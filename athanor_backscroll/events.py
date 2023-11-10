from rich.console import Console


class NullWriter:
    def write(self, *args, **kwargs):
        pass

    def flush(self):
        pass


CONSOLE = None


def get_console() -> Console:
    global CONSOLE
    if CONSOLE:
        return CONSOLE
    CONSOLE = Console(
        color_system="truecolor", file=NullWriter(), width=78, record=True
    )


def rich_print(*args, **kwargs):
    console = get_console()
    new_kwargs = {"highlight": False}
    new_kwargs.update(kwargs)
    console.print(*args, **new_kwargs)
    return console.export_text(clear=True, styles=True)


def character_at_post_msg_receive(character, from_obj=None, **kwargs):
    if options := kwargs.get("options", dict()):
        if options.get("no_backscroll", False):
            return
    if text_kw := kwargs.get("text", None):
        text = text_kw[0] if isinstance(text_kw, tuple) else text_kw
        if text:
            character.backscroll_records.create(text=text)
    if rich_kw := kwargs.get("rich", None):
        rich_renderable = rich_kw[0] if isinstance(rich_kw, tuple) else rich_kw
        text = rich_print(rich_renderable)
        if text:
            character.backscroll_records.create(text=text)
