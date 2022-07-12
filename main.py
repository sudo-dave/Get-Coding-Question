
import click
import scrape


choice_diff = {"E": "Easy", "MD": "Intermediate", "H": "Hard"}


@click.command()
@click.option('--n', default=1, type=click.IntRange(1, 10), show_default=True, help="The number of questions generated")
@click.option("--diff", default="E", type=click.Choice(['E', 'MD', 'H']),  help="The difficulty of the questions")
def hello(n, diff):
    num = int(n)
    lvl = choice_diff.get(str(diff))
    r = scrape.Obj()
    for _ in range(num):
        submission = r.getRandomSubmission(lvl)
        r.createFile(submission)
    print("Done")


if __name__ == '__main__':
    hello()
