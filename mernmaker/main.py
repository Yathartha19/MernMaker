import click
from mernmaker.commands.create import create
from mernmaker.commands.changelog import changelog
from mernmaker.commands.stats import stats

@click.group()
def main():
    pass

main.add_command(create)
main.add_command(changelog)
main.add_command(stats)

if __name__ == '__main__':
    main()
