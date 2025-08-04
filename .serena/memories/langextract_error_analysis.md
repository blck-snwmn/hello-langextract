# langextract「This is a continuation of the previous conversation」エラー分析

## 調査結果

### 1. extract関数の実装構造

langextract.extract関数は以下の流れで動作する：

1. **プロンプトテンプレート構築** (`prompting.py`)
   - `PromptTemplateStructured`クラスでプロンプトを管理
   - `QAPromptGenerator`クラスでQ&A形式のプロンプトを生成
   - デフォルトのプレフィックス：
     - `question_prefix: str = "Q: "`
     - `answer_prefix: str = "A: "`

2. **プロンプト生成ロジック** (`prompting.py` line 143-166)
```python
def render(self, question: str, additional_context: str | None = None) -> str:
    prompt_lines: list[str] = [f"{self.template.description}\n"]
    
    if additional_context:
        prompt_lines.append(f"{additional_context}\n")
    
    if self.template.examples:
        prompt_lines.append(self.examples_heading)
        for ex in self.template.examples:
            prompt_lines.append(self.format_example_as_text(ex))
    
    prompt_lines.append(f"{self.question_prefix}{question}")
    prompt_lines.append(self.answer_prefix)
    return "\n".join(prompt_lines)
```

3. **LLMへのAPI呼び出し** (`inference.py`)
   - GeminiLanguageModelクラスがGemini APIを呼び出し
   - `contents=prompt`として直接プロンプト文字列を送信

### 2. エラーの原因分析

「This is a continuation of the previous conversation」エラーの原因：

#### A. プロンプト構造の問題
Q&A形式のプロンプトが会話の継続と誤認される：
```
<description>

Examples
Q: <example_text>
A: <example_output>

Q: <actual_input_text>
A: 
```

#### B. Gemini APIの解釈
- Gemini APIは`contents`パラメータを会話として解釈
- Q&A形式の構造により、既存の会話の継続として認識される
- 特に複数のQ&Aペアがある場合に発生しやすい

#### C. API呼び出し実装
```python
response = self._client.models.generate_content(
    model=self.model_id, 
    contents=prompt,  # ←ここが問題
    config=config
)
```

### 3. 対処法の提案

#### Option 1: システムメッセージとユーザーメッセージの分離
```python
# 現在の実装
contents=prompt

# 改善案
contents=[
    {"role": "system", "parts": [system_part]},
    {"role": "user", "parts": [user_part]}
]
```

#### Option 2: プロンプト構造の変更
Q&A形式を避けて、より直接的な指示形式に変更

#### Option 3: 会話履歴のクリア
新しいリクエストごとに会話状態をリセット

### 4. 影響範囲
- few-shot examples（examples）が多いほど発生しやすい
- プロンプトが長いほど発生しやすい
- 特に日本語コンテンツで発生する可能性が高い

### 5. 関連ファイル
- `/langextract/__init__.py` (lines 59-259): extract関数の本体
- `/langextract/prompting.py` (lines 143-166): プロンプト生成ロジック
- `/langextract/inference.py` (lines 310-330): Gemini API呼び出し
- `/langextract/annotation.py` (lines 284-291): バッチプロンプト作成