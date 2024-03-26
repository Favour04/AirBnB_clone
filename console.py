#!/usr/bin/python3
"""
    This module contian hbnb
    cosole program
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
from models.place import Place
import re
from models.review import Review
import shlex
from models.state import State
from models import storage
from models.user import User


classes = {
            'Amenity': Amenity,
            'BaseModel': BaseModel,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User,
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program"""
        # return end of file
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        # return end of file
        return self.do_EOF(line)

    def do_create(self, line):
        """
            creates new instance of a class
            USEAGE: create <class name>
        """
        if line == '':
            print("** class name missing **")
        elif line == 'Amenity':
            obj = Amenity()
            obj.save()
            print(obj.id)
        elif line == 'BaseModel':
            obj = BaseModel()
            obj.save()
            print(obj.id)
        elif line == 'City':
            obj = City()
            obj.save()
            print(obj.id)
        elif line == 'Place':
            obj = Place()
            obj.save()
            print(obj.id)
        elif line == 'Review':
            obj = Review()
            obj.save()
            print(obj.id)
        elif line == 'State':
            obj = State()
            obj.save()
            print(obj.id)
        elif line == 'User':
            obj = User()
            obj.save()
            print(obj.id)
        elif line not in classes.keys():
            print("** class doesn't exist **")

    def do_show(self, line):
        """
            show all instance of a class
            USEAGE: show <class name>
        """
        objs = storage.all()
        args = line.split()

        if line == '':
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            object_key = f"{args[0]}" + '.' + f"{args[1]}"
            if object_key in objs:
                print(objs[object_key])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """
            delete an instance of a class
            USEAGE: destroy <class name> <id>
        """
        objs = storage.all()
        args = line.split()

        if line == "":
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            object_key = f"{args[0]}" + '.' + f"{args[1]}"
            objnum = len(objs.keys())
            if object_key in objs:
                del objs[object_key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """
            show all instances stored or
            all instance of a class stored
            USEAGE: (1) all
                    (2) all <class name>
        """
        objs = storage.all()
        if line == "":
            lists = []
            for key in objs.keys():
                lists.append(str(objs[key]))
            print(lists)
        elif line in classes.keys():
            lists = []
            for obj in objs.values():
                if obj.__class__.__name__ == line:
                    lists.append(str(obj))
            print(lists)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
            update an instance of a class
            USEAGE: update <class name> <id> 'feild' 'value'
        """
        args = shlex.split(line)
        objects = storage.all()
        if len(args) > 2 or len(args) == 2:
            obj_id = f"{args[0]}" + '.' + f"{args[1]}"
        else:
            obj_id = None

        if line == '':
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif len(args) == 2:
            if obj_id in objects.keys():
                print('** attribute name missing **')
            else:
                print('** no instance found **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            if obj_id in objects.keys():
                setattr(objects[obj_id], args[2], args[3])
                objects[obj_id].save()
            else:
                print('** no instance found **')

    def emptyline(self):
        """
            This is to make sure an empty line dosent
            execute anythign.
        """
        return ""

    def do_count(self, line):
        """
            count all instances of a class
            USEAGE: count <class name>
        """
        objs = storage.all()
        count = 0
        args = line.split()
        if line == "":
            print("** class name missing **")
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            for obj in objs.values():
                if obj.__class__.__name__ == args[0]:
                    count += 1
            print(count)

    def onecmd(self, line):
        """
            This is to make sure the command is
            executed.
        """
        pattern = r'(\w+).(\w+)\((.+)?\)'
        match = re.search(pattern, line)
        if match is not None:
            command = match.group(2)
            modelname = match.group(1)
            arguments = match.group(3)

            """
                All extra commands are handled here
            """
            if arguments is not None:
                arguments = arguments.split(', ')
                line = command + ' ' + modelname + ' ' + arguments[
                                                        0].strip('"\'')
                if len(arguments) > 1:
                    line += ' ' + ' '.join(arguments[1:])
            else:
                line = command + ' ' + modelname
        return cmd.Cmd.onecmd(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
