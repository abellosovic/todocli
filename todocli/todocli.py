# -*- coding: utf-8 -*-

import argparse
import logging

from todocli.controller import get_all, add, delete, workflow

logger = logging.getLogger(__name__)


def get_all_cli_definition(parser):
    parser.add_argument(
        "-f", "--format", type=str, required=True, choices=["txt", "table", "json"]
    )


def add_cli_definition(parser):
    parser.add_argument("text")


def delete_cli_definition(parser):
    parser.add_argument("id", type=str)


def workflow_cli(_):
    pass


PARSERS = [
    {
        "command": "getall",
        "help": "get all todos",
        "definition": get_all_cli_definition,
        "entrypoint": get_all,
    },
    {
        "command": "add",
        "help": "add a todo",
        "definition": add_cli_definition,
        "entrypoint": add,
    },
    {
        "command": "delete",
        "help": "delete a todo",
        "definition": delete_cli_definition,
        "entrypoint": delete,
    },
    {
        "command": "workflow",
        "help": "test workflow",
        "definition": workflow_cli,
        "entrypoint": workflow,
    },
]


def todo_cli():
    parser = argparse.ArgumentParser(prog="Todo CLI")
    subparsers = parser.add_subparsers(help="Todo commands")

    for cmd in PARSERS:
        _parser = subparsers.add_parser(cmd["command"], help=cmd["help"])
        cmd["definition"](_parser)
        _parser.set_defaults(func=cmd["entrypoint"])

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
