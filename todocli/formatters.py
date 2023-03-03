# -*- coding: utf-8 -*-

import json

import termtables


def draw_table(json_data):
    header = ["id", "text"]
    data = [[todo.get("_id"), todo.get("text")] for todo in json_data]
    termtables.print(
        data=data,
        header=header,
        style=termtables.styles.markdown,
        padding=(0, 1),
        alignment="cc",
    )


def json_formatter(json_data):
    print(json.dumps(json_data, indent=2))


def txt_formatter(json_data):
    print("id,text")
    for todo in json_data:
        print(f"{todo.get('_id')},{todo.get('text')}")
