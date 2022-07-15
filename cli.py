import os
import click
import scrape
import random
import pickle
from operator import itemgetter

CHOICE_DIFF = {"E": "Easy", "MD": "Intermediate", "H": "Hard"}


@click.group()
@click.option(
    '--client-id',
    help='Your reddit client-id key'
)
@click.option(
    '--secret',
    help='Your reddit secret key'
)
@click.option(
    '--user-agent',
    help='Your reddit user_agent key'
)
@click.option(
    '--config-file', '-c',
    type=click.Path(),
    default='~/.reddit.cfg',
)
@click.pass_context
def main(ctx, client_id, secret, user_agent, config_file):
    """
    A cli app that returns a coding question(s) file of varying difficulty. The 
    questions are web scrape from reddit. The subreddit that is scraped is from /r/dailyprogrammer. You can get free credentials from https://www.reddit.com/prefs/apps.
    """
    filename = os.path.expanduser(config_file)
    # add a contiadon if only or
    if not client_id or not secret or not user_agent and os.path.exists(filename):
        file = open(filename, 'rb')
        cfg = pickle.load(file)
        file.close()
        client_id, secret, user_agent = itemgetter(
            'client_id', 'secret', 'user_agent')(cfg)

    ctx.obj = {
        'config_file': filename,
        'client_id': client_id, 'secret': secret, 'user_agent': user_agent
    }


@main.command()
@click.pass_context
def config(ctx):
    """
    Store configuration values in a file.
    Default file location : ~/.reddit.cfg
    """
    config_file = ctx.obj['config_file']

    client_id = click.prompt(
        "Please enter your client_id",
        default=ctx.obj.get('client_id', '')
    )
    secret = click.prompt(
        "Please enter your secret",
        default=ctx.obj.get('secret', '')
    )
    user_agent = click.prompt(
        "Please enter your user_agent",
        default=ctx.obj.get('user_agent', '')
    )

    content = {'client_id': client_id,
               'secret': secret, 'user_agent': user_agent}

    with open(config_file, "wb") as cfg:
        pickle.dump(content, cfg)

    click.echo("Saved info @ "+config_file)


@main.command()
@click.option('--n', default=1, type=click.IntRange(1, 10), show_default=True, help="The number of questions generated.")
@click.option('--diff', type=click.Choice(['E', 'MD', 'H']),  help="The difficulty of the questions. Default is random difficulty")
@click.pass_context
def get(ctx, n, diff):
    """
    Get coding question(s).
    """
    client_id, secret, user_agent = itemgetter(
        'client_id', 'secret', 'user_agent')(ctx.obj)

    if not client_id or not secret or not user_agent:
        click.echo("NEED reddit keys\n**Run config command to add**")
        return

    txt_q = "Questions" if n > 1 else "Question"
    lvl = CHOICE_DIFF.get(diff) if diff else random.choice(
        list(CHOICE_DIFF.values()))

    r = scrape.Obj(client_id, secret, user_agent)

    click.echo(f"--Getting {lvl} {txt_q}--")
    submissions = r.getRandomSubmissions(lvl, n)
    for submission in submissions:
        r.createFile(submission)

    click.echo("Done :-)")


if __name__ == '__main__':
    main()
