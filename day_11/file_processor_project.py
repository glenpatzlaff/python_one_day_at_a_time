import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("process.log"),
                        logging.StreamHandler()
                    ])

def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            data = infile.read()
            # Placeholder for data processing logic
            processed_data = data.upper()  # Example processing step
    except FileNotFoundError:
        logging.error(f"File not found: {input_filename}")
        return
    except IOError:
        logging.error(f"IO error occurred while processing {input_filename}")
        return
    else:
        try:
            with open(output_filename, 'w') as outfile:
                outfile.write(processed_data)
                logging.info(f"Processed data has been saved to {output_filename}")
        except IOError:
            logging.error(f"Could not write to {output_filename}")

process_file('sample_input.txt', 'output.txt')