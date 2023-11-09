#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """Commnad casll"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Shouldn't execute anything"""
        pass

    def do_EOF(self, line):
        """End Of File character"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
