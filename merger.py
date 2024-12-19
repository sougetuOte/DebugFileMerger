import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def merge_files(output_file):
    """
    指定されたディレクトリ内のすべてのファイルを結合し、一つのファイルに出力する。
    """
    total_size = 0
    file_count = 0
    
    with open(output_file, 'wb') as outfile:
        for filename in os.listdir('.'):
            if os.path.isfile(filename) and filename != output_file:
                try:
                    filepath = os.path.join('.', filename)
                    filesize = os.path.getsize(filepath)
                    logging.info(f"Merging file: {filename}, size: {filesize} bytes")
                    with open(filepath, 'rb') as infile:
                        outfile.write(infile.read())
                    total_size += filesize
                    file_count += 1
                except Exception as e:
                    logging.error(f"Error merging file: {filename}, {e}")
                    continue
        outfile.write(f"\n\nMerged {file_count} files, total size: {total_size} bytes".encode('utf-8'))
    logging.info(f"Successfully merged {file_count} files into {output_file}, total size: {total_size} bytes")

if __name__ == "__main__":
    output_filename = "merged_file.txt"
    merge_files(output_filename)
