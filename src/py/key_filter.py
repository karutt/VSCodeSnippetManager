import os
import json5, json
import sys
from search_utils import filter_and_rank_snippets


def get_selected_file_path():
    file_path = os.environ.get('selected_file_path')
    if not file_path or not os.path.isfile(file_path):
        raise FileNotFoundError("Selected file path is invalid or not found.")
    return file_path


def get_user_query():
    return sys.argv[1].strip().replace(" ", "").lower() if len(sys.argv) > 1 else ""


def read_snippets_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        snippets = json5.load(f)
    return snippets


def build_snippet_item(lang, key, snippet, score):
    body_content = "\n".join(snippet.get("body", []))
    return {
        "title": key,
        "subtitle": snippet.get('prefix', ''),
        "variables": {"lang": lang, "prefix": key, "body_content": body_content},
        "valid": True,
    }


def generate_items(snippets, lang, query):
    ranked_results = filter_and_rank_snippets(snippets, query)
    items = [
        build_snippet_item(lang, key, snippet, score) for key, snippet, score in ranked_results
    ]
    if not items:
        items = [{"title": "No matches found", "subtitle": "No snippets matched.", "valid": False}]
    return items


def main():
    try:
        file_path = get_selected_file_path()
        query = get_user_query()
        snippets = read_snippets_from_file(file_path)
        lang = os.path.splitext(os.path.basename(file_path))[0]
        items = generate_items(snippets, lang, query)
        print(json.dumps({"items": items}, ensure_ascii=False, indent=2))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(
            json.dumps(
                {"items": [{"title": "Error", "subtitle": str(e), "valid": False}]},
                ensure_ascii=False,
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
