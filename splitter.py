import argparse
import os

def split_file(input_file, part_size):
    print('Start...')
    try:
        file_size = os.path.getsize(input_file)
        size_gb = int(part_size)
        part_size_bytes = size_gb * 1024 * 1024 * 1024
        num_parts = file_size // part_size_bytes + (file_size % part_size_bytes > 0)
        file_dir, file_name = os.path.split(input_file)

        with open(input_file, 'rb') as f:
            part_number = 1
            bytes_written = 0

            while True:
                chunk = f.read(part_size_bytes)
                if not chunk:
                    break

                part_name = f"{file_name}.part{part_number}"
                output_path = os.path.join(file_dir, part_name)
                with open(output_path, 'wb') as part_file:
                    part_file.write(chunk)

                bytes_written += len(chunk)
                if bytes_written >= part_size_bytes:
                    part_number += 1
                    bytes_written = 0

                print(f"Splitting... Part {part_number}/{num_parts}")

        print('Done. File split into parts.')
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Splits a file into multiple parts')
    parser.add_argument('-i', '--input', required=True, help='Input file')
    parser.add_argument('-s', '--part-size', required=True, help='Size of each part in gigabytes')
    args = parser.parse_args()

    split_file(args.input, args.part_size)
