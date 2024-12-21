import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_file_tree(project_dir, max_depth=3, skip_dirs=None, skip_extensions=None, current_depth=1):
    """
    プロジェクトディレクトリのファイルツリーを生成する
    
    Args:
        project_dir: プロジェクトのルートディレクトリ
        max_depth: ツリーの最大深さ（デフォルト: 3）
        skip_dirs: 中身を表示しないディレクトリのリスト
        skip_extensions: 除外する拡張子のリスト
        current_depth: 現在の深さ（再帰用、初期値: 1）
    """
    if skip_dirs is None:
        skip_dirs = []
    if skip_extensions is None:
        skip_extensions = []
        
    if current_depth == 1:
        tree_lines = [
            "# Project Tree\n",
            f"Root: {os.path.abspath(project_dir)}\n"
        ]
    else:
        tree_lines = []
    
    def add_to_tree(directory, prefix="", depth=1):
        if depth > max_depth:
            return
        
        try:
            items = sorted(os.listdir(directory))
        except PermissionError:
            return
            
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            current_prefix = "└── " if is_last else "├── "
            next_prefix = "    " if is_last else "│   "
            
            full_path = os.path.join(directory, item)
            
            # 拡張子チェック
            _, ext = os.path.splitext(item)
            if ext in skip_extensions:
                continue
                
            if os.path.isdir(full_path):
                tree_lines.append(f"{prefix}{current_prefix}{item}/")
                # スキップするディレクトリでなければ中身を表示
                if item not in skip_dirs and depth < max_depth:
                    add_to_tree(full_path, prefix + next_prefix, depth + 1)
            else:
                tree_lines.append(f"{prefix}{current_prefix}{item}")
    
    add_to_tree(project_dir)
    return "\n".join(tree_lines)

def merge_files(output_file, file_paths, project_dir=None, max_depth=3, skip_dirs=None, skip_extensions=None,
               error_message=None, error_log1=None, error_log2=None):
    """
    指定されたファイルを結合し、一つのファイルに出力する。
    project_dirが指定された場合は、ファイルツリーも出力する。
    
    Args:
        output_file: 出力ファイルのパス
        file_paths: マージするファイルのパスのリスト
        project_dir: プロジェクトディレクトリ（ファイルツリー生成用）
        max_depth: ファイルツリーの最大深さ（デフォルト: 3）
        skip_dirs: 中身を表示しないディレクトリのリスト
        skip_extensions: 除外する拡張子のリスト
        error_message: エラーメッセージ（オプション）
        error_log1: エラーログ1（オプション）
        error_log2: エラーログ2（オプション）
    """
    total_size = 0
    file_count = 0
    
    with open(output_file, 'wb') as outfile:
        # プロジェクトのファイルツリーを出力
        if project_dir:
            tree = generate_file_tree(
                project_dir,
                max_depth=max_depth,
                skip_dirs=skip_dirs,
                skip_extensions=skip_extensions
            )
            outfile.write(tree.encode('utf-8'))
            outfile.write(b'\n')

        # エラーメッセージとログの出力
        if error_message:
            outfile.write(b"# Error Message\n")
            outfile.write(error_message.encode('utf-8'))
            outfile.write(b'\n\n')
        
        if error_log1:
            outfile.write(b"# Error Log 1\n")
            outfile.write(error_log1.encode('utf-8'))
            outfile.write(b'\n\n')
        
        if error_log2:
            outfile.write(b"# Error Log 2\n")
            outfile.write(error_log2.encode('utf-8'))
            outfile.write(b'\n\n')

        # マージされたファイルの内容を出力
        for filepath in file_paths:
            if os.path.isfile(filepath):
                try:
                    # config.iniは除外
                    if os.path.basename(filepath) == 'config.ini':
                        continue
                        
                    filesize = os.path.getsize(filepath)
                    filename = os.path.basename(filepath)
                    logging.info(f"Merging file: {filename}, size: {filesize} bytes")
                    with open(filepath, 'rb') as infile:
                        outfile.write(b"\n\n# File: " + filename.encode('utf-8') + b"\n")
                        outfile.write(infile.read())
                    total_size += filesize
                    file_count += 1
                except Exception as e:
                    logging.error(f"Error merging file: {filename}, {e}")
                    continue

        # サマリーの出力
        outfile.write(f"\n\n# Summary\nMerged {file_count} files, total size: {total_size} bytes".encode('utf-8'))
    logging.info(f"Successfully merged {file_count} files into {output_file}, total size: {total_size} bytes")

if __name__ == "__main__":
    output_filename = "merged_file.txt"
    # テスト用のファイルリスト
    test_files = ["main.py", "merger.py"]
    merge_files(output_filename, test_files)
