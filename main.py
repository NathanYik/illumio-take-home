import csv
from collections import defaultdict

def main():
    protocol_number_mappings = {
        '6': 'tcp',
        '17': 'udp'
    }
    tag_mappings = {}
    with open('lookup_table.csv') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            tag_mappings[(row["dstport"], row["protocol"])] = row["tag"]

    with open('flow_logs.txt') as file:
        port_n_protocol_counts = defaultdict(int)
        tag_counts = defaultdict(int)
        for line in file:
            s = line.split()
            key = (s[6], protocol_number_mappings[s[7]])
            port_n_protocol_counts[key] += 1
            if key in tag_mappings:
                tag_counts[tag_mappings[key]] += 1
            else:
                tag_counts["Untagged"] += 1


        with open('tag_counts.csv', 'w') as tag_count_file:
            writer = csv.writer(tag_count_file)
            writer.writerow(['Tag', 'Count'])
            for tag, count in tag_counts.items():
                writer.writerow([tag, count])


        with open('port_and_protocol_combinations.csv', 'w') as port_n_protocol_file:
            writer = csv.writer(port_n_protocol_file)
            writer.writerow(['Port', 'Protocol', 'Count'])
            for (port, protocol), count in port_n_protocol_counts.items():
                writer.writerow([port, protocol, count])


if __name__ == "__main__":
    main()