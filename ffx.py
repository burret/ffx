from argparse import ArgumentParser, RawDescriptionHelpFormatter
from textwrap import dedent

import pyffx

DESCRIPTION = '''\
    Format-preserving, Feistel-based cryptography.
        $ echo 8005551212 | python %(prog)s -e mypassword 0123456789
        9441166894
        $ echo 9441166894 | python %(prog)s -d mypassword 0123456789
        8005551212
        $ echo '+😊qwerty🍦*' | python %(prog)s -e secret-squirrel '*+😊🍦abcdefghijklmnopqrstuvwxyz'
        rgmty🍦udpv
        $ echo 'rgmty🍦udpv' | python %(prog)s -d secret-squirrel '*+😊🍦abcdefghijklmnopqrstuvwxyz'
        +😊qwerty🍦*
        $
'''

parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description=dedent(DESCRIPTION))
verb_group = parser.add_mutually_exclusive_group(required=True)
verb_group.add_argument('-e', action='store_true', help='Encode.')
verb_group.add_argument('-d', action='store_true', help='Decode.')
parser.add_argument('key', help='Passphrase.')
parser.add_argument('alphabet', help='Symbol set.')
args = parser.parse_args()

key = bytearray(args.key, encoding='ascii', errors='strict')
input_ = input()
ffx = pyffx.String(key, alphabet=args.alphabet, length=len(input_))
process = ffx.encrypt if args.e else ffx.decrypt
output = process(input_)
print(output)
