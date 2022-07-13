
from pydoc import cli
import click
import scrape
import random

choice_diff = {"E": "Easy", "MD": "Intermediate", "H": "Hard"}


@click.command()
@click.option('--n', default=1, type=click.IntRange(1, 10), show_default=True, help="The number of questions generated")
@click.option("--diff", type=click.Choice(['E', 'MD', 'H']),  help="The difficulty of the questions")
def hello(n, diff):
    num = int(n)
    lvl = choice_diff.get(diff) if diff else random.choice(
        list(choice_diff.values()))
    r = scrape.Obj()
    txt_q = "Questions" if n > 1 else "Question"

    click.echo(f"Getting {lvl} {txt_q}...")

    for _ in range(num):
        submission = r.getRandomSubmission(lvl)
        r.createFile(submission)

    click.echo("Done :-)")


if __name__ == '__main__':
    hello()
