import os
import sys
import logging  # ログ記録用のモジュール
import configparser  # 設定ファイル読み込み用のモジュール
import tkinter as tk  # GUIを作成するための標準ライブラリ
from tkinter import filedialog, messagebox  # ファイル選択ダイアログとメッセージボックス用
from tkinter import ttk  # モダンなGUIウィジェット用
import traceback

# 基本カラースキーム
COLORS = {
    'main': '#E6F3FF',      # メインカラー（薄い青）
    'accent': '#4B89DC',    # アクセントカラー（中間の青）
    'emphasis': '#2C3E50',  # 強調カラー（濃い青）
    'warning': '#E74C3C',   # 警告カラー（赤）
    'success': '#27AE60',   # 成功カラー（緑）
    'hover_accent': '#357ABD',  # ホバー時のアクセントカラー
    'hover_warning': '#D62C1A',  # ホバー時の警告カラー
    'bg_light': '#F5F8FA',  # より薄い青（偶数行背景）
    'text_light': '#F8F9FA' # テキストエリア背景
}

def setup_tkdnd():
    """tkdndライブラリのセットアップ"""
    # 実行ファイルのディレクトリを取得
    if getattr(sys, 'frozen', False):
        # PyInstallerで作成された実行ファイルの場合
        base_path = sys._MEIPASS
    else:
        # 通常のPython実行の場合
        base_path = os.path.dirname(os.path.abspath(__file__))

    # tkdndのパスを環境変数に追加
    tkdnd_path = os.path.join(base_path, 'tkinterdnd2', 'tkdnd')
    if os.path.exists(tkdnd_path):
        os.environ['TKDND_LIBRARY'] = tkdnd_path

    # tkinterdnd2をインポート
    from tkinterdnd2 import DND_FILES, TkinterDnD
    return DND_FILES, TkinterDnD

# tkdndのセットアップ
DND_FILES, TkinterDnD = setup_tkdnd()

from merger import merge_files  # 自作のマージ機能モジュール

class FileListItem(ttk.Frame):
    """ファイルリストの各項目を表すクラス"""
    def __init__(self, parent, filepath, on_delete, is_odd=False):
        super().__init__(parent)
        self.filepath = filepath
        
        # 背景色を交互に変更
        if is_odd:
            self.configure(style='Odd.TFrame')
        else:
            self.configure(style='Even.TFrame')
        
        # ファイルパスを表示するラベル
        self.label = ttk.Label(self, text=filepath)
        self.label.pack(side='left', padx=(0, 5), fill='x', expand=True)
        # 削除ボタン
        self.delete_btn = ttk.Button(self, text="×", width=3, command=lambda: on_delete(self), style='Warning.TButton')
        self.delete_btn.pack(side='right')

class ScrollableFileList(ttk.Frame):
    """スクロール可能なファイルリストを表すクラス"""
    def __init__(self, parent, on_double_click):
        super().__init__(parent)
        # スクロールバーの作成
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side='right', fill='y')
        
        # キャンバスの作成
        self.canvas = tk.Canvas(self, yscrollcommand=self.scrollbar.set, bg=COLORS['main'])
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # スクロールバーとキャンバスの連動
        self.scrollbar.config(command=self.canvas.yview)
        
        # ファイルリストを配置するフレーム
        self.file_frame = ttk.Frame(self.canvas, style='Odd.TFrame')
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.file_frame, anchor='nw')
        
        # ファイルパスのリスト
        self.file_items = []
        
        # キャンバスのサイズ調整
        self.file_frame.bind('<Configure>', self._on_frame_configure)
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        
        # マウスホイールでのスクロール
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        
        # ダブルクリックイベント
        self.canvas.bind('<Double-Button-1>', lambda e: on_double_click())
        self.file_frame.bind('<Double-Button-1>', lambda e: on_double_click())

    def _on_frame_configure(self, event=None):
        """内部フレームのサイズが変更されたときにスクロール範囲を更新"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_canvas_configure(self, event):
        """キャンバスのサイズが変更されたときに内部フレームの幅を調整"""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def _on_mousewheel(self, event):
        """マウスホイールでスクロール"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    def add_file(self, filepath):
        """ファイルをリストに追加"""
        is_odd = len(self.file_items) % 2 == 1
        item = FileListItem(self.file_frame, filepath, self.remove_file, is_odd)
        item.pack(fill='x', padx=5, pady=2)
        self.file_items.append(item)

    def remove_file(self, item):
        """ファイルをリストから削除"""
        item.pack_forget()
        item.destroy()
        self.file_items.remove(item)
        # 背景色を再設定
        for i, item in enumerate(self.file_items):
            if i % 2 == 1:
                item.configure(style='Odd.TFrame')
            else:
                item.configure(style='Even.TFrame')

    def get_files(self):
        """現在のファイルパスのリストを取得"""
        return [item.filepath for item in self.file_items]

    def clear(self):
        """リストをクリア"""
        for item in self.file_items[:]:
            self.remove_file(item)

def setup_logging():
    """ロギングの設定"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),  # 標準出力へのハンドラ
            logging.FileHandler('debug_merger.log', encoding='utf-8')  # ファイルへのハンドラ
        ]
    )

def main():
    # ロギングの設定（エラーや重要な情報を記録するため）
    setup_logging()

    # ==========================================================
    # 設定ファイル（config.ini）の読み込み
    # ==========================================================
    # 設定のデフォルト値
    DEFAULT_CONFIG = {
        'output_filename': 'merged_result.md',
        'max_depth': '3',
        'skip_dirs': '.git,build,dist,__pycache__,node_modules,venv,.venv,.idea,.vscode',
        'skip_extensions': '.pyc,.pyo,.pyd,.so,.dll,.dylib,.exe,.obj,.o'
    }

    config = configparser.ConfigParser(defaults=DEFAULT_CONFIG)
    try:
        if os.path.isfile('config.ini'):
            # UTF-8エンコーディングを指定して設定ファイルを読み込み
            config.read('config.ini', encoding='utf-8')
        
        # 設定値の取得（エラーハンドリング付き）
        try:
            default_output = config.get('DEFAULT', 'output_filename', fallback=DEFAULT_CONFIG['output_filename'])
            max_depth = config.getint('DEFAULT', 'max_depth', fallback=int(DEFAULT_CONFIG['max_depth']))
        except (configparser.Error, ValueError) as e:
            logging.warning(f"設定値の読み込みエラー: {e}")
            default_output = DEFAULT_CONFIG['output_filename']
            max_depth = int(DEFAULT_CONFIG['max_depth'])
        
        # 除外設定の読み込み
        try:
            skip_dirs = [d.strip() for d in config.get('DEFAULT', 'skip_dirs', 
                        fallback=DEFAULT_CONFIG['skip_dirs']).split(',') if d.strip()]
            skip_extensions = [e.strip() for e in config.get('DEFAULT', 'skip_extensions', 
                            fallback=DEFAULT_CONFIG['skip_extensions']).split(',') if e.strip()]
        except configparser.Error as e:
            logging.warning(f"除外設定の読み込みエラー: {e}")
            skip_dirs = [d.strip() for d in DEFAULT_CONFIG['skip_dirs'].split(',') if d.strip()]
            skip_extensions = [e.strip() for e in DEFAULT_CONFIG['skip_extensions'].split(',') if e.strip()]
    except Exception as e:
        logging.error(f"設定ファイルの読み込みに失敗しました: {e}")
        # デフォルト値を使用
        default_output = DEFAULT_CONFIG['output_filename']
        max_depth = int(DEFAULT_CONFIG['max_depth'])
        skip_dirs = [d.strip() for d in DEFAULT_CONFIG['skip_dirs'].split(',') if d.strip()]
        skip_extensions = [e.strip() for e in DEFAULT_CONFIG['skip_extensions'].split(',') if e.strip()]

    # ==========================================================
    # メインウィンドウの設定
    # ==========================================================
    root = TkinterDnD.Tk()  # ドラッグ＆ドロップ対応のTkインターフェース
    root.title("Flask Debug File Merger")  # ウィンドウのタイトル
    root.geometry("800x600")  # ウィンドウサイズ（幅x高さ）

    # スタイルの設定
    style = ttk.Style()
    
    # フレームスタイル
    style.configure('Odd.TFrame', background=COLORS['main'])
    style.configure('Even.TFrame', background=COLORS['bg_light'])
    
    # ボタンスタイル
    style.configure('Accent.TButton', background=COLORS['accent'], foreground='white')
    style.configure('Warning.TButton', background=COLORS['warning'], foreground='white')
    style.map('Accent.TButton', background=[('active', COLORS['hover_accent'])])
    style.map('Warning.TButton', background=[('active', COLORS['hover_warning'])])
    
    # タブスタイル
    style.configure('TNotebook', background=COLORS['main'])
    style.configure('TNotebook.Tab', background=COLORS['bg_light'], foreground=COLORS['emphasis'])
    style.map('TNotebook.Tab', background=[('selected', COLORS['accent'])],
                               foreground=[('selected', 'white')])

    # ラベルスタイル
    style.configure('TLabel', foreground=COLORS['emphasis'])
    style.configure('Error.TLabel', foreground=COLORS['warning'])
    style.configure('Success.TLabel', foreground=COLORS['success'])

    # ==========================================================
    # プロジェクトディレクトリ選択部分の作成
    # ==========================================================
    frame_dir = ttk.Frame(root, style='Odd.TFrame')  # フレーム（コンテナ）の作成
    frame_dir.pack(fill='x', pady=5, padx=5)  # フレームの配置（x方向に伸縮可能）
    
    # ラベルとテキスト入力欄の配置
    ttk.Label(frame_dir, text="プロジェクトディレクトリ:").pack(side='left')
    project_dir_var = tk.StringVar()  # ディレクトリパスを保持する変数
    entry_dir = ttk.Entry(frame_dir, textvariable=project_dir_var, width=50)
    entry_dir.pack(side='left', padx=5)

    # ディレクトリ選択ダイアログを開く関数
    def browse_dir():
        d = filedialog.askdirectory()  # ディレクトリ選択ダイアログを表示
        if d:  # ディレクトリが選択された場合
            project_dir_var.set(d)  # 選択されたパスを入力欄にセット
    
    # 「Browse...」ボタンの配置
    ttk.Button(frame_dir, text="開く", command=browse_dir, style='Accent.TButton').pack(side='left')

    # ==========================================================
    # タブインターフェースの作成
    # ==========================================================
    notebook = ttk.Notebook(root)  # タブコンテナの作成
    notebook.pack(fill='both', expand=True, pady=5, padx=5)

    # ファイルリスト用タブの作成
    frame_files = ttk.Frame(notebook, style='Odd.TFrame')
    notebook.add(frame_files, text='Files')  # タブに「Files」ページを追加

    # ファイル追加ボタンの作成
    def add_files():
        """ファイル選択ダイアログを表示してファイルを追加"""
        project_dir = project_dir_var.get()
        if not project_dir:
            messagebox.showerror("Error", "先にプロジェクトの場所を選んでください")
            return
        
        files = filedialog.askopenfilenames()
        if files:
            for f in files:
                try:
                    relpath = os.path.relpath(f, project_dir)
                    file_list.add_file(relpath)
                except ValueError:
                    file_list.add_file(f)

    add_button = ttk.Button(frame_files, text="ファイルを追加", command=add_files, style='Accent.TButton')
    add_button.pack(anchor='w', padx=5, pady=5)

    # ドラッグ＆ドロップ領域の作成
    ttk.Label(frame_files, text="ここにファイルをドロップするか、ダブルクリックしてダイアログを開いてください").pack(anchor='w', padx=5)
    file_list = ScrollableFileList(frame_files, add_files)  # ダブルクリックでadd_files関数を呼び出す
    file_list.pack(fill='both', expand=True, padx=5)

    # エラーメッセージ用タブの作成
    frame_error = ttk.Frame(notebook, style='Odd.TFrame')
    notebook.add(frame_error, text='エラーメッセージ')  # タブに「Error Message」ページを追加

    # エラーメッセージ入力領域の作成
    ttk.Label(frame_error, text="報告要望やエラーメッセージ").pack(anchor='w', padx=5)
    error_text = tk.Text(frame_error, wrap=tk.WORD, height=20, bg=COLORS['text_light'], fg='black')  # テキスト入力欄
    error_text.pack(fill='both', expand=True, padx=5)

    # エラーログ1用タブの作成
    frame_error_log1 = ttk.Frame(notebook, style='Odd.TFrame')
    notebook.add(frame_error_log1, text='ログ 1')

    # エラーログ1入力領域の作成
    ttk.Label(frame_error_log1, text="エラーログをここに貼り付けてください").pack(anchor='w', padx=5)
    error_log1_text = tk.Text(frame_error_log1, wrap=tk.WORD, height=20, bg=COLORS['text_light'], fg='black')
    error_log1_text.pack(fill='both', expand=True, padx=5)

    # エラーログ2用タブの作成
    frame_error_log2 = ttk.Frame(notebook, style='Odd.TFrame')
    notebook.add(frame_error_log2, text='ログ 2')

    # エラーログ2入力領域の作成
    ttk.Label(frame_error_log2, text="エラーログをここに貼り付けてください").pack(anchor='w', padx=5)
    error_log2_text = tk.Text(frame_error_log2, wrap=tk.WORD, height=20, bg=COLORS['text_light'], fg='black')
    error_log2_text.pack(fill='both', expand=True, padx=5)

    # ==========================================================
    # ドラッグ＆ドロップの処理関数
    # ==========================================================
    def drop_enter(event):
        """ドラッグしたアイテムがウィンドウに入ってきた時の処理"""
        event.widget.focus_force()
        return event.action

    def drop(event):
        """アイテムがドロップされた時の処理"""
        # ドロップされたファイルのパスを取得（複数ファイルの場合は空白区切り）
        paths = root.splitlist(event.data)
        project_dir = project_dir_var.get()
        
        # プロジェクトディレクトリが設定されているか確認
        if not project_dir:
            messagebox.showerror("Error", "先にプロジェクトディレクトリを選択")
            return
        
        # 各ファイルをリストに追加
        for p in paths:
            try:
                # プロジェクトディレクトリからの相対パスを計算
                relp = os.path.relpath(p, project_dir)
                file_list.add_file(relp)
            except ValueError:
                # 相対パス計算に失敗した場合（異なるドライブなど）は絶対パスを使用
                file_list.add_file(p)

    # ドラッグ＆ドロップのイベントをバインド
    file_list.canvas.drop_target_register(DND_FILES)
    file_list.canvas.dnd_bind('<<DropEnter>>', drop_enter)
    file_list.canvas.dnd_bind('<<Drop>>', drop)

    # ==========================================================
    # ボタン類の作成と処理関数の定義
    # ==========================================================
    frame_buttons = ttk.Frame(root, style='Odd.TFrame')
    frame_buttons.pack(fill='x', pady=5, padx=5)

    def do_merge():
        """マージボタンが押された時の処理"""
        try:
            # プロジェクトディレクトリの確認
            project_dir = project_dir_var.get().strip()
            if not project_dir:
                messagebox.showerror("Error", "プロジェクトディレクトリがセットされていません")
                return

            # ファイルリストとエラーテキストの取得
            relative_paths = file_list.get_files()
            error_message = error_text.get('1.0', tk.END).strip()
            error_log1 = error_log1_text.get('1.0', tk.END).strip()
            error_log2 = error_log2_text.get('1.0', tk.END).strip()

            # マージ対象が存在するか確認
            if not relative_paths and not error_message and not error_log1 and not error_log2:
                messagebox.showerror("Error", "ファイルやメッセージがありません")
                return

            # 相対パスを絶対パスに変換
            absolute_paths = [os.path.join(project_dir, path) for path in relative_paths]
            merge_files(
                os.path.join(project_dir, default_output),
                absolute_paths,
                project_dir=project_dir,
                max_depth=max_depth,
                skip_dirs=skip_dirs,
                skip_extensions=skip_extensions,
                error_message=error_message,
                error_log1=error_log1,
                error_log2=error_log2
            )
            messagebox.showinfo("成功", f"Merged into {os.path.join(project_dir, default_output)}")
            logging.info("ファイルはプロジェクトディレクトリに保存されました")

        except Exception as e:
            # エラーが発生した場合はログに記録してユーザーに通知
            logging.error("マージ失敗", exc_info=True)
            messagebox.showerror("Error", f"Merge failed: {e}")

    def do_reset():
        """リセットボタンが押された時の処理"""
        project_dir_var.set("")  # プロジェクトディレクトリをクリア
        file_list.clear()  # ファイルリストをクリア
        error_text.delete('1.0', tk.END)  # エラーテキストをクリア
        error_log1_text.delete('1.0', tk.END)  # エラーログ1をクリア
        error_log2_text.delete('1.0', tk.END)  # エラーログ2をクリア

    # マージボタンとリセットボタンの配置
    ttk.Button(frame_buttons, text="Merge", command=do_merge, style='Accent.TButton').pack(side='left', padx=5)
    ttk.Button(frame_buttons, text="Reset", command=do_reset, style='Warning.TButton').pack(side='left', padx=5)

    # ==========================================================
    # ステータス表示部分の作成
    # ==========================================================
    status_var = tk.StringVar()
    status_label = ttk.Label(root, textvariable=status_var, anchor='w')
    status_label.pack(fill='x', side='bottom', padx=5, pady=5)

    # メインループの開始（GUIの表示を開始）
    root.mainloop()


# プログラムのエントリーポイント
if __name__ == "__main__":
    main()
