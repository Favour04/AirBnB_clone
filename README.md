# DESCRIPTION
This project is aimed to create the clone of AirBnB site
## The Console
the console is developed for easy testing of the backend
and to allow the backend to be created and tested even with
out the front end.
### How to start the console
1. download the the file from ... or clone the repo
1. on the root directory run ./console
### How to use the console
1. After starting the console type help for further 
explaination and available comand
#### example
$ ./console
(hbnb) help

$ help create
### Examples
1.	(hbnb) help

	Dcumented commands (type help <topic>):
	=======================================
	EOF  create  help  quit

	Undocumented commands:
	======================
	all  destroy  show  update

1. 	(hbnb) help create destroy
	*** No help on create destroy

1. 	(hbnb) help create

            	creates new instance of a class
            	USEAGE: create <class name>

1.	(hbnb) create User
	a43de9a7-a825-4709-9330-7d197a21df07

1.	(hbnb) create BaseModel
	3ce0a8b4-2e65-4049-8abf-4b635d936480

1.	(hbnb) show User f52997a8-cc9b-41a4-89ea-b06292516f00
	[User] (f52997a8-cc9b-41a4-89ea-b06292516f00) {'id': 'f52997a8-cc9b-41a4-89ea-b06292516f00', 'created_at'...

1.	(hbnb) quit
	$
