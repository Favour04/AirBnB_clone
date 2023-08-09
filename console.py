#!/usr/bin/python3
"""
    This module contian hbnb
    cosole program
"""


from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
import copy
from datetime import datetime
from models.place import Place
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
    """
        This class is a command
        line interpreter.
        * Custom prompt: (hbnb)
        * quit and EOF to exit the program
        * help (this action is provided by default
          by cmd but you should keep it updated and
          documented as you work through tasks)
        * create: Creates new instance of a class
        * show: Prints the string representation
          of a an object
        * destroy: Deletes an instance base on name&id
        * all: print all string rep of all instance
        * update: Updates insatance based on name & id
    """

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
        objs = storage.all()
        args = line.split()

        if line == '':
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **') 
        else:
            obj_id = f"{args[0]}" + '.' + f"{args[1]}"
            objnum = len(objs.keys())
            count = 1
            for key in objs.keys():
                if key == obj_id:
                    print(objs[key])
                    break
                elif objnum == count:
                    print('** no instance found **')
                    break
                count += 1

    def do_destroy(self, line):
        objs = storage.all()
        args = line.split()

        if line == '':
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            obj_id = f"{args[0]}" + '.' + f"{args[1]}"
            objnum = len(objs.keys())
            count = 1
            for key in objs.keys():
                if key == obj_id:
                    del objs[key]
                    storage.save()
                    break
                elif objnum == count:
                    print('** no instance found **')
                    break
                count += 1

    def do_all(self, line):
        objs = storage.all()
        if line == '':
            lists = []
            for key in objs.keys():
                lists.append(str(objs[key]))
            print(lists)
        elif line in classes.keys():
            lists = []
            obj = copy.deepcopy(objs)
            for key in obj.keys():
                if obj[key].to_dict()['__class__'] == line:
                    lists.append(str(objs[key]))
            print(lists)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = shlex.split(line)

        if line == '':
            print('** class name missing **')
        elif args[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif len(args) == 2:
            obj_id = f"{args[0]}" + '.' + f"{args[1]}"
            if obj_id in storage.all().keys():
                print('** attribute name missing **')
            else:
                print('** no instance found **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            obj_id = f"{args[0]}" + '.' + f"{args[1]}"
            for key in storage.all().keys():
                objnum = len(storage.all().keys())
                count = 1
                if key == obj_id:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
                    break
                elif objnum == count:
                    print('** no instance found **')
                    break
                count += 1

    def emptyline(self):
        """
            This is to make sure an empty line dosent
            execute anythign.
        """
        return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
