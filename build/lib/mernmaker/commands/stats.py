import click
import os

@click.command()
@click.argument('app_name')
def stats(app_name):
    """Display project statistics for the specified app."""
    
    def count_lines_of_code(directory):
        total_lines = 0
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(('.js', '.jsx', '.ts', '.tsx', '.py')):
                    filepath = os.path.join(dirpath, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for line in f)
        return total_lines

    backend_directory = os.path.join(app_name, 'backend')
    frontend_directory = os.path.join(app_name, 'frontend')

    loc = count_lines_of_code(backend_directory) + count_lines_of_code(frontend_directory)
    click.echo(f'Total Lines of Code: {loc}')
    click.echo('\nTest Coverage:')
