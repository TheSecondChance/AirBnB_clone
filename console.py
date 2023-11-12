#!/usr/bin/python3
"""Command interpreter Console"""
import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


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
        elif line not in storage.classe():
            print("** class doesn't exist **")
        else:
            created_instance = eval(f"{line}()")
            storage.save()
            print(created_instance.id)

    def do_show(self, line):
        """Show Command
        String representation of an instance based on the class name"""
        class_id_name = line.split(" ")

        if len(line) == 0:
            print("** class name missing **")
        elif class_id_name[0] not in storage.classe():
            print("** class doesn't exist **")
        elif len(class_id_name) < 2:
            print("** instance id missing **")
        else:
            item = storage.all()
            key = "{}.{}".format(class_id_name[0], class_id_name[1])
            if key not in storage.all():
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
            if id_name[0] not in storage.classe():
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

    def do_all(self, line):
        """All Command
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()

        if line != "":
            items = line.split(" ")
            if items[0] not in storage.classe():
                print("** class doesn't exist **")
            else:
                for key, value in objects.items():
                    if key.split(".")[0] == items[0]:
                        print(str(value))
        else:
            for key, value in objects.items():
                print(str(value))

    def func(self):
        functons_dect = {"all": self.do_all}
        return functons_dect

    def do_update(self, line):
        """Update Command
        Updates an instance based on the class name and
        id by adding or updating attribute"""
        items_of_update = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif items_of_update[0] not in storage.classe():
            print("** class doesn't exist **")
        elif len(items_of_update) < 2:
            print("** instance id missing **")
        else:
            items = storage.all()
            key = "{}.{}".format(items_of_update[0], items_of_update[1])
            if key not in items:
                print("** no instance found **")
            elif len(items_of_update) < 3:
                print("** attribute name missing **")
            elif len(items_of_update) < 4:
                print("** value missing **")
            else:
                ful_item = items["{}.{}".format(
                    items_of_update[0], items_of_update[1])]
                item_first = items_of_update[2]
                item_first_v = items_of_update[3]

                try:
                    item_first_v = eval(item_first_v)
                except Exception:
                    pass
                setattr(ful_item, item_first, item_first_v)
                ful_item.save()

    def default(self, line):
        """Cmd module
        retrieve all instances of a class by using
        <class name>.all()"""
        separet_com = line.split(".")
        class_name = separet_com[0]
        second_tezaz = separet_com[1]
        second_tezaz_separet = second_tezaz.split("(")
        all_dict_commnd = second_tezaz_separet[0]

        if all_dict_commnd in self.func().keys():
            return self.func()[all_dict_commnd]("{} {}".format(class_name, ""))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
