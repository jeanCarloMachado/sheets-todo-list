#!/usr/bin/env python
import click

from sheets_todo_list.insert_content import InsertContent


@click.group()
def cli():
    pass

@cli.command()
@click.option('--content', '-c',
              required=True,
              help='the content to add')
def add_to_inbox(content):
    InsertContent().to_the_top(content, 'inbox')



@cli.command()
@click.option('--content','-c',
              required=True,
              help='the content to add')
def add_to_today(content):
    InsertContent().to_the_top(content, 'today')

@cli.command()
@click.option('--content', '-c',
              required=True,
              help='the content to add')
def add_to_done_today(content):
    InsertContent().to_the_top(content, 'done')


if __name__ == '__main__':
    cli()

