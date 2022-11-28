#!/usr/bin/python3
"""
    This module contains the aairbnb console program
"""
import cmd
import models


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

    def do_create(self, arg):
        """Creates a new instance of a Model"""
        if arg:
            try:
                args = arg.split()
                template = models.test_classes[args[0]]
                new_instance = template()
                try:
                    for pair in args[1:]:
                        pair_split = pair.split("=")
                        if (hasattr(new_instance, pair_split[0])):
                            value = pair_split[1]
                            flag = 0
                            if (value.startswith('"')):
                                value = value.strip('"')
                                value = value.replace("\\", "")
                                value = value.replace("_", " ")
                            elif ("." in value):
                                try:
                                    value = float(value)
                                except:
                                    flag = 1
                            else:
                                try:
                                    value = int(value)
                                except:
                                    flag = 1
                            if (not flag):
                                setattr(new_instance, pair_split[0], value)
                        else:
                            continue
                    new_instance.save()
                    print(new_instance.id)
                except:
                    new_instance.rollback()
            except:
                print("** class doesn't exist **")
                models.storage.rollback()
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """string representation of an instance"""
        if arg:
            arg = arg.split()
            if arg[0] in models.test_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        print(models.storage.all()[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        if arg:
            arg = arg.split()
            if arg[0] in models.test_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        garbage = models.storage.all().pop(key)
                        del(garbage)
                        models.storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_all(self, arg):
        """string representation of all instances"""
        result = []
        if arg:
            arg = arg.split()
            if arg[0] in models.test_classes:
                current_inst = models.test_classes[arg[0]]
                for i, o in models.storage.all(current_inst).items():
                    if i.split('.')[0] == arg[0]:
                        result.append(str(o))
            else:
                print("** class doesn't exist **")
        else:
            for instance, obj in models.storage.all().items():
                result.append(str(obj))
        if result:
            print(result)

    def do_update(self, arg):
        """Updates an instance adding or updating attribute"""
        if arg:
            arg = arg.split()
            if arg[0] in models.test_classes:
                if len(arg) > 1:
                    key = "{}.{}".format(arg[0], arg[1])
                    try:
                        instance = models.storage.all()[key]
                        if len(arg) > 2:
                            if len(arg) > 3:
                                setattr(instance, arg[2], arg[3].strip('"'))
                                instance.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    except:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

	


if __name__ == '__main__':
    HBNBCommand().cmdloop()
