import os
import argparse
from typing import List


def load_ignore_list(ignore_file: str) -> List[str]:
    """
    Load the ignore patterns from the specified ignore file.

    Args:
        ignore_file (str): The path to the ignore file.

    Returns:
        List[str]: A list of patterns from the ignore file. If the file does not exist,
                   an empty list is returned.
    """
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            # Read the ignore patterns, remove empty lines and comments
            ignore_patterns = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
        return ignore_patterns
    return []


def should_ignore(path: str, ignore_patterns: List[str]) -> bool:
    """
    Determine if a file or directory should be ignored based on the ignore patterns.

    Args:
        path (str): The file or directory path to check.
        ignore_patterns (List[str]): A list of patterns to ignore.

    Returns:
        bool: True if the path matches an ignore pattern, otherwise False.
    """
    for pattern in ignore_patterns:
        if pattern in path:  # Simple substring match; could be extended for regex
            return True
    return False


def list_directory(
    start_path: str,
    ignore_patterns: List[str],
    show_all: bool = False
) -> None:
    """
    Recursively list the directory structure starting from the given directory.

    Args:
        start_path (str): The directory to start listing from (default is current directory).
        ignore_patterns (List[str]): A list of patterns to ignore (default is empty list).
        show_all (bool): Flag to show all files and directories, ignoring the ignore list (default is False).
    """

    def print_tree(root: str, prefix: str = "") -> None:
        """
        Helper function to recursively print the directory tree.

        Args:
            root (str): The current root directory to print.
            prefix (str): The prefix used for formatting the tree structure.
        """
        # Get all items in the directory
        items: List[str] = os.listdir(root)
        # Sort items so that directories come first
        items.sort(key=lambda x: (os.path.isfile(os.path.join(root, x)), x.lower()))

        for i, name in enumerate(items):
            path = os.path.join(root, name)
            is_last: bool = i == len(items) - 1

            # Skip files/directories that match the ignore patterns if `show_all` is False
            if not show_all and should_ignore(path, ignore_patterns):
                continue

            if os.path.isdir(path):
                # Print the directory, use '└──' if it's the last directory item
                print(f"{prefix}├── {name}/" if not is_last else f"{prefix}└── {name}/")
                # Recurse into the directory with updated prefix
                new_prefix = prefix + ("│   " if not is_last else "    ")
                print_tree(path, new_prefix)
            else:
                # Print the file, use '└──' if it's the last file item
                print(f"{prefix}├── {name}" if not is_last else f"{prefix}└── {name}")

    # Get the absolute path and print it as the "root"
    abs_path: str = os.path.abspath(start_path)
    print(f"{abs_path}:")
    print_tree(start_path)


if __name__ == "__main__":
    # Setup argparse for handling command-line arguments
    parser = argparse.ArgumentParser(description="Display a directory structure in tree format.")

    # Positional argument: the path to the directory (optional, defaults to current directory)
    parser.add_argument('path',
                        nargs='?',
                        default='.',
                        help="Path to the directory (default is current directory).")

    # Optional argument: the path to the ignore file (defaults to `.ignorelist`)
    parser.add_argument('--ignore-file',
                        default='.ignorelist',
                        help="Path to the ignore file (default is .ignorelist).")

    # Flag argument: show all files, even those matching ignore patterns
    parser.add_argument('--show-all',
                        action='store_true',
                        help="Show all files and directories, ignoring the ignore list.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Load ignore patterns from the specified ignore file (or use an empty list if `--show-all` is passed)
    ignore_patterns: List[str] = load_ignore_list(args.ignore_file) if not args.show_all else []

    # Start listing the directory structure from the specified path
    list_directory(args.path, ignore_patterns, args.show_all)
