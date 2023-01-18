#!/usr/bin/env python3
from collections import defaultdict
import re
import sys
import time
from curses import wrapper

hosts = defaultdict(int)
attacks = defaultdict(int)

HOST_IP = 4
ATTACKER_IP = 2

def read_dump(df):
	dump = []
	hosts.clear()
	attacks.clear()

	with open(df, 'r') as f:
		lines = f.readlines()
		for i in range(len(lines)):
			dump.append(lines[i])

	get_incoming(dump)

def get_incoming(pings):
	for ping in range(len(pings)):
		match = re.search("ICMP echo request", pings[ping])
		if match:
			l = pings[ping].split(" ")
			hosts[l[HOST_IP][:-1]] += 1
			attacks[l[ATTACKER_IP]] += 1

def display_dashboard(screen):
	screen.clear()
	screen.addstr(0, 0, "Attacker IP \t Count")

	for i in range(len(attacks)):
		ip = str(list(attacks.keys())[i])
		counter = str(list(attacks.values())[i])
		screen.addstr(1+i, 0, f"{ip} \t {counter}")

	screen.addstr(len(attacks) + 4, 0, f"Target \t\t Count")

	for j in range(len(hosts)):
		ip = str(list(hosts.keys())[j])
		counter = str(list(hosts.values())[j])
		screen.addstr((len(attacks)+5)+j, 0, f"{ip} \t {counter}")

	screen.refresh()

def continue_read(df, screen):
	while True:
		read_dump(df)
		display_dashboard(screen)
		time.sleep(10)

def main(screen):
	try:
		continue_read(sys.argv[1], screen)
	except Exception as err:
		print(err)
		print("Usage: ./pingsweepdetect.py <filename.txt>")

if __name__ == "__main__":
        wrapper(main)
