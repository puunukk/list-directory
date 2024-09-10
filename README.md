# Directory Tree Printing Script

This Python script lists the directory structure of a given path in a visually formatted tree-like structure. It includes support for ignoring files and directories, similar to a .gitignore file, and allows the option to show all files despite the ignore rules.
Features

  * Displays a directory structure in a tree format.
  * Supports custom ignore lists for files and directories.
  * Option to override the ignore list and display all files.
  * Fully type-safe with inline documentation and comments.
  * Organized using inner functions for better encapsulation and code structure.

Output example:
> ```
> /list-directory:
> ├── .ignorelist
> ├── list_dir.py
> └── README.md
> ```


### Basic Usage
```
python list_dir.py <enter path, default value is ".">
```
This will display the directory structure starting from the current directory (default behavior).

### Display a Specific Directory
```
python list_dir.py /path/to/directory
```
This will display the directory structure starting from the specified path.

### Use a Custom Ignore File
```
python list_dir.py --ignore-file /path/to/custom.ignorelist
```

This allows you to specify a custom file that contains patterns to ignore, similar to `.gitignore`.

### Show All Files _(Ignore Ignore List)_
```
python list_dir.py --show-all
```
This option will show all files and directories, ignoring the specified ignore patterns.

### Combine Options

You can combine options to specify a path, use a custom ignore file, and show all files:
```
python list_dir.py /path/to/directory --ignore-file /path/to/custom.ignorelist --show-all
```


## Ignore File Format

By default, the script looks for an `.ignorelist` file in the current directory. This file contains patterns for files or directories to ignore, one per line. Patterns are similar to `.gitignore`.

Default `.ignorelist` items:
  - `*.log`: Ignore all .log files.
  - `/node_modules/`: Ignore the `node_modules` directory.
  - `/build/`: Ignore the build directory.
  - `/git/`: Ignore the `.git` hidden folder.
  - `/intelij/`: Ignore the .intelij hidden folder.
  - `/vscode/`: Ignore the .vscodium hidden folder.
