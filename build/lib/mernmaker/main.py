import click
from mernmaker.commands.create import create
from mernmaker.commands.changelog import changelog
from mernmaker.commands.stats import stats
from mernmaker.commands.lint import lint

@click.group()
def main():
    pass

main.add_command(create)
main.add_command(changelog)
main.add_command(stats)
main.add_command(lint)

if __name__ == '__main__':
    main()
