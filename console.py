#!/usr/bin/python3

"""
    This module contains the aairbnb console program
"""
import cmd


class HBNBCommand(Cmd.cmd):
    """
        Inherits from the Cmd super class from the cmd module
    """
    pass

if __name__ = '__main__':
    HBNBCommand().cmdloop()
