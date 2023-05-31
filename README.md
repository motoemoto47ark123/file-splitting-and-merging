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

## How to Run

1. Clone this repository: `git clone https://github.com/motoemoto47ark123/file-splitting-and-merging.git`
2. Navigate to the project directory: `file-splitting-and-merging`
3. Split files: Use the following command to split a file:

   ```bash
   python splitter.py -i inputfile.txt -s 1
   ```

   Replace `inputfile.txt` with the path to your input file, and modify the part size as needed.

4. Merge files: Use the following command to merge file parts:

   ```bash
   python merger.py -i part1.txt part2.txt part3.txt -o outputfile.txt
   ```

   Replace `part1.txt`, `part2.txt`, `part3.txt` with the paths to your input file parts, and specify the desired output file name with `-o` option.
