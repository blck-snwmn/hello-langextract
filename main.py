def main():
    import argparse
    import sys
    from pathlib import Path
    import langextract as lx
    import os
    
    # コマンドライン引数のパーサーを設定
    parser = argparse.ArgumentParser(
        description="langextractを使用してテキストファイルから構造化情報を抽出"
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="抽出対象のテキストファイルのパス"
    )
    
    args = parser.parse_args()
    
    # 入力ファイルの存在確認
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"エラー: 入力ファイル '{args.input_file}' が見つかりません。")
        sys.exit(1)
    
    # テキストファイルを読み込む
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            input_text = f.read()
    except Exception as e:
        print(f"エラー: ファイルの読み込みに失敗しました: {e}")
        sys.exit(1)
    
    print(f"入力ファイル: {args.input_file}")
    print(f"テキストの長さ: {len(input_text)} 文字")
    print("-" * 50)
    
    # langextractで抽出を実行
    try:
        print("抽出を開始します...")
        
        # シンプルな英語の例に変更（JSONパースエラーを回避）
        examples = [
            lx.data.ExampleData(
                text="John Smith attended the Tech Conference in Tokyo on January 15, 2023.",
                extractions=[
                    lx.data.Extraction(extraction_class="person", extraction_text="John Smith"),
                    lx.data.Extraction(extraction_class="event", extraction_text="Tech Conference"),
                    lx.data.Extraction(extraction_class="location", extraction_text="Tokyo"),
                    lx.data.Extraction(extraction_class="date", extraction_text="January 15, 2023")
                ]
            )
        ]
        
        result = lx.extract(
            text_or_documents=input_text,
            prompt_description="Extract people, events, locations, and dates from the text.",
            examples=examples,
            model_id="gemini-2.5-flash"
        )
        
        # 結果を保存
        output_file = "output.jsonl"
        lx.io.save_annotated_documents([result], output_file)
        print(f"\n抽出結果を '{output_file}' に保存しました。")
        
        # HTML可視化を生成
        try:
            html_file = "visualization.html"
            # 実際のJSONLファイルパスを指定
            actual_jsonl_path = Path(output_file) / "data.jsonl"
            html_content = lx.visualize(str(actual_jsonl_path))
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"HTML可視化を '{html_file}' に生成しました。")
        except Exception as viz_error:
            print(f"警告: HTML可視化の生成に失敗しました: {viz_error}")
        
        # 抽出結果の簡単なサマリーを表示
        print("\n抽出された情報:")
        print("-" * 50)
        
        # resultは単一のAnnotatedDocumentオブジェクト
        if hasattr(result, 'extractions') and result.extractions:
            for extraction in result.extractions:
                print(f"- {extraction.extraction_class}: {extraction.extraction_text}")
        else:
            print("（抽出された情報はありません）")
        
    except Exception as e:
        print(f"エラー: 抽出処理中にエラーが発生しました: {e}")
        print("\nトラブルシューティング:")
        print("1. GOOGLE_API_KEY が正しく設定されているか確認してください")
        print("2. 入力テキストが長すぎる場合は、短いテキストで試してください")
        print("3. ネットワーク接続を確認してください")
        sys.exit(1)

if __name__ == "__main__":
    main()
