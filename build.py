import os
import shutil
import subprocess
import sys
import glob

def find_tkdnd_path():
    """tkdndライブラリのパスを探す"""
    # venvのsite-packagesディレクトリを取得
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        # venv環境の場合
        site_packages = os.path.join(sys.prefix, 'Lib', 'site-packages')
    else:
        # グローバル環境の場合
        site_packages = os.path.join(sys.prefix, 'Lib', 'site-packages')

    # tkinterdnd2のパスを構築
    tkdnd_path = os.path.join(site_packages, 'tkinterdnd2')
    if not os.path.exists(tkdnd_path):
        raise FileNotFoundError(f"tkinterdnd2 directory not found at {tkdnd_path}")
    
    # tkdndディレクトリを探す
    tkdnd_dll_dir = os.path.join(tkdnd_path, 'tkdnd')
    if not os.path.exists(tkdnd_dll_dir):
        raise FileNotFoundError(f"tkdnd directory not found at {tkdnd_dll_dir}")
    
    return tkdnd_path, tkdnd_dll_dir

def clean_build():
    """ビルド関連の一時ファイルやディレクトリを削除"""
    dirs_to_remove = ['build', 'dist', '__pycache__']
    files_to_remove = ['*.spec', '*.pyc']
    
    # ディレクトリの削除
    for d in dirs_to_remove:
        if os.path.exists(d):
            shutil.rmtree(d)
    
    # ファイルの削除
    for pattern in files_to_remove:
        for f in os.listdir('.'):
            if f.endswith(pattern[1:]):  # パターンから'*.'を除いて比較
                os.remove(f)

def build_exe():
    """実行可能ファイルのビルド"""
    # tkdndのパスを取得
    tkdnd_path, tkdnd_dll_dir = find_tkdnd_path()
    print(f"Found tkinterdnd2 at: {tkdnd_path}")
    print(f"Found tkdnd DLLs at: {tkdnd_dll_dir}")

    # データファイルの設定
    datas = [
        (tkdnd_dll_dir, 'tkinterdnd2/tkdnd'),  # tkdndライブラリ
        ('config.ini', '.'),  # 設定ファイル
    ]

    # PyInstallerのコマンドを構築
    cmd = [
        'pyinstaller',
        '--name=DebugFileMerger',
        '--onefile',  # 単一の実行可能ファイルを生成
        '--noconsole',  # コンソールウィンドウを表示しない
        '--clean',  # ビルド前にキャッシュをクリア
        '--hidden-import=tkinterdnd2',  # tkinterdnd2を明示的にインポート
        '--collect-all=tkinterdnd2',  # tkinterdnd2の全ファイルを収集
    ]

    # データファイルの追加
    for src, dst in datas:
        cmd.append(f'--add-data={src};{dst}')

    # メインスクリプトの追加
    cmd.append('main.py')
    
    # コマンドを実行
    print("Running PyInstaller with command:", ' '.join(cmd))
    subprocess.run(cmd, check=True)

    # 生成されたexeファイルの確認
    exe_path = os.path.join('dist', 'DebugFileMerger.exe')
    if os.path.exists(exe_path):
        print(f"\nExecutable successfully created at: {exe_path}")
        print(f"Size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
    else:
        raise FileNotFoundError("Executable file was not created")

def main():
    try:
        # ビルド前のクリーンアップ
        print("Cleaning up previous builds...")
        clean_build()
        
        # 実行可能ファイルのビルド
        print("Building executable...")
        build_exe()
        
        print("\nBuild completed successfully!")
        print("You can now distribute the executable from the 'dist' directory.")
    except Exception as e:
        print(f"\nError during build: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
