class MacroCommand:
    """명령 리스트를 실행하는 명령"""

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()
