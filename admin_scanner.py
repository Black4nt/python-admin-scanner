#!/usr/bin/python

__author__   = "Black4nt"
__version__  = "0.1"
__email__    = "black4nt(dot)id(at)gmail(dot)com"
__homepage__ = "https://search.black4nt.ga"
__github__   = "https://github.com/Black4nt/python-admin-scanner"
__license__  = "MIT"

BANNER = """\033[01;32m\
+----------------------------+
| python admin pages scanner |
+----------------------------+
| %s |
+,,,,,,,,,,,,,,,,,,,,,,,,,,,,+\033[0m
""" % __homepage__

import os
import sys
import time
import requests

if (sys.version_info[0] < 3):
	from urlparse import urlparse
else:
	from urllib.parse import urlparse

def get_new_url(url):
	if not url.startswith(("http://","https://")):
		url = "http://" + url
	parse = urlparse(url)
	url = parse.scheme + "://" + parse.netloc
	return url

def admin_scanner(target):
	print ("\n[*] Starting at %s\n" % time.strftime("%X"))
	sys.stdout.write("\r[~] Scanning admin page")
	sys.stdout.flush()
	found = False
	admin_pages = open("admin_pages.txt").readlines()
	while len(admin_pages) != 0:
		new_url = get_new_url(target) + "/" + admin_pages.pop(0).strip()
		response = requests.get(new_url)
		sys.stdout.write(".")
		sys.stdout.flush()
		if response.status_code == 200:
			print ("\n[*] Admin page found: " + response.url)
			found = True; break
	if not found:
		print ("\n[!] Admin page tidak ditemukan!")
	else:
		pass


def main():
	prog = sys.argv[0]
	print (BANNER)
	if len(sys.argv) != 2:
		print ("\n[!] Usage   : %s <target>" % prog)
		print ("[+] Example : %s http://www.example.com\n" % prog)
		sys.exit(1)
	else:
		try:
			admin_scanner(sys.argv[1])
		except Exception as msg:
			print ("\n[!] Error: %s" % msg)

		except KeyboardInterrupt as e:
			print ("\n[!] User stopped")

		finally:
			print ("\n[-] Shutting down at %s\n\n" % time.strftime("%X"))
		return;

if __name__ == "__main__":
	main()