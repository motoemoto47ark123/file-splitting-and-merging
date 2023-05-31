import argparse
import os

def merge_files(input_parts, output_file):
    print('Start...')
    try:
        with open(output_file, 'wb') as output:
            for part in input_parts:
                with open(part, 'rb') as file:
                    output.write(file.read())
                print(f"Merging... {part}")

        print(f"Done. File saved in {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merges multiple file parts into a single file')
    parser.add_argument('-i', '--input', nargs='+', required=True, help='Input file parts')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    args = parser.parse_args()

    merge_files(args.input, args.output)
