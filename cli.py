#!/usr/bin/env python
import click
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

config = {
    'inbox': {
        'col': 'A',
        'top': 'A3',
        'range': 'A3:A20'
    },
    'today': {
        'col': 'B',
        'top': 'B3',
        'range': 'B3:B20'
    },
    'done': {
        'col': 'C',
        'top': 'C3',
        'range': 'C3:C20'
    }
}

def get_worksheet():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('./credentials.json', scope)
    gc = gspread.authorize(credentials)

    sh = gc.open_by_key('16IEVEWcVN36Fxw-mjgW_1FEW7GeGytm8O8_y9iFEiNc')
    worksheet = sh.get_worksheet(0)

    return worksheet

def add_to_top(content, worksheet, column_name):
    cell_list = worksheet.range(config[column_name]['range'])

    # check if there's still space left and clean up the cells
    has_empty = False
    reshufled_list = [content]
    for i in cell_list:
        if i.value == "":
            has_empty=True
        else:
            reshufled_list.append(i.value)
            i.value = ''

    if not has_empty:
        raise Exception("No space left in the inbox clean it up first!")

    worksheet.update_cells(cell_list)
    the_range = f'{config[column_name]["top"]}:{config[column_name]["col"]}{2 + len(reshufled_list)}'
    cell_list = worksheet.range(the_range)

    for indice, i in enumerate(cell_list):
        i.value = reshufled_list[indice]

    worksheet.update_cells(cell_list)


@click.group()
def cli():
    pass

@cli.command()
@click.option('--content',
              required=True,
              help='the content to add')
def add_to_inbox(content):
    worksheet = get_worksheet()
    add_to_top(content, worksheet, 'inbox')



@cli.command()
@click.option('--content',
              required=True,
              help='the content to add')
def add_to_today(content):
    worksheet = get_worksheet()
    add_to_top(content, worksheet, 'today')

@cli.command()
@click.option('--content',
              required=True,
              help='the content to add')
def add_to_done_today(content):
    worksheet = get_worksheet()
    add_to_top(content, worksheet, 'done')


if __name__ == '__main__':
    cli()

