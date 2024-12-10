import os
import logging  # ログ記録用のモジュール
import configparser  # 設定ファイル読み込み用のモジュール
import tkinter as tk  # GUIを作成するための標準ライブラリ
from tkinter import filedialog, messagebox  # ファイル選択ダイアログとメッセージボックス用
from tkinter import ttk  # モダンなGUIウィジェット用
from tkinterdnd2 import DND_FILES, TkinterDnD  # ドラッグ＆ドロップ機能を提供
import traceback
from merger import merge_files, setup_logging  # 自作のマージ機能モジュール

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
        self.delete_btn = ttk.Button(self, text="×", width=3, command=lambda: on_delete(self))
        self.delete_btn.pack(side='right')

class ScrollableFileList(ttk.Frame):
    """スクロール可能なファイルリストを表すクラス"""
    def __init__(self, parent, on_double_click):
        super().__init__(parent)
        # スクロールバーの作成
        self.scrollbar = ttk.Scrollbar(self)
        self.scrollbar.pack(side='right', fill='y')
        
        # キャンバスの作成
        self.canvas = tk.Canvas(self, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side='left', fill='both', expand=True)
        
        # スクロールバーとキャンバスの連動
        self.scrollbar.config(command=self.canvas.yview)
        
        # ファイルリストを配置するフレーム
        self.file_frame = ttk.Frame(self.canvas)
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

def main():
    # ロギングの設定（エラーや重要な情報を記録するため）
    setup_logging()

    # ==========================================================
    # 設定ファイル（config.ini）の読み込み
    # ==========================================================
    config = configparser.ConfigParser()
    if os.path.isfile('config.ini'):
        # UTF-8エンコーディングを指定して設定ファイルを読み込み
        config.read('config.ini', encoding='utf-8')
    # デフォルト値の設定（設定ファイルが無い場合や設定が見つからない場合に使用）
    default_output = config['DEFAULT'].get('output_filename', 'merged_result.md')
    max_depth = config['DEFAULT'].getint('max_depth', 3)

    # ==========================================================
    # メインウィンドウの設定
    # ==========================================================
    root = TkinterDnD.Tk()  # ドラッグ＆ドロップ対応のTkインターフェース
    root.title("Flask Debug File Merger")  # ウィンドウのタイトル
    root.geometry("800x600")  # ウィンドウサイズ（幅x高さ）

    # スタイルの設定
    style = ttk.Style()
    style.configure('Odd.TFrame', background='#f0f0f0')
    style.configure('Even.TFrame', background='white')

    # ==========================================================
    # プロジェクトディレクトリ選択部分の作成
    # ==========================================================
    frame_dir = ttk.Frame(root)  # フレーム（コンテナ）の作成
    frame_dir.pack(fill='x', pady=5, padx=5)  # フレームの配置（x方向に伸縮可能）
    
    # ラベルとテキスト入力欄の配置
    ttk.Label(frame_dir, text="Project Directory:").pack(side='left')
    project_dir_var = tk.StringVar()  # ディレクトリパスを保持する変数
    entry_dir = ttk.Entry(frame_dir, textvariable=project_dir_var, width=50)
    entry_dir.pack(side='left', padx=5)

    # ディレクトリ選択ダイアログを開く関数
    def browse_dir():
        d = filedialog.askdirectory()  # ディレクトリ選択ダイアログを表示
        if d:  # ディレクトリが選択された場合
            project_dir_var.set(d)  # 選択されたパスを入力欄にセット
    
    # 「Browse...」ボタンの配置
    ttk.Button(frame_dir, text="Browse...", command=browse_dir).pack(side='left')

    # ==========================================================
    # タブインターフェースの作成
    # ==========================================================
    notebook = ttk.Notebook(root)  # タブコンテナの作成
    notebook.pack(fill='both', expand=True, pady=5, padx=5)

    # ファイルリスト用タブの作成
    frame_files = ttk.Frame(notebook)
    notebook.add(frame_files, text='Files')  # タブに「Files」ページを追加

    # ファイル追加ボタンの作成
    def add_files():
        """ファイル選択ダイアログを表示してファイルを追加"""
        project_dir = project_dir_var.get()
        if not project_dir:
            messagebox.showerror("Error", "Please set the Project Directory first.")
            return
        
        files = filedialog.askopenfilenames()
        if files:
            for f in files:
                try:
                    relpath = os.path.relpath(f, project_dir)
                    file_list.add_file(relpath)
                except ValueError:
                    file_list.add_file(f)

    add_button = ttk.Button(frame_files, text="Add Files...", command=add_files)
    add_button.pack(anchor='w', padx=5, pady=5)

    # ドラッグ＆ドロップ領域の作成
    ttk.Label(frame_files, text="Drop files here or double-click to add:").pack(anchor='w', padx=5)
    file_list = ScrollableFileList(frame_files, add_files)  # ダブルクリックでadd_files関数を呼び出す
    file_list.pack(fill='both', expand=True, padx=5)

    # エラーメッセージ用タブの作成
    frame_error = ttk.Frame(notebook)
    notebook.add(frame_error, text='Error Message')  # タブに「Error Message」ページを追加

    # エラーメッセージ入力領域の作成
    ttk.Label(frame_error, text="Paste error message here:").pack(anchor='w', padx=5)
    error_text = tk.Text(frame_error, wrap=tk.WORD, height=20)  # テキスト入力欄
    error_text.pack(fill='both', expand=True, padx=5)

    # エラーログ1用タブの作成
    frame_error_log1 = ttk.Frame(notebook)
    notebook.add(frame_error_log1, text='Error Log 1')

    # エラーログ1入力領域の作成
    ttk.Label(frame_error_log1, text="Paste error log 1 here:").pack(anchor='w', padx=5)
    error_log1_text = tk.Text(frame_error_log1, wrap=tk.WORD, height=20)
    error_log1_text.pack(fill='both', expand=True, padx=5)

    # エラーログ2用タブの作成
    frame_error_log2 = ttk.Frame(notebook)
    notebook.add(frame_error_log2, text='Error Log 2')

    # エラーログ2入力領域の作成
    ttk.Label(frame_error_log2, text="Paste error log 2 here:").pack(anchor='w', padx=5)
    error_log2_text = tk.Text(frame_error_log2, wrap=tk.WORD, height=20)
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
            messagebox.showerror("Error", "Please set the Project Directory first.")
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
    frame_buttons = ttk.Frame(root)
    frame_buttons.pack(fill='x', pady=5, padx=5)

    def do_merge():
        """マージボタンが押された時の処理"""
        try:
            # プロジェクトディレクトリの確認
            project_dir = project_dir_var.get().strip()
            if not project_dir:
                messagebox.showerror("Error", "Project directory is not set.")
                return

            # ファイルリストとエラーテキストの取得
            relative_paths = file_list.get_files()
            error_message = error_text.get('1.0', tk.END).strip()
            error_log1 = error_log1_text.get('1.0', tk.END).strip()
            error_log2 = error_log2_text.get('1.0', tk.END).strip()

            # マージ対象が存在するか確認
            if not relative_paths and not error_message and not error_log1 and not error_log2:
                messagebox.showerror("Error", "No files or error messages to merge.")
                return

            # マージ処理の実行
            output_md = default_output
            merge_files(
                project_dir,
                relative_paths,
                output_md,
                error_message=error_message,
                error_log1=error_log1,
                error_log2=error_log2,
                max_depth=max_depth
            )
            messagebox.showinfo("Success", f"Merged into {os.path.join(project_dir, output_md)}")
            logging.info("Merge completed successfully.")

        except Exception as e:
            # エラーが発生した場合はログに記録してユーザーに通知
            logging.error("Merge failed", exc_info=True)
            messagebox.showerror("Error", f"Merge failed: {e}")

    def do_reset():
        """リセットボタンが押された時の処理"""
        project_dir_var.set("")  # プロジェクトディレクトリをクリア
        file_list.clear()  # ファイルリストをクリア
        error_text.delete('1.0', tk.END)  # エラーテキストをクリア
        error_log1_text.delete('1.0', tk.END)  # エラーログ1をクリア
        error_log2_text.delete('1.0', tk.END)  # エラーログ2をクリア

    # マージボタンとリセットボタンの配置
    ttk.Button(frame_buttons, text="Merge", command=do_merge).pack(side='left', padx=5)
    ttk.Button(frame_buttons, text="Reset", command=do_reset).pack(side='left', padx=5)

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
