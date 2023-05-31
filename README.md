```markdown
# File Splitter and Merger

This command-line tool allows you to split large files into smaller parts and merge them back into a single file.

## Splitting Files

To split a file into smaller parts, use the following command:

```bash
python splitter.py -i inputfile.txt -s 1
```

- `-i` or `--input`: Specify the path to the input file.
- `-s` or `--part-size`: Specify the size of each part in gigabytes. For example, `-s 1` will split the file into 1GB parts.

The tool will split the input file into parts and save them with the naming convention `inputfile.txt.partX`.

## Merging Files

To merge multiple file parts into a single file, use the following command:

```bash
python merger.py -i part1.txt part2.txt part3.txt -o outputfile.txt
```

- `-i` or `--input`: Specify the paths to the input file parts. Provide the paths of all the parts to be merged.
- `-o` or `--output`: Specify the path to the output file.

The tool will merge the input file parts in the specified order and save the result as `outputfile.txt`.

> Note: Ensure that the file parts to be merged are in the correct order.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`
3. Split files: Use the `splitter.py` script as explained above.
4. Merge files: Use the `merger.py` script as explained above.
