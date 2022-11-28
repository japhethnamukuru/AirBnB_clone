#!/usr/bin/python3

"""
    This module contains the aairbnb console program
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Inherits from the Cmd super class from the cmd module
    """
    
    prompt  = "(hbnb) "

    def do_EOF(self, arg):
        """End of File command to exit the program"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
