#!/usr/bin/env python
import click

from sheets_todo_list.done import Done
from sheets_todo_list.projects import Projects
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


@cli.command()
def clean_done_today():
    """
    Cleans the done today section
    """
    Done().clean_today()

@cli.command()
def sort_projects():
    """
    Cleans the done today section
    """
    Projects().sort()

if __name__ == '__main__':
    cli()

