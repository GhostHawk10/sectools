#!/usr/bin/env python3
from collections import defaultdict
import re
import sys

hosts = defaultdict(int)
attacks = defaultdict(int)

HOST_IP = 4
ATTACKER_IP = 2

def read_dump(df):
        dump = []
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

def display_dashboard():
        print(f"Attacker IP \t Count")
        for i in attacks.keys():
                print(f"{str(i)} \t {str(attacks[i])}")
        print("")
        print(f"Target \t\t Count")
        for j in hosts.keys():
                print(f"{str(j)} \t {str(hosts[j])}")

try:
        read_dump(sys.argv[1])
        display_dashboard()
except:
        print("File not found.")
        print("Usage: ./pingsweepdetect.py <filename.txt>")
