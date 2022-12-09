from flask import Flask, request, jsonify
import json
import os
#Flaskオブジェクトの生成
app = Flask(__name__)

# 定数（ファイル無し）
NO_FILE = "NoFile!!"

# ===================
# エンドポイント
# ===================
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE']) 
def free_path( path ) :
    # -----------------------------------
    # URLに相当するファイルパスを取得
    # -----------------------------------    
    filepath = get_file_path( path, request.method )

    # -----------------------------------
    # ファイル無し
    # -----------------------------------
    if filepath == NO_FILE:
        # 空のjsonオブジェクト返却
        return jsonify({})

    # -----------------------------------
    # ファイルあり
    # -----------------------------------
    else:
        # ファイルを読み込む
        with open(filepath, 'r', encoding='utf-8') as f:
            # ファイルの中身をjsonで返す
            json_str = json.load(f)
            return jsonify(json_str)


# ===================
# ファイルパス取得
# ===================
def get_file_path( path, method ):
    # カレントディレクトリ取得
    my_dir = os.path.dirname(os.path.abspath(__file__))

    # static/[path]/index_[method].json
    try_path = f"{my_dir}/static/{path}/index_{method}.json"
    if os.path.exists(try_path):
        return try_path

    # static/[path]_[method].json
    try_path = f"{my_dir}/static/{path}_{method}.json"
    if os.path.exists(try_path):
        return try_path

    # static/[path]/index.json
    try_path = f"{my_dir}/static/{path}/index.json"
    if os.path.exists(try_path):
        return try_path

    # static/[path].json
    try_path = f"{my_dir}/static/{path}.json"
    if os.path.exists(try_path):
        return try_path

    # ファイル無し
    return NO_FILE


#run.pyを実行する
if __name__ == "__main__":
    app.run(debug=True)