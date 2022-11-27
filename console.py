#!/usr/bin/python3
"""This is the command interpreter for AirBnb clone console
    version : 0.0.1
"""

import cmd
import json
import re 
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """This is a custom console class for the AirBnb clone project
    """

    prompt = '(hbnb)'

def default(self, arg):
    """Attributes to the default behavior based on cmd module
    """
    return False

def handle_empty_line(self, arg):
    """removes the empty lines
    """
    return False

def do_quit(self, arg):
    """Exits the program using 'quit'
    Args:
    line(arg): provides the argument for exiting the terminal
    """
    return True

def do_EOF(self, arg):
    """ Exits the console and saves data by pressing ctrl+d
    """

    return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
