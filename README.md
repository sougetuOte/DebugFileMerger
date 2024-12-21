# Debug File Merger

デバッグファイルのマージツール

## 目次

- [Debug File Merger](#debug-file-merger)
  - [目次](#目次)
  - [概要](#概要)
  - [機能](#機能)
  - [必要要件](#必要要件)
  - [インストール手順](#インストール手順)
    - [Windows](#windows)
    - [Ubuntu](#ubuntu)
  - [使用方法](#使用方法)
  - [ライセンス](#ライセンス)

## 概要

このツールは、デバッグファイルをマージするためのユーティリティです。

## 機能

- デバッグファイルの自動マージ
- 設定ファイルによる柔軟なカスタマイズ
- 複数のファイル形式のサポート
- タイムスタンプ付きの出力ファイル（時系列管理）

## 必要要件

- Python 3.8以上
- pip（Pythonパッケージマネージャー）

## インストール手順

### Windows

1. Pythonのインストール
   ```cmd
   # Pythonの公式サイトからインストーラーをダウンロード
   https://www.python.org/downloads/

   # インストール時に「Add Python to PATH」にチェックを入れる
   ```

2. pyenvのインストール（オプション）
   ```cmd
   # PowerShellを管理者として実行
   pip install pyenv-win
   ```

3. 仮想環境の作成とアクティベート
   ```cmd
   # プロジェクトディレクトリで実行
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. 依存パッケージのインストール
   ```cmd
   pip install -r requirements.txt
   ```

### Ubuntu

1. Pythonのインストール
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. pyenvのインストール（オプション）
   ```bash
   # 必要なパッケージのインストール
   sudo apt install -y make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
   libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
   liblzma-dev python-openssl git

   # pyenvのインストール
   curl https://pyenv.run | bash

   # .bashrcに以下を追加
   echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. 仮想環境の作成とアクティベート
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. 依存パッケージのインストール
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 設定ファイルの準備
   - 用意されているものを使っても良いが、必要に応じて新たに作成することもできる
   ```ini
   # config.iniを編集して必要な設定を行う
   [settings]
   input_dir = ./input
   output_dir = ./output
   ```

2. プログラムの実行
   ```bash
   # 新しいプロジェクトを開始する場合
   python main.py /path/to/project

   # 前回のプロジェクトを継続する場合
   python main.py
   ```

   プログラムは自動的に前回開いたプロジェクトディレクトリを記憶し、次回起動時にそのディレクトリを開きます。
   この設定は`config.ini`の`[Session]`セクションで管理されます。

   マージ結果は`merged_file_yyyymmddhhmmss.txt`の形式で保存されます。
   例：`merged_file_20240101123456.txt`
   
   タイムスタンプ付きのファイル名により、マージ結果を時系列で管理でき、
   過去の結果との比較や履歴の追跡が容易になります。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。
