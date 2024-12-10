# Project Structure

```
LifeLog/
├─ .git
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ refs
│  │  └─ HEAD
│  ├─ objects
│  │  ├─ 03
│  │  ├─ 07
│  │  ├─ 08
│  │  ├─ 09
│  │  ├─ 10
│  │  ├─ 12
│  │  ├─ 18
│  │  ├─ 1d
│  │  ├─ 1f
│  │  ├─ 21
│  │  ├─ 26
│  │  ├─ 28
│  │  ├─ 29
│  │  ├─ 31
│  │  ├─ 33
│  │  ├─ 38
│  │  ├─ 3c
│  │  ├─ 3d
│  │  ├─ 45
│  │  ├─ 48
│  │  ├─ 4c
│  │  ├─ 54
│  │  ├─ 58
│  │  ├─ 5e
│  │  ├─ 63
│  │  ├─ 65
│  │  ├─ 66
│  │  ├─ 69
│  │  ├─ 6d
│  │  ├─ 6f
│  │  ├─ 71
│  │  ├─ 73
│  │  ├─ 7a
│  │  ├─ 7d
│  │  ├─ 7f
│  │  ├─ 81
│  │  ├─ 8d
│  │  ├─ 91
│  │  ├─ 97
│  │  ├─ 9b
│  │  ├─ 9f
│  │  ├─ a2
│  │  ├─ a6
│  │  ├─ ab
│  │  ├─ ac
│  │  ├─ b3
│  │  ├─ b4
│  │  ├─ b5
│  │  ├─ be
│  │  ├─ c0
│  │  ├─ c2
│  │  ├─ c9
│  │  ├─ ca
│  │  ├─ cb
│  │  ├─ cc
│  │  ├─ cd
│  │  ├─ ce
│  │  ├─ d1
│  │  ├─ d5
│  │  ├─ d7
│  │  ├─ d9
│  │  ├─ de
│  │  ├─ e0
│  │  ├─ e3
│  │  ├─ e6
│  │  ├─ ea
│  │  ├─ ee
│  │  ├─ f1
│  │  ├─ f2
│  │  ├─ f3
│  │  ├─ f8
│  │  ├─ fc
│  │  ├─ fd
│  │  ├─ info
│  │  └─ pack
│  ├─ refs
│  │  ├─ heads
│  │  ├─ remotes
│  │  └─ tags
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ config
│  ├─ description
│  ├─ index
│  └─ packed-refs
├─ .github
├─ .pytest_cache
│  ├─ v
│  │  └─ cache
│  ├─ .gitignore
│  ├─ CACHEDIR.TAG
│  └─ README.md
├─ __pycache__
│  ├─ app.cpython-311.pyc
│  ├─ database.cpython-311.pyc
│  └─ lifelog_all_merge.cpython-311.pyc
├─ docs
│  ├─ diagrams.md
│  ├─ diagrams_ja.md
│  ├─ specification.md
│  └─ specification_ja.md
├─ instance
│  └─ diary.db
├─ migrations
│  ├─ versions
│  │  └─ 612831183f49_initial_migration.py
│  ├─ README
│  ├─ env.py
│  └─ script.py.mako
├─ models
│  ├─ __pycache__
│  │  ├─ __init__.cpython-311.pyc
│  │  ├─ base.cpython-311.pyc
│  │  ├─ diary_item.cpython-311.pyc
│  │  ├─ entry.cpython-311.pyc
│  │  ├─ init_data.cpython-311.pyc
│  │  ├─ user.cpython-311.pyc
│  │  └─ user_manager.cpython-311.pyc
│  ├─ __init__.py
│  ├─ base.py
│  ├─ diary_item.py
│  ├─ entry.py
│  ├─ init_data.py
│  ├─ user.py
│  └─ user_manager.py
├─ static
│  ├─ admin.css
│  ├─ main.css
│  ├─ script.js
│  ├─ style.css
│  └─ user.css
├─ templates
│  ├─ admin.html
│  ├─ index.html
│  ├─ login.html
│  ├─ register.html
│  └─ settings.html
├─ tests
│  ├─ __pycache__
│  │  ├─ conftest.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_app.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_database.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_diary_item.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_entry.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_init_data.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_lifelog_all_merge.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_models.cpython-311-pytest-8.3.4.pyc
│  │  ├─ test_user.cpython-311-pytest-8.3.4.pyc
│  │  └─ test_user_manager.cpython-311-pytest-8.3.4.pyc
│  ├─ instance
│  │  ├─ custom.db
│  │  ├─ diary.db
│  │  └─ test.db
│  ├─ conftest.py
│  ├─ test_app.py
│  ├─ test_database.py
│  ├─ test_diary_item.py
│  ├─ test_entry.py
│  ├─ test_init_data.py
│  ├─ test_models.py
│  ├─ test_user.py
│  └─ test_user_manager.py
├─ .coverage
├─ .coveragerc
├─ .gitignore
├─ LICENSE
├─ README.md
├─ README_JA.md
├─ alembic.ini
├─ app.py
├─ create_data.py
├─ database.py
├─ lifelog_all_merge.py
├─ merged_result.md
├─ models.py
├─ package-lock.json
├─ package.json
├─ pytest.ini
├─ requirements-test.txt
├─ requirements.txt
├─ schema.sql
└─ ドキュメント更新プロンプト.txt
```

[* 'app.py']
```python
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, make_response
from flask_wtf.csrf import CSRFProtect, generate_csrf
import datetime
import re
import functools
import logging
from database import db, init_db, logger as db_logger
from models import User, Entry, DiaryItem, create_initial_data
from sqlalchemy import select, desc

# ロガーの設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('app')

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 本番環境では安全な値に変更してください
csrf = CSRFProtect(app)

# セキュリティヘッダーの設定
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    # 開発環境ではコメントアウト
    # response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    # CSRFトークンをCookieとして設定
    if '/api/' in request.path:
        response.set_cookie('csrf_token', generate_csrf())
    return response

# デバッグ用ミドルウェア
@app.before_request
def log_request_info():
    logger.debug('Headers: %s', dict(request.headers))
    logger.debug('Body: %s', request.get_data())

@app.after_request
def log_response_info(response):
    logger.debug('Response Status: %s', response.status)
    logger.debug('Response Headers: %s', dict(response.headers))
    return response

# データベース初期化
init_db(app)

MAX_LOGIN_ATTEMPTS = 3  # ログイン試行回数を3回に変更

# ログイン必須デコレータ
def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        logger.debug('Checking login requirement')
        logger.debug('Session: %s', dict(session))
        if 'user_id' not in session:
            logger.debug('User not logged in, returning 401')
            return jsonify({'error': 'ログインが必要です'}), 401
        return f(*args, **kwargs)
    return decorated_function

# 管理者必須デコレータ
def admin_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        logger.debug('Checking admin requirement')
        logger.debug('Session: %s', dict(session))
        if 'user_id' not in session or not session.get('is_admin'):
            logger.debug('User not admin, returning 403')
            return jsonify({'error': '管理者権限が必要です'}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    logger.debug('Accessing index page')
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    logger.debug('Accessing login page')
    return render_template('login.html')

@app.route('/settings', methods=['GET'])
@login_required
def settings():
    logger.debug('Accessing settings page')
    return render_template('settings.html')

@app.route('/admin', methods=['GET'])
@admin_required
def admin():
    logger.debug('Accessing admin page')
    return render_template('admin.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    logger.debug('Login attempt received')
    logger.debug('Request JSON: %s', request.json)
    
    userid = request.json.get('userid')
    password = request.json.get('password')
    
    logger.debug('Login attempt for user: %s', userid)
    
    if not userid or not password:
        logger.debug('Missing userid or password')
        return jsonify({'error': 'ユーザーIDとパスワードを入力してください'}), 400

    stmt = select(User).filter_by(userid=userid, is_visible=True)
    user = db.session.execute(stmt).scalar_one_or_none()

    if not user:
        logger.debug('User not found or not visible: %s', userid)
        return jsonify({'error': 'ユーザーIDまたはパスワードが正しくありません'}), 401

    if user.is_locked:
        logger.debug('Account locked: %s', userid)
        return jsonify({'error': 'アカウントがロックされています。管理者に連絡してください'}), 403

    if user.check_password(password):
        logger.debug('Login successful: %s', userid)
        # ログイン成功時の処理
        user.login_attempts = 0
        user.last_login_attempt = None
        db.session.commit()
        
        session['user_id'] = user.id
        session['is_admin'] = user.is_admin
        session['name'] = user.name
        session['userid'] = user.userid
        logger.debug('Session updated: %s', dict(session))
        return jsonify({'message': 'ログインしました'})
    else:
        logger.debug('Invalid password for user: %s', userid)
        # ログイン失敗時の処理
        user.login_attempts += 1
        user.last_login_attempt = datetime.datetime.now()
        if user.login_attempts >= MAX_LOGIN_ATTEMPTS:
            user.is_locked = True
            logger.debug('Account locked due to too many attempts: %s', userid)
        db.session.commit()
        
        attempts_left = MAX_LOGIN_ATTEMPTS - user.login_attempts
        if attempts_left > 0:
            return jsonify({'error': f'パスワードが正しくありません。あと{attempts_left}回間違えるとロックされます'}), 401
        else:
            return jsonify({'error': 'アカウントがロックされました。管理者に連絡してください'}), 403

@app.route('/api/logout', methods=['POST'])
def logout():
    logger.debug('Logout request received')
    logger.debug('Session before logout: %s', dict(session))
    session.clear()
    logger.debug('Session cleared')
    return jsonify({'message': 'ログアウトしました'})

@app.route('/api/user/settings', methods=['PUT'])
@login_required
def update_user_settings():
    logger.debug('Update user settings request received')
    logger.debug('Request JSON: %s', request.json)
    
    name = request.json.get('name')
    current_password = request.json.get('currentPassword')
    new_password = request.json.get('newPassword')
    
    stmt = select(User).filter_by(id=session['user_id'], is_visible=True)
    user = db.session.execute(stmt).scalar_one_or_none()
    
    if not user:
        logger.debug('User not found: %s', session['user_id'])
        return jsonify({'error': 'ユーザーが見つかりません'}), 404
    
    # パスワード変更がある場合
    if current_password and new_password:
        logger.debug('Password change requested')
        if not user.check_password(current_password):
            logger.debug('Current password verification failed')
            return jsonify({'error': '現在のパスワードが正しくありません'}), 400
            
        user.password = new_password  # TODO: パスワードのハッシュ化
        user.name = name
        logger.debug('Password and name updated')
    else:
        # 名前のみ更新
        user.name = name
        logger.debug('Name updated')
    
    db.session.commit()
    session['name'] = name
    logger.debug('Settings update successful')
    return jsonify({'message': '設定を更新しました'})

@app.route('/api/user/deactivate', methods=['POST'])
@login_required
def deactivate_account():
    logger.debug('Account deactivation request received')
    logger.debug('Request JSON: %s', request.json)
    
    password = request.json.get('password')
    if not password:
        logger.debug('Password not provided')
        return jsonify({'error': 'パスワードを入力してください'}), 400

    stmt = select(User).filter_by(id=session['user_id'], is_visible=True)
    user = db.session.execute(stmt).scalar_one_or_none()

    if not user:
        logger.debug('User not found: %s', session['user_id'])
        return jsonify({'error': 'ユーザーが見つかりません'}), 404

    if not user.check_password(password):
        logger.debug('Password verification failed')
        return jsonify({'error': 'パスワードが正しくありません'}), 400

    # 管理者は退会できない
    if user.is_admin:
        logger.debug('Admin account deactivation attempted')
        return jsonify({'error': '管理者アカウントは退会できません'}), 403

    # ユーザーを不可視に設定
    user.is_visible = False
    db.session.commit()
    session.clear()
    logger.debug('Account deactivated successfully')
    return jsonify({'message': '退会処理が完了しました'})

@app.route('/api/admin/users', methods=['GET'])
@admin_required
def get_users():
    logger.debug('Admin user list request received')
    stmt = select(User).filter(User.userid != session['userid']).order_by(User.userid)
    users = db.session.execute(stmt).scalars().all()
    
    user_list = [{
        'id': user.id,
        'userid': user.userid,
        'name': user.name,
        'is_admin': user.is_admin,
        'is_locked': user.is_locked,
        'is_visible': user.is_visible,
        'login_attempts': user.login_attempts,
        'last_login_attempt': user.last_login_attempt.isoformat() if user.last_login_attempt else None,
        'entries_count': db.session.query(Entry).filter_by(user_id=user.id).count()
    } for user in users]
    
    logger.debug('User list retrieved: %d users', len(user_list))
    return jsonify(user_list)

@app.route('/api/admin/users/<int:user_id>/unlock', methods=['POST'])
@admin_required
def unlock_user(user_id):
    logger.debug('Unlock user request received: %d', user_id)
    stmt = select(User).filter_by(id=user_id)
    user = db.session.execute(stmt).scalar_one_or_none()
    if not user:
        return jsonify({'error': 'ユーザーが見つかりません'}), 404
    
    user.is_locked = False
    user.login_attempts = 0
    user.last_login_attempt = None
    db.session.commit()
    logger.debug('User unlocked successfully')
    return jsonify({'message': 'アカウントのロックを解除しました'})

@app.route('/api/admin/users/<int:user_id>/toggle-admin', methods=['POST'])
@admin_required
def toggle_admin(user_id):
    logger.debug('Toggle admin status request received: %d', user_id)
    stmt = select(User).filter_by(id=user_id)
    user = db.session.execute(stmt).scalar_one_or_none()
    if not user:
        return jsonify({'error': 'ユーザーが見つかりません'}), 404
    
    user.is_admin = not user.is_admin
    db.session.commit()
    logger.debug('Admin status toggled: %s', user.is_admin)
    return jsonify({'message': '管理者権限を更新しました'})

@app.route('/api/admin/users/<int:user_id>/toggle-visibility', methods=['POST'])
@admin_required
def toggle_visibility(user_id):
    logger.debug('Toggle visibility request received: %d', user_id)
    stmt = select(User).filter_by(id=user_id)
    user = db.session.execute(stmt).scalar_one_or_none()
    if not user:
        return jsonify({'error': 'ユーザーが見つかりません'}), 404
    
    # 管理者は削除できない
    if user.is_admin:
        logger.debug('Attempted to toggle admin account visibility')
        return jsonify({'error': '管理者アカウントは削除できません'}), 403
        
    user.is_visible = not user.is_visible
    db.session.commit()
    
    action = '復元' if user.is_visible else '削除'
    logger.debug('Visibility toggled: %s -> %s', action, user.is_visible)
    return jsonify({'message': f'ユーザーを{action}しました'})

@app.route('/entries', methods=['GET'])
def get_entries():
    logger.debug('Get entries request received')
    if 'user_id' in session and session.get('is_admin'):
        logger.debug('Admin user requesting all entries')
        # 管理者は全ての投稿を表示（退会ユーザーの投稿も含む）
        stmt = select(Entry).join(User).order_by(
            desc(Entry.updated_at if Entry.updated_at is not None else Entry.created_at)
        )
    else:
        logger.debug('Regular user or non-logged-in user requesting entries')
        # 未ログインユーザーまたは一般ユーザーは可視状態のユーザーの投稿のみ表示
        stmt = select(Entry).join(User).filter(User.is_visible == True).order_by(
            desc(Entry.updated_at if Entry.updated_at is not None else Entry.created_at)
        )
    
    entries = db.session.execute(stmt).scalars().all()
    logger.debug('Retrieved %d entries', len(entries))

    entry_list = [{
        'id': entry.id,
        'title': entry.title,
        'content': entry.content,
        'notes': entry.notes,
        'items': [{
            'item_name': item.item_name,
            'item_content': item.item_content
        } for item in entry.items],
        'created_at': entry.created_at.isoformat() if entry.created_at else None,
        'updated_at': entry.updated_at.isoformat() if entry.updated_at else None,
        'author_name': entry.user.name,
        'author_userid': entry.user.userid,
        'is_visible': entry.user.is_visible,
        'user_id': entry.user_id,
        'can_edit': 'user_id' in session and (
            session.get('is_admin') or (entry.user_id == session['user_id'] and entry.user.is_visible)
        )
    } for entry in entries]

    return jsonify(entry_list)

@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    logger.debug('Add entry request received')
    logger.debug('Request JSON: %s', request.json)
    
    title = request.json.get('title')
    content = request.json.get('content')
    notes = request.json.get('notes', '')
    items = request.json.get('items', [])
    
    if not title:
        logger.debug('Title is empty')
        return jsonify({'error': 'タイトルが空です'}), 400
    if not content:
        logger.debug('Content is empty')
        return jsonify({'error': '内容が空です'}), 400
    
    user = db.session.get(User, session['user_id'])
    if not user or not user.is_visible:
        logger.debug('User account is invalid')
        return jsonify({'error': 'アカウントが無効です'}), 403

    try:
        # エントリーを作成
        entry = Entry(
            user_id=session['user_id'],
            title=title,
            content=content,
            notes=notes,
            created_at=datetime.datetime.now()
        )
        db.session.add(entry)
        db.session.flush()  # IDを生成するためにflush
        logger.debug('Entry created: %d', entry.id)

        # 活動項目を追加
        for item in items:
            diary_item = DiaryItem(
                entry_id=entry.id,
                item_name=item['item_name'],
                item_content=item['item_content'],
                created_at=datetime.datetime.now()
            )
            db.session.add(diary_item)
            logger.debug('Diary item added to entry %d', entry.id)

        db.session.commit()
        logger.debug('Entry creation successful')
        return jsonify({'message': '投稿が完了しました'})
    except Exception as e:
        logger.error('Error creating entry: %s', str(e))
        db.session.rollback()
        return jsonify({'error': '投稿に失敗しました'}), 500

@app.route('/entries/<int:entry_id>', methods=['PUT'])
@login_required
def update_entry(entry_id):
    logger.debug('Update entry request received: %d', entry_id)
    logger.debug('Request JSON: %s', request.json)
    
    stmt = select(Entry).join(User).filter(Entry.id == entry_id)
    entry = db.session.execute(stmt).scalar_one_or_none()
    
    if not entry:
        logger.debug('Entry not found: %d', entry_id)
        return jsonify({'error': '投稿が見つかりません'}), 404
    
    # 管理者以外の場合、退会済みユーザーは編集不可
    if not session.get('is_admin') and (
        entry.user_id != session['user_id'] or not entry.user.is_visible
    ):
        logger.debug('User does not have edit permission')
        return jsonify({'error': '編集権限がありません'}), 403

    title = request.json.get('title')
    content = request.json.get('content')
    notes = request.json.get('notes', '')
    items = request.json.get('items', [])
    
    if not title:
        logger.debug('Title is empty')
        return jsonify({'error': 'タイトルが空です'}), 400
    if not content:
        logger.debug('Content is empty')
        return jsonify({'error': '内容が空です'}), 400
    
    try:
        # エントリーを更新
        entry.title = title
        entry.content = content
        entry.notes = notes
        entry.updated_at = datetime.datetime.now()
        logger.debug('Entry updated: %d', entry_id)

        # 既存の活動項目を削除
        stmt = select(DiaryItem).filter_by(entry_id=entry.id)
        existing_items = db.session.execute(stmt).scalars().all()
        for item in existing_items:
            db.session.delete(item)
        logger.debug('Existing diary items deleted')

        # 新しい活動項目を追加
        for item in items:
            diary_item = DiaryItem(
                entry_id=entry.id,
                item_name=item['item_name'],
                item_content=item['item_content'],
                created_at=datetime.datetime.now()
            )
            db.session.add(diary_item)
        logger.debug('New diary items added')

        db.session.commit()
        logger.debug('Entry update successful')
        return jsonify({'message': '更新が完了しました'})
    except Exception as e:
        logger.error('Error updating entry: %s', str(e))
        db.session.rollback()
        return jsonify({'error': '更新に失敗しました'}), 500

@app.route('/entries/<int:entry_id>', methods=['DELETE'])
@login_required
def delete_entry(entry_id):
    logger.debug('Delete entry request received: %d', entry_id)
    stmt = select(Entry).join(User).filter(Entry.id == entry_id)
    entry = db.session.execute(stmt).scalar_one_or_none()
    
    if not entry:
        logger.debug('Entry not found: %d', entry_id)
        return jsonify({'error': '投稿が見つかりません'}), 404
    
    # 管理者以外の場合、退会済みユーザーは削除不可
    if not session.get('is_admin') and (
        entry.user_id != session['user_id'] or not entry.user.is_visible
    ):
        logger.debug('User does not have delete permission')
        return jsonify({'error': '削除権限がありません'}), 403

    try:
        db.session.delete(entry)
        db.session.commit()
        logger.debug('Entry deleted successfully')
        return jsonify({'message': '削除が完了しました'})
    except Exception as e:
        logger.error('Error deleting entry: %s', str(e))
        db.session.rollback()
        return jsonify({'error': '削除に失敗しました'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

```

[* 'models.py']
```python
from datetime import datetime
from sqlalchemy import Boolean, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from database import db

class Base(DeclarativeBase):
    pass

class User(db.Model, Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)  # ハッシュ化されたパスワード
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_locked: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    login_attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_login_attempt: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    # リレーションシップ
    entries: Mapped[list["Entry"]] = relationship("Entry", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.userid}>"

    def check_password(self, password: str) -> bool:
        # TODO: パスワードのハッシュ化比較を実装
        return self.password == password

class Entry(db.Model, Base):
    __tablename__ = 'entries'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=False, default='')
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    # リレーションシップ
    user: Mapped["User"] = relationship("User", back_populates="entries")
    items: Mapped[list["DiaryItem"]] = relationship("DiaryItem", back_populates="entry", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Entry {self.title}>"

class DiaryItem(db.Model, Base):
    __tablename__ = 'diary_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    entry_id: Mapped[int] = mapped_column(Integer, ForeignKey('entries.id'), nullable=False)
    item_name: Mapped[str] = mapped_column(String(100), nullable=False)
    item_content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    # リレーションシップ
    entry: Mapped["Entry"] = relationship("Entry", back_populates="items")

    def __repr__(self):
        return f"<DiaryItem {self.item_name}>"

# 初期データ作成用の関数
def create_initial_data():
    # 管理者ユーザーの作成
    admin = User(
        userid='admin',
        name='管理人',
        password='Admin3210',
        is_admin=True,
        created_at=datetime.now()
    )

    # テストユーザー1の作成
    tetsu = User(
        userid='tetsu',
        name='devilman',
        password='Tetsu3210',
        created_at=datetime.now()
    )

    # テストユーザー2の作成
    gento = User(
        userid='gento',
        name='gen chan',
        password='Gento3210',
        created_at=datetime.now()
    )

    db.session.add_all([admin, tetsu, gento])
    db.session.commit()

    # サンプル日記の作成
    admin_entry = Entry(
        user=admin,
        title='LifeLogの運営開始について',
        content='本日よりLifeLogの運営を開始しました。\n\n皆様に快適にご利用いただけるよう、以下のルールを設けさせていただきます：\n\n1. 他者への誹謗中傷は禁止\n2. 個人情報の投稿は控えめに\n3. 楽しく前向きな記録を心がけましょう\n\nご協力よろしくお願いいたします。',
        notes='天気：晴れ\n気分：わくわく',
        created_at=datetime.now()
    )

    tetsu_entry1 = Entry(
        user=tetsu,
        title='試合に向けて本格始動',
        content='今日から本格的なトレーニング期間に入る。\n\n朝一番でランニングから始めて、午後はジムでの練習。\n\n来月の試合までに必ず仕上げる！',
        notes='体重：75kg\n体調：絶好調\n気温：20℃',
        created_at=datetime.now()
    )

    # 活動項目の追加
    tetsu_items = [
        DiaryItem(
            entry=tetsu_entry1,
            item_name='筋トレ',
            item_content='スクワット 30回×3セット\nベンチプレス 80kg×10回×3セット\n腹筋 50回×3セット',
            created_at=datetime.now()
        ),
        DiaryItem(
            entry=tetsu_entry1,
            item_name='ランニング',
            item_content='朝：10km（50分）\n夜：5km（25分）',
            created_at=datetime.now()
        )
    ]

    db.session.add_all([admin_entry, tetsu_entry1] + tetsu_items)
    db.session.commit()

```

[* 'README.md']
```
# About LifeLog

A simple diary posting and management system with user authentication, featuring role-based access control for regular users and administrators.

## Important Notice
- This application is under development and may have security and performance issues.

## Version History
- 2024/12/01: Initial release 0.01
- 2024/12/08: Model structure improvements and test additions
- 2024/12/09: Migration functionality added
- 2024/12/10: Test coverage improvements, documentation updates, and environment setup changes

## Key Features

- User Management (Registration, Authentication, Access Control)
- Diary Entry Management (Create, Edit, Delete)
- Administrative Functions (User Management, Content Management)
- Simple and User-Friendly Interface

## Technology Stack

- Python 3.11
- Flask 3.1.0
- SQLAlchemy 2.0.36
- Flask-SQLAlchemy 3.1.1
- Alembic 1.14.0
- Flask-WTF 1.2.1
- SQLite3
- HTML/CSS/JavaScript

## Setup Instructions

1. Prepare Python Environment
```bash
# Install Miniconda (if not already installed)
# Download from: https://docs.conda.io/en/latest/miniconda.html

# Create conda environment
conda create -n lifelog python=3.11
conda activate lifelog
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Database Setup
```bash
# Run migrations
alembic upgrade head

# Create initial data
python -c "from models import create_initial_data; create_initial_data()"
```

4. Start Application
```bash
python app.py
```

After starting the application, access http://127.0.0.1:5000 in your browser.

## Running Tests

1. Install Test Dependencies
```bash
pip install -r requirements-test.txt
```

2. Run Tests
```bash
pytest
```

The tests cover the following areas:
- User Authentication and Registration (92% coverage)
- Diary Entry Creation, Editing, and Deletion (96% coverage)
- User Management (90%+ coverage)
- Access Control
- Database Operations

## Initial Accounts

Administrator Account:
- User ID: admin
- Password: Admin3210

Test Users:
- User ID: tetsu
- Password: Tetsu3210

- User ID: gento
- Password: Gento3210

## Current Limitations

The current development version has the following limitations:
- No file upload functionality
- No pagination support
- No password reset feature
- No account deletion reversal

## License
- [MIT License](LICENSE)

## Detailed Specifications

For detailed application specifications, please refer to the following documents:
- [Specification (English)](docs/specification.md)
- [Design Diagrams (English)](docs/diagrams.md)

## Project Structure

```
/
├── app.py              # Main Application
├── database.py         # Database Operations
├── models.py           # SQLAlchemy Model Definitions (Unified)
├── alembic.ini         # Migration Configuration
├── models/            # Model Definitions
│   ├── __init__.py    # Model Package Initialization
│   ├── base.py        # Base Class Definition
│   ├── user.py        # User Model
│   ├── entry.py       # Diary Entry Model
│   ├── diary_item.py  # Diary Item Model
│   ├── user_manager.py # User Management
│   └── init_data.py   # Initial Data Creation
├── static/            # Static Files
│   ├── style.css      # Common Styles
│   ├── admin.css      # Admin Panel Styles
│   ├── user.css       # User Settings Styles
│   ├── main.css       # Main Styles
│   └── script.js      # Client-side Scripts
├── templates/         # HTML Templates
│   ├── index.html     # Homepage
│   ├── login.html     # Login Page
│   ├── register.html  # Registration Page
│   ├── settings.html  # User Settings Page
│   └── admin.html     # Admin Panel
├── migrations/        # Migration Files
│   └── versions/      # Version-controlled Migrations
├── instance/          # Instance-specific Files
│   └── diary.db      # SQLite Database
├── tests/            # Test Files
│   ├── conftest.py   # Test Configuration
│   ├── test_user.py  # User Tests
│   ├── test_entry.py # Entry Tests
│   └── test_user_manager.py # User Manager Tests
└── docs/             # Documentation
    ├── specification.md     # Specifications (English)
    ├── specification_ja.md  # Specifications (Japanese)
    ├── diagrams.md         # Design Diagrams (English)
    └── diagrams_ja.md      # Design Diagrams (Japanese)

```

[* '..\..\Users\metral\AppData\Local\Temp\tmpk00i6pr_.txt']
```
PS C:\work2\DebugFileMerger> python main.py
PS C:\work2\DebugFileMerger> python main.py
Traceback (most recent call last):
  File "C:\work2\DebugFileMerger\main.py", line 186, in <module>
    main()
  File "C:\work2\DebugFileMerger\main.py", line 21, in main
    config.read('config.ini')
  File "C:\Users\metral\.pyenv\pyenv-win\versions\3.12.5\Lib\configparser.py", line 684, in read
    self._read(fp, filename)
  File "C:\Users\metral\.pyenv\pyenv-win\versions\3.12.5\Lib\configparser.py", line 999, in _read
    for lineno, line in enumerate(fp, start=1):
                        ^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'cp932' codec can't decode byte 0x81 in position 6: illegal multibyte sequence
PS C:\work2\DebugFileMerger> python main.py
PS C:\work2\DebugFileMerger> python main.py
```

