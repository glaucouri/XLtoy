# -*- coding: utf-8
"""
xltoy main cli (Command Line Interface)
"""
import click
from xltoy.collector import Collector, DiffCollector
from xltoy.utils import timeit




@click.group()
def cli(): pass

@click.command()
@click.option('--timeit', is_flag=True, help='Print out how many times it takes for the task')
@click.option('--yaml', is_flag=True, help='Print out the yaml hiearchical view')
@click.option('--data', is_flag=True, help='Collect only data, it will ignore formulas')
@click.argument('filename')
def collect(filename, **kwargs):
    click.echo('Collect an excel')
    with timeit("{} collect".format(filename), kwargs.get('timeit')):
        c = Collector(filename, only_data=kwargs.get('data'))
        if kwargs.get('yaml'):
            print(c.to_yaml())


@click.command()
@click.option('--timeit', is_flag=True, help='Print out how many times it takes for the task')
@click.option('--data', is_flag=True, help='Collect only data, it will ignore formulas')
@click.argument('filename1')
@click.argument('filename2')
def diff(filename1, filename2, **kwargs):
    with timeit("collect 2 files", kwargs.get('timeit')):
        d = DiffCollector(filename1,filename2, only_data=kwargs.get('data'))
        print(d.to_yaml())



cli.add_command(collect)
cli.add_command(diff)

if __name__ == '__main__':
    cli()
