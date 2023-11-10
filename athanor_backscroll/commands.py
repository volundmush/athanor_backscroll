from athanor.commands import AthanorCommand


class CmdBackscroll(AthanorCommand):
    """
    View stored backscroll for this character.

    Usage:
        backscroll [<count>]

    Where <count> is the number of lines. Defaults to 20.
    Viewing backscroll will not add to backscroll.
    """

    key = "backscroll"
    help_category = "Comms"

    def func(self):
        if not self.args:
            count = 20
        else:
            try:
                count = int(self.args)
            except ValueError:
                self.msg("Invalid count.", options={"no_backscroll": True})
                return
        if not (backscroll := self.caller.backscroll_records.all()):
            self.msg("No backscroll found.", options={"no_backscroll": True})
            return

        out = []
        for record in backscroll[-count:]:
            out.append(
                f"> {self.account.datetime_format(dt=record.timestamp, template='%c')}\n{record.text}"
            )

        self.msg("\n".join(backscroll[-count:]), options={"no_backscroll": True})
