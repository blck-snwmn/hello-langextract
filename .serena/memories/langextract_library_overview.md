# Google LangExtract Library Overview

## 概要
LangExtractは、Googleが開発したオープンソースのPythonライブラリで、LLM（大規模言語モデル）を使用して非構造化テキストから構造化情報を抽出することを目的としています。

**GitHubリポジトリ**: https://github.com/google/langextract

## 主な特徴

### 1. 精密なソースグラウンディング
- 抽出されたエンティティを元のテキストの正確な文字位置にマッピング
- 抽出結果の視覚的なトレーサビリティを提供
- インタラクティブなHTML可視化機能

### 2. 柔軟なLLMサポート
- Google Geminiファミリー（推奨）
- OpenAI API
- Ollamaインターフェース経由のローカルモデル
- クラウドベースとオンデバイスの両方に対応

### 3. ドメイン適応性
- 医療、金融、法律、文学など、あらゆるドメインに対応
- モデルのファインチューニング不要
- 少数の例（few-shot）による学習で動作

### 4. 大規模文書処理の最適化
- スマートなチャンキング戦略
- 並列処理機能
- 複数回の抽出パスによる感度向上

## インストール

```bash
# 基本インストール
pip install langextract

# 完全インストール（全依存関係を含む）
pip install langextract[full]

# 開発用（GitHubから）
git clone https://github.com/google/langextract.git
cd langextract
pip install -e ".[dev]"  # 開発ツール付き
pip install -e ".[test]"  # テストツール付き
```

## 使用例

```python
import langextract as lx

# 基本的な抽出
result = lx.extract(
    text_or_documents=input_text,
    prompt_description="Extract characters, emotions, and their relationships",
    examples=[
        # few-shot examples
    ],
    model_id="gemini-2.5-flash"
)

# 結果の保存
lx.io.save_annotated_documents(result, "output.jsonl")

# HTML可視化の生成
lx.visualization.create_visualization("output.jsonl", "visualization.html")
```

## データフォーマット
- JSONL形式を使用（1行1JSONオブジェクト）
- 人間が読みやすく、パース・共有・統合が容易
- 各抽出結果には元テキストへの正確な参照情報を含む

## 主要な使用事例

### 医療分野
- 臨床ノートからの構造化情報抽出
- 薬剤情報（薬品名、用量、投与方法）の抽出
- 放射線レポートの構造化

### その他の応用分野
- 文学テキスト分析（キャラクター、感情、関係性の抽出）
- 法的文書の解析
- 金融レポートの構造化
- エンジニアリング文書の処理

## 技術的な特徴
- Controlled Generation技術による一貫した出力フォーマット
- カスタムスキーマ定義による柔軟な抽出
- LLMの世界知識を活用した抽出の補強

## 注意事項
- Apache-2.0ライセンス
- Googleの公式サポート製品ではない
- 医療用途の例は説明目的のみで、診断や治療には使用不可
- クラウドホスティングモデル（Gemini等）の使用にはAPIキーが必要

## 他のツールとの差別化要因
1. 抽出結果の正確なソースマッピング
2. インタラクティブな可視化機能
3. ドメインに依存しない汎用的な抽出能力
4. モデルの世界知識を活用した補完機能
5. 長文書処理に最適化されたアーキテクチャ