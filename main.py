
import click
import scrape

# @click.command()
# @click.argument('name', default='guest')
# @click.argument('age', type=int)
# def hello(name, age):
#     click.echo(f'{name} is {age} years old')


def hello():
    r = scrape.Obj()
    r.getRandomChallenge()


if __name__ == '__main__':
    hello()
