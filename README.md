# Illumio Take Home

## Assumptions made
1. Given that there are many protocols, my program only handles tcp, udp, and icmp, as given in the example lookup_table.csv. Further protocol codes can be added later.
2. The program only handles the default log format and only version 2.

## Steps to run
1. Install python3
2. run `python3 main.py`
3. The program will generate the two output files requested, they will be named `port_and_protocol_combinations.csv` and `tag_counts.csv`

 ## Notes
 1. This code only looks at the `dstport` and `protocol` columns in every line of `flow_logs.txt` (columns 7 and 8 respectively), the rest of the row is ignored.