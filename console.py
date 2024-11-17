#!/usr/bin/python
"""
Module for console
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def help_quit(self, arg):
        """

        """
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
