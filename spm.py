# Structural Pattern Matching
"""
def execute_command(command):
    match command.split():
        # case ['ls' | 'list', *paths, '--force']:
        #     for path in paths:
        #         print("Forced Listing files from", path,)
        case ['ls' | 'list' as command_name, *paths] as the_list if len(paths) > 1:
            for path in paths:
                print("Listing ALL files from", path,)
                print(f'{command_name=}, {the_list=}')
        case ['ls' | 'list', *paths] if len(paths) <= 1:
            print("Listing SINGLE files from", paths[0])
        case ['cd', path]:
            print("Changing directory from", path)
        case _:  # optional
            print("Unknown command")


# execute_command('ls . /home --force')
# print()
execute_command('ls . /amand')
print()
execute_command('ls /home')
print()
# execute_command('list . /home --force')
# print()
# execute_command('list . /amand')
# print()



def execute_command(command):
    match command:
        case {'command': 'ls', 'dirs': [_, *_]}:
            for dir in command['dirs']:
                print("Listing ALL files from", dir)
        case _:  # optional
            print("Unknown command")


execute_command({
    'command': 'ls',
    'dirs': ['/home', '/amand'],
})
"""
from dataclasses import dataclass


@dataclass
class Command:
    command: str
    dirs: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', dirs=[_, *_]):
            for dir in command.dirs:
                print("Listing ALL files from", dir)
        case _:  # optional
            print("Unknown command")


com = Command('ls', ['/home', '/amand'])
execute_command(com)
