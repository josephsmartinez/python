#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
#https://docs.python.org/3.3/library/argparse.html#const
#https://docs.python.org/3.3/howto/argparse.html#id1
#
import argparse
from subcommands import *

DESCRIPTION="This is a simple example program from docs.python.org/3.3/howto/argparse"
EPILOG="Example: ./commandline.py hello 1"


def foo(args):
  print(args)

def bar(args):
  print(args)


def main():
  
  # the ArgumentParser object will hold all the information necessary to parse the command line 
  parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
  # allows for us to specify options that conflict with each other
  group = parser.add_mutually_exclusive_group()
  
  parser.add_argument(dest="echo", # by default, ArgumentParser objects use the dest value as the “name” of each object
                      help="echo the string you use here",
                      action="store", # this just stores the argument’s value. This is the default action
                      type=str)
  parser.add_argument("number",
                      help="int value choices",
                      metavar='num', # an alternative name can be specified with metavar
                      type=int,
                      choices=[0, 1, 2])
  parser.add_argument('-int', '--integers',
                      help='an integer for the accumulator',
                      metavar='N',
                      action="store",
                      type=int, 
                      nargs='+', # Just like '*', all command-line args present are gathered into a list. an error message will be generated if there wasn’t at least one command-line argument present
                      default=[1,2,3])
  parser.add_argument('--sum',
                      help='sum the integers (default: find the max)',
                      dest='accumulate', 
                      action='store_const', # stores the value specified by the const keyword argument
                      const=sum, 
                      default=max)
  # if the option is specified, assign the value True to args.verbose. Not specifying it implies False
  group.add_argument("-v", "--verbose",
                      help="increase output verbosity",
                      action="store_true", # store the values True and False respectively
                      default=False)
  group.add_argument("-q", "--quiet",
                      help="quiet is good...",
                      action="store_false",
                      default=False)
  # “count”, to count the number of occurrences of a specific optional arguments
  parser.add_argument("-c", "--count",
                      help="increase output verbosity",
                      action="count", # counts the number of times a keyword argument occurs
                      default=0)
  # the add_subparsers() method also supports title and description keyword arguments
  subparsers = parser.add_subparsers(title='subcommands',
                        description='valid subcommands',
                        help='additional help')

  parser_foo = subparsers.add_parser('foo')
  parser_foo.add_argument('-x', type=int, default=1)
  
  parser_bar = subparsers.add_parser('bar')
  parser_bar.add_argument('z')

  args = parser.parse_args()

  if args.count > 1:
    print("many count")

  if args.quiet:
    print("quiet turned on")
    print("{} {} {} {}".format(args.echo, args.number, args.verbose, args.quiet))
    exit(0)

  if args.verbose:
    print("verbosity turned on")
    print(args)
    exit(0)
              # args.accumulate -> sum() const value is set
  print(args, args.accumulate(args.integers))
  exit(0)
  

if __name__ == "__main__":
    main()
