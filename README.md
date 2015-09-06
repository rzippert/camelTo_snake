# camelTo_snake
A simple python script to convert camelCase text to snake_case text.

## Usage ##
Place the script wherever you like and use the files and directories 
you want to convert as arguments.

Examples:

	To convert the file file.txt and everything on 2 other folders:
	`./camelTo_snake /path/to/file.txt /path/to/folder /somewhereElse`

	To convert everything under your home directory:
	`python camelTo_snake ~`

## Observations ##
There are no confirmation prompts and it won't smartly ignore anything.
The file needs execution permission in order to use the `./camelTo_snake`
call.
There is no backup system and no way to undo what this script does.
You can ask for features, but I have no real intention of improving this
much.
In all else, enjoy :D
