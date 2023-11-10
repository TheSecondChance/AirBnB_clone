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

    def do_create(self, line):
        """Create Command to create BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classe:
            print("** class doesn't exist **")
        else:
            created_instance = BaseModel()
            created_instance.save()
            print(created_instance.id)

    def do_show(self, line):
        """Show Command
        String representation of an instance based on the class name"""
        class_id_name = line.split(" ")

        if len(line) == 0:
            print("** class name missing **")
        elif class_id_name[0] not in self.classe:
            print("** class doesn't exist **")
        elif len(class_id_name) < 2:
            print("** instance id missing **")
        else:
            item = storage.all()
            key = "{}.{}".format(class_id_name[0], class_id_name[1])
            if key not in item:
                print("** no instance found **")
            else:
                print(item[key])

    def do_destroy(self, line):
        """Destroy Command
        Deletes an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
        else:
            id_name = line.split()
            if id_name[0] not in self.classe:
                print("** class doesn't exist **")
            elif len(id_name) < 2:
                print("** instance id missing **")
            else:
                items = storage.all()
                key = "{}.{}".format(id_name[0], id_name[1])
                if key in items:
                    del items[key]
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
