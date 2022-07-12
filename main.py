
import click
import scrape


@click.command()
@click.option('--n', default=1, type=int, show_default=True, help="The number of questions generated")
@click.option("--diff", default="EZ", type=click.Choice(['EZ', 'MD', 'H']),  help="The difficulty of the questions")
def hello(n, diff):
    num = int(n)
    diff_lvl = str(diff)


if __name__ == '__main__':
    hello()
