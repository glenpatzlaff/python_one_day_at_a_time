import csv

def read_csv_to_dict(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = {column: [] for column in reader.fieldnames}
        for row in reader:
            for column, value in row.items():
                data[column].append(value)
    return data

def write_dict_to_csv(data, file_path):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        for i in range(len(next(iter(data.values())))):  # Assuming non-empty columns
            row = {column: data[column][i] for column in data}
            writer.writerow(row)

# Example usage
data = read_csv_to_dict('input.csv')
# Perform some analysis or transformation on data
write_dict_to_csv(data, 'output.csv')
