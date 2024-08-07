# 数当てゲーム

数当てゲームへようこそ！このゲームは、プレイヤーが1から100の間でランダムに選ばれた数を当てるシンプルなPythonゲームです。

## ファイル構成

NumberGuessingGame/
├── main.py
├── game_logic.py
├── user_input.py
└── number_generator.py


## ファイルの説明

- **main.py**: プログラムのエントリーポイントです。`play_game`関数を呼び出してゲームを開始します。
- **game_logic.py**: ゲームのメインロジックが含まれています。`generate_number`関数を使ってランダムな数を生成し、`get_user_input`関数を使ってユーザーからの入力を受け取ります。
- **user_input.py**: ユーザーからの入力を処理します。入力が有効な数であることを確認し、無効な入力があった場合は再度入力を求めます。
- **number_generator.py**: ランダムな数を生成します。`random.randint`関数を使って1から100の間の数を返します。

## 実行方法

数当てゲームを実行するには、以下の手順に従ってください。

1. システムにPythonがインストールされていることを確認します。[こちら](https://www.python.org/downloads/)からダウンロードできます。
2. NumberGuessingGameプロジェクトをローカルマシンにクローンまたはダウンロードします。
3. ターミナルまたはコマンドプロンプトでプロジェクトディレクトリに移動します。
4. 以下のコマンドを実行してゲームを開始します。

   ```bash
   python main.py

##ゲームの説明
ゲームを実行すると、1から100の間の数を予想するように求められます。各予想の後、予想が低すぎるか高すぎるか、または正解かをゲームが教えてくれます。正解の数を見つけるまで予想を続けてください。ゲームは試行回数も記録します。

##例
数当てゲームへようこそ！
1から100の間の数を当ててください。
あなたの予想: 50
もっと大きい数です。
あなたの予想: 75
もっと小さい数です。
あなたの予想: 62
おめでとうございます！正解は 62 でした。
3 回の試行で当てました。


