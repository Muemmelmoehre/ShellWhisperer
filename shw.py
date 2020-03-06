#!/usr/bin/python3 # for use on Kali or any other Linux machine
# for Windows or Mac, please run: python3 shw.py <lang>

import argparse

parser = argparse.ArgumentParser(description="Shell cheat sheet. Look up that one-liner you always forget...")
parser.add_argument(dest="lang", metavar="lang", help="The language in which you'd like to spawn a shell. One-liners are available for bash, perl, python, ruby.", choices=["bash", "perl", "python", "ruby"])
args = parser.parse_args()


if(args.lang=="bash"):
	print("/bbin/bash -i")

elif(args.lang=="perl"):
	print("perl -e 'exec \"/bin/bash\";'\nor\nexec \"/bin/bash\";")

elif(args.lang=="python"):
	print("python -c 'import pty; pty.spawn(\"/bin/bash\")'")

elif(args.lang=="ruby"):
	print("exec \"/bin/bash\"")