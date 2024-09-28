import os
import json
import sys
from search_utils import filter_and_rank_languages


def get_snippets_dir():
    vscode_snippets_dir = os.environ.get('vscode_snippets_dir')
    if not vscode_snippets_dir:
        raise EnvironmentError("Environment variable 'vscode_snippets_dir' is not set.")
    snippets_dir = os.path.expanduser(vscode_snippets_dir)
    if not os.path.isdir(snippets_dir):
        raise FileNotFoundError(f"Snippets directory does not exist: {snippets_dir}")
    return snippets_dir


def get_user_query():
    return sys.argv[3].strip()


def get_user_action():
    return sys.argv[1].strip()


def get_python_path():
    return sys.argv[2].strip()


def list_snippet_files(snippets_dir):
    return [f for f in os.listdir(snippets_dir) if f.endswith(".json")]


def matches_query(lang_name, query):
    runner = 0
    lang_len = len(lang_name)
    for char in query:
        while runner < lang_len and lang_name[runner] != char:
            runner += 1
        if runner >= lang_len:
            return False
        runner += 1
    return True


def build_item(lang_name, snippets_dir, action, python_path):
    return {
        "title": lang_name,
        "variables": {
            "selected_file_path": os.path.join(snippets_dir, f"{lang_name}.json"),
            "lang": lang_name,
            "action": action,
            "python_path": python_path,
        },
        "icon": {"path": f"src/img/{action}.png"},
    }


def generate_items(files, snippets_dir, query, action, python_path):
    filter_languages = filter_and_rank_languages(files, query)
    items = [build_item(lang, snippets_dir, action, python_path) for lang in filter_languages]
    if not items:
        items.append(
            {"title": "No matches found", "subtitle": "No snippets matched.", "valid": False}
        )
    return items


def main():
    try:
        snippets_dir = get_snippets_dir()
    except (EnvironmentError, FileNotFoundError) as e:
        error_item = {
            "items": [{"title": "Configuration Error", "subtitle": str(e), "valid": False}]
        }
        print(json.dumps(error_item, ensure_ascii=False, indent=2))
        sys.exit(1)
    query = get_user_query()
    action = get_user_action()
    python_path = get_python_path()
    files = list_snippet_files(snippets_dir)
    items = generate_items(files, snippets_dir, query, action, python_path)

    print(json.dumps({"items": items}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
