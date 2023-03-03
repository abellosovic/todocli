# -*- coding: utf-8 -*-

import random

import bleach

from todocli import api
from todocli.formatters import txt_formatter, draw_table, json_formatter


def add(args):
    sanitize_text = bleach.clean(text=args.text)
    return api.add(text=sanitize_text)


def delete(args):
    if args.id.isalnum():
        if api.delete(args.id):
            print(f"ID: {args.id} deleted")
        else:
            print(f"ID '{args.id}' does not exist")


def get_all(args):
    data = api.get_all()
    if data:
        match args.format:
            case "txt":
                txt_formatter(data)
            case "table":
                draw_table(data)
            case "json":
                json_formatter(data)
    else:
        print("The todo list is empty")


def workflow(_):
    random_number = random.randrange(start=10, stop=100)
    for index in range(random_number):
        api.add(text=f"todo_{index}")
    all_todos = api.get_all()
    txt_formatter(all_todos)
    draw_table(all_todos)
    json_formatter(all_todos)
    for todo in all_todos:
        api.delete(todo.get("_id"))
    pass
