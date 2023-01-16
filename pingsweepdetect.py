#!/usr/bin/env python3
from collections import defaultdict
import re

hosts = defaultdict(int)
attacks = defaultdict(int)

def read_dump(df):
	dump = []
	with open(df, 'r') as f:
		lines = f.readlines()
		for i in range(len(lines)):
			dump.append(lines[i])

	analyze_pings(dump)

def get_incoming(pings):
	for ping in range(len(pings)):
		match = re.search("ICMP echo request", pings[ping])
		if match:
			l = pings[ping].split(" ")
			hosts[l[4][:-1]] += 1
			attacks[l[2]] += 1


def analyze_pings(pings):
	get_incoming(pings)
		#0 = timestamp
		#2 = source
		#4 = destination

def display_dashboard():
	print("Attacker IP" + "\t" + "Count")
	for i in attacks.keys():
		print(str(i) + "\t" + str(attacks[i]))
	print("")
	print("Target" + "\t\t" + "Count")
	for j in hosts.keys():
		print(str(j) + "\t" + str(hosts[j]))

read_dump('dump.txt')
display_dashboard()
