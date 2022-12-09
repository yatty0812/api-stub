# api-stub  
Flask製のAPIスタブです  

## APIスタブ仕様
staticフォルダ配下に配置した静的JSONを、APIレスポンスとして返してくれます  

URLのパスにリンクさせて、静的JSONを配置ください  

例）  
APIのURL：**/users/customers/10000001**  
　　　　　　　↓  
JSONパス：api-stub/app/static/**/users/customers/10000001.json**  

### 詳細仕様
APIスタブは、１つのURLに対して、以下４ファイルパターンを探索します  
①⇒④の順に探索を行い、最初に見つかったファイルをAPIレスポンスとして返します

① api-stub/static/<URLパス>/index_<HTTPリクエストメソッド>.json  
② api-stub/static/<URLパス>_<HTTPリクエストメソッド>.json  
③ api-stub/static/<URLパス>/index.json  
④ api-stub/static/<URLパス>.json    

※↑の　例）　はパターン④に該当します  
　仮に↑の例）をパターン①に該当させると、以下となります  
　JSONパス：api-stub/app/static/**login/member/authentication/index_POST.json**  
　（POSTリクエストだった場合のパスです）



## スタブ利用の前提  
ローカル環境に「Python」がインストールされていることを前提とします  
  
### （参考）Pythonインストールの仕方  
インストールの仕方は特に問いませんが、  
Chocolateyを使ったインストールが楽ですのでおすすめです  
  
- ChocolateyによるPythonインストール手順  
https://qiita.com/ns_k/items/bedaa80f4a5129e4eef4  


## ローカルセットアップ手順(１回だけ行えばOK)
- api-stubに移動
```
cd C:\xxxx\api-stub 
```

- 仮想環境作成
```
python -m venv .env
```

- 仮想環境アクティベート
```
[Power Shell]
.env/Scripts/Activate.ps1

[Shell]
.env/Scripts/activate
```

- 関連モジュールインストール
```
[Power Shell]
python -m pip install -r requirements.txt

※なんでかはわからないが、pip installがうまく動かない
　python -m pip install　なら大丈夫

[Shell]
pip install -r requirements.txt
```
結局のところ、やってるのはpip install Flaskとイコールです

## APIスタブ起動手順

- api-stubに移動
```
cd C:\xxxx\api-stub 
```

- 仮想環境アクティベート
```
[Power Shell]
.env/Scripts/Activate.ps1

[Shell]
.env/Scripts/activate
```

- アプリ起動
```
python run.py
```

以降　http://localhost:5000/　でスタブアクセスできます

