# makeNewFile
The program I use to generate source files for recent projects.

It's written in basic Python 3 and does not require any other modules.

There are a few file types supported (and more to come):

- C Source
- C Header
- C++ Source
- C++ Header
- NASM Assembly Source

NASM Assembly and C source contain no special things.
C++ source contains C name guards, but commented out if you need them.
All header files contain include guards.

Please note, in order for makeNewFile to automaticly fill some portions (such as username and license type),
you need a JSON file called `mnfSettings.json` in your home directory.

Here is an example of one:

```
{
	"author": "Shrek",
	"licence": true,
	"licensetext": "mit"
}
```

This would create files that have the username "Shrek" and have a MIT license enabled.

Here is a list of available license types you can insert (and more to come):

- `mit`: The MIT License
- `apache2`: The Apache 2.0 Licence

IF YOU INSTALL THIS PROGRAM, you need to edit the first line, and set it to your Python 3 interpreter path.

For any other information, type `makeNewFile -h` when installed.
