# Draft Application

## 環境セットアップ

1. 仮想環境を作成し、アクティベートします（オプションですが推奨）。
    ```sh
    python -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    ```

2. 必要なパッケージをインストールします。
    ```sh
    pip install -r requirements.txt
    ```

3. アプリケーションを実行します。
    ```sh
    python app.py
    ```

4. ブラウザで以下のURLにアクセスします。
    ```
    http://127.0.0.1:5000/
    ```

## 使用方法

1. トップページで参加者名とドラフトメンバーを入力し、送信します。
2. 再度フォームに戻り、次のドラフトを行います。
3. すべてのドラフトが完了したら、結果ページ（`/results`）にアクセスし、結果を確認します。
