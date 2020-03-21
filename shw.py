# run with: python3 shw.py <lang>

import argparse

parser = argparse.ArgumentParser(description="Shell cheat sheet. Look up that one-liner you always forget...")
parser.add_argument(dest="lang", metavar="lang", help="The language or program in which you'd like to spawn a shell. One-liners are available for bash, nano, perl, python, ruby, vim.", choices=["bash", "nano", "perl", "python", "ruby", "vim"])
args = parser.parse_args()


if(args.lang=="bash"):
	print("/bin/bash -i")

elif(args.lang=="perl"):
	print("perl -e 'exec \"/bin/bash\";'\nor\nexec \"/bin/bash\";")

elif(args.lang=="python"):
	print("python -c 'import pty; pty.spawn(\"/bin/bash\")'")

elif(args.lang=="ruby"):
	print("exec \"/bin/bash\"")

elif(args.lang=="nano"):
	print("^R ^X\nreset; sh 1>&0 2>&0")

elif(args.lang=="vim"):
	print(":!bash \nor\n:set shell=/bin/bash:shell")
