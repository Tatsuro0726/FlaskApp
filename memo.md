### メモ

2020/05/11
- markdawnの参考
    - [Qiita Markdown記法 サンプル集](https://qiita.com/tbpgr/items/989c6badefff69377da7)
- pyenvインストール済み
    - myenv
- mysqlインストール済み
    - ユーザ、データベース作成済み(ユーザ名：flask, password: flask, database: flask)
- フォルダ構成の参考
    - https://github.com/hamano/explore-flask-ja/blob/master/configuration.md

2020/05/17
- login_user()の参考
    - ソース：https://flask-login.readthedocs.io/en/latest/_modules/flask_login/utils.html#login_user
    - ドキュメント：https://flask-login.readthedocs.io/en/latest/
    - Qiita：https://qiita.com/msrks/items/d9c327dd81749ec01d1d
    - ポイント：DBにis_active？(activeだけでもいいかも、そもそもいらない？）カラムを作成すること。⇒ UserMixin使えばいける
    - flask-sqlalchemyのqueryを使う。sqlalchemyと少し違うので注意
        - https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records
    - __init__でlogin_manager.login_view() = "<view>"を書けばそこにredirectされる。

2020/05/17
- FLASK_APP=""がよくわからない。run.pyを設定したが、ホストIPやPortが反映されない。要検討。
- Flask-migrateの使い方。Script版も記載されている。
    - https://flask-migrate.readthedocs.io/en/latest/