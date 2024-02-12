# FileManipulator

## Overview
コマンドラインから簡単なファイル操作を行うことができるスクリプトです。コンピュータサイエンス学習サイト[recursion](https://recursionist.io/)のBackend_project1の課題として取り組みました。

## USAGE
input.txtの内容を入力するコマンドによって処理を行いoutput.txtに書き込みます。
| Method | description | USAGE |
| ------ | ------ | ----- |
| reverse | 文字列を逆にして書き込みます | ```python3 file_manipulator.py reverse input.txt output.txt```|
| copy | 文字列をそのまま書きこみます | ```python3 file_manipulator.py copy input.txt output.txt``` |
| duplicate-contents | 文字列をnum個複製して書き込みます | ```python3 file_manipulator.py duplicate-contents input.txt output.txt num``` |
| replace-string | 文字列内のneedleをすべてnew_stringに置き換えて書き込みます | ```python3 file_manipulator.py replace-string input.txt output.txt needle new_string``` |
