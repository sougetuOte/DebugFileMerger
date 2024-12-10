import os
import logging
from pathlib import Path  # パス操作を簡単にするためのモジュール

# 無視するディレクトリのリスト
IGNORED_DIRS = {
    'venv',          # Python仮想環境
    '.git',          # Gitリポジトリ
    '.pytest_cache',  # Pytestのキャッシュ
    '__pycache__',   # Pythonのキャッシュ
    '.vscode',       # VSCodeの設定
    '.idea',         # PyCharmの設定
    'node_modules',  # Node.jsの依存関係
    '.env',          # 環境変数
    'build',         # ビルド成果物
    'dist',          # 配布用ファイル
    'coverage',      # カバレッジレポート
    '.coverage',     # カバレッジデータ
    '.mypy_cache',   # Mypyのキャッシュ
    '.tox',          # Toxの仮想環境
    'htmlcov',       # HTMLカバレッジレポート
}

def setup_logging():
    """
    ログ設定を初期化する関数
    
    ログの出力先やフォーマット、ログレベルなどを設定します。
    error.logファイルにログが記録されます。
    """
    logging.basicConfig(
        filename='error.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

def generate_dir_structure(project_dir: str, max_depth: int = 3) -> str:
    """
    プロジェクトディレクトリの構造をツリー形式のテキストで生成する関数
    
    Args:
        project_dir (str): プロジェクトのルートディレクトリパス
        max_depth (int): 表示する階層の深さ（デフォルト: 3）
    
    Returns:
        str: ディレクトリ構造を表すASCIIアート形式の文字列
    
    Example:
        project/
        ├─ src/
        │  ├─ main.py
        │  └─ utils.py
        └─ docs/
           └─ readme.md
    """
    project_path = Path(project_dir)
    lines = []  # ツリー構造の各行を格納するリスト

    def should_ignore(path: Path) -> bool:
        """指定されたパスが無視すべきディレクトリかどうかを判定"""
        return path.name in IGNORED_DIRS

    def recurse(path: Path, prefix: str = '', depth: int = 0):
        """
        ディレクトリを再帰的に探索してツリー構造を生成する内部関数
        
        Args:
            path: 現在のディレクトリパス
            prefix: 行の接頭辞（インデントやツリーライン）
            depth: 現在の階層の深さ
        """
        # 最大深さを超えたら探索を中止
        if depth > max_depth:
            return
        
        # ディレクトリ内のファイルとフォルダを取得（ソート済み）
        entries = []
        try:
            for entry in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name)):
                # 無視すべきディレクトリはスキップ
                if entry.is_dir() and should_ignore(entry):
                    continue
                entries.append(entry)
        except PermissionError:
            # アクセス権限がない場合はスキップ
            return
        
        # 各エントリ（ファイルやフォルダ）を処理
        for i, e in enumerate(entries):
            # 最後の要素かどうかで使用する接続記号を変える
            connector = '└─ ' if i == len(entries)-1 else '├─ '
            lines.append(prefix + connector + e.name)
            
            # ディレクトリの場合は再帰的に処理
            if e.is_dir():
                # 次の階層のprefixを設定（最後の要素かどうかで変える）
                new_prefix = prefix + ('   ' if i == len(entries)-1 else '│  ')
                recurse(e, new_prefix, depth+1)

    # ルートディレクトリ名を追加
    lines.append(project_path.name + '/')
    # ツリー構造の生成を開始
    recurse(project_path, '', 1)
    
    # 生成した行を改行で結合して返す
    return '\n'.join(lines)

def merge_files(project_dir: str, relative_paths: list, output_md: str, error_message: str = None, error_log1: str = None, error_log2: str = None, max_depth: int = 3) -> None:
    """
    指定されたファイルの内容をマークダウンファイルにマージする関数
    
    Args:
        project_dir (str): プロジェクトのルートディレクトリパス
        relative_paths (list): マージするファイルの相対パスのリスト
        output_md (str): 出力するマークダウンファイルの名前
        error_message (str): エラーメッセージ（オプション）
        error_log1 (str): エラーログ1（オプション）
        error_log2 (str): エラーログ2（オプション）
        max_depth (int): ディレクトリ構造の表示深さ（デフォルト: 3）
    
    Raises:
        FileNotFoundError: 指定されたファイルが見つからない場合
    """
    # プロジェクトディレクトリの絶対パスを取得
    project_dir = os.path.abspath(project_dir)
    
    # 入力ファイルの存在確認
    for rp in relative_paths:
        full_path = os.path.join(project_dir, rp)
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

    # プロジェクトのディレクトリ構造を生成
    tree_str = generate_dir_structure(project_dir, max_depth=max_depth)

    # マークダウンファイルの生成
    with open(os.path.join(project_dir, output_md), 'w', encoding='utf-8') as md:
        # プロジェクト構造を書き込み
        md.write("# Project Structure\n\n")
        md.write("```\n")
        md.write(tree_str)
        md.write("\n```\n\n")

        # エラーメッセージを最初に書き込む
        if error_message:
            md.write("* 'Error Message'\n```\n")
            md.write(error_message)
            md.write("\n```\n\n")

        # エラーログ1を書き込む
        if error_log1:
            md.write("* 'Error Log 1'\n```\n")
            md.write(error_log1)
            md.write("\n```\n\n")

        # エラーログ2を書き込む
        if error_log2:
            md.write("* 'Error Log 2'\n```\n")
            md.write(error_log2)
            md.write("\n```\n\n")

        # ファイルの内容を書き込み
        for rp in relative_paths:
            full_path = os.path.join(project_dir, rp)
            # ファイル拡張子に基づいて言語を判定
            ext = os.path.splitext(full_path)[1].lower()
            lang = ""
            if ext == '.py':
                lang = "python"
            elif ext == '.html':
                lang = "html"
            elif ext == '.js':
                lang = "javascript"
            elif ext == '.css':
                lang = "css"
            elif ext == '.json':
                lang = "json"
            # その他の拡張子は言語指定なし

            # ファイル名とコードブロックを書き込み
            md.write(f"* '{rp}'\n")
            md.write("```" + lang + "\n")
            # ファイルの内容を読み込んで書き込み
            with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            md.write(content)
            md.write("\n```\n\n")

    # 成功ログを記録
    logging.info(f"Merged files into {output_md}")
