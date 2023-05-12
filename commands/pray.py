from commands.command import Command
from evennia import CmdSet
from ai.ai import ai_chat


class CmdPray(Command):
    """
    Pray to the gods and hope for an answer

    Usage:
        pray <something>

    """
    key = "pray"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        prompt = f"Respond to the following as if you are a merciful and all-powerful god that has knowledge of all things: {self.args.strip()}"

        resp = ai_chat(prompt)
        resp = resp.strip()
        if resp == '':
            self.caller.msg(
                "You listen, but hear nothing in response to your earnest plea. Maybe you should try again later?")
        else:
            self.caller.msg(
                f"A divine voice brimming with unlimited potential enters your mind: '{resp}'")
