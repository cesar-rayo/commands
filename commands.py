import argparse
import sys

def main(args):
    usage = "python3 commands.py <COMMAND> -a <value> -n <value> -r [-h]"
    parser = argparse.ArgumentParser(description='Script description', usage=usage)

    parser.add_argument(
        'command',
        help='Executes some command'
    )

    parser.add_argument(
        '-a', '--argument',
        metavar='<value>',
        help='First argument'
    )
    parser.add_argument(
        '-n', '--name',
        metavar='Some Name',
        help='Name used inside script'
    )
    parser.add_argument(
        '-r', '--run',
        action='store_true',
        help='Flag used to run extra instruction'
    )

    arguments = parser.parse_args(args)

    if arguments.command == 'some':
        print("running some command")
        if arguments.argument:
            response = some_function(arguments.argument)
            print("using '{}'".format(response))
        if arguments.run:
            extra_function(arguments)
    elif arguments.command == 'another':
        print("running another command")
        if arguments.name:
            response = some_function(arguments.name)
            print("using '{}'".format(response))
        if arguments.run:
            extra_function(arguments)
    else:
        sys.exit("Command {} does not exits".format(arguments.command))

def some_function(parameter):
    print("executing some function")
    return parameter

def extra_function(arguments):
    print("Running extra function with {}".format(arguments))

if __name__ == '__main__':
    main(sys.argv[1:])