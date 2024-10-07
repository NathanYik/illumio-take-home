import csv
from collections import defaultdict

def get_tag_mappings(file_name):
    tag_mappings = {}
    with open(file_name) as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tag_mappings[(row["dstport"], row["protocol"])] = row["tag"]
    return tag_mappings

def get_tag_counts_and_port_n_protocol_counts(file_name, protocol_number_mappings, tag_mappings):
    port_n_protocol_counts = defaultdict(int)
    tag_counts = defaultdict(int)
    with open(file_name) as file:
        for line in file:
            s = line.split()
            key = (s[6], protocol_number_mappings[s[7]])
            port_n_protocol_counts[key] += 1
            if key in tag_mappings:
                tag_counts[tag_mappings[key]] += 1
            else:
                tag_counts["Untagged"] += 1
    return [port_n_protocol_counts, tag_counts]

def write_tag_count_file(file_name, tag_counts):
    with open(file_name, 'w') as tag_count_file:
        writer = csv.writer(tag_count_file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])

def write_port_n_protocol_file(file_name, port_n_protocol_counts):
    with open(file_name, 'w') as port_n_protocol_file:
        writer = csv.writer(port_n_protocol_file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_n_protocol_counts.items():
            writer.writerow([port, protocol, count])


def main():
    protocol_number_mappings = {
        '1': 'icmp',
        '6': 'tcp',
        '17': 'udp'
    }
    tag_mappings = get_tag_mappings("lookup_table.csv")

    port_n_protocol_counts, tag_counts = get_tag_counts_and_port_n_protocol_counts("flow_logs.txt", protocol_number_mappings, tag_mappings)

    write_tag_count_file("tag_counts.csv", tag_counts)

    write_port_n_protocol_file("port_and_protocol_combinations.csv", port_n_protocol_counts)


if __name__ == "__main__":
    main()