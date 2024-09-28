import os
import json5
import json
import sys


def log(message):
    sys.stderr.write(f"{message}\n")


def load_snippets(file_path):
    if not os.path.isfile(file_path):
        log(f"Snippet file '{file_path}' does not exist.")
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            snippets = json5.load(f)
        log(f"Loaded snippets from '{file_path}'.")
        return snippets
    except json5.JSONDecodeError as e:
        log(f"Failed to decode JSON from '{file_path}': {e}")
        return {}


def save_snippets(file_path, snippets):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(snippets, f, indent=4, ensure_ascii=False)
        log(f"Saved snippets to '{file_path}'.")
    except Exception as e:
        log(f"Failed to save snippets to '{file_path}': {e}")


def create_snippet(lang, prefix, code, vscode_snippets_dir):
    output_file = os.path.expanduser(f"{vscode_snippets_dir}/{lang}.json")
    body = code.splitlines()
    new_snippet = {prefix: {"prefix": prefix, "body": body, "description": ""}}

    snippets = load_snippets(output_file)
    if not snippets:
        snippets = {}

    if prefix in snippets:
        log(f"Snippet with prefix '{prefix}' already exists. Use update operation instead.")
        return

    snippets.update(new_snippet)
    save_snippets(output_file, snippets)

    log(f"Snippet '{prefix}' added successfully to '{output_file}'.")


def read_snippets(lang, prefix, vscode_snippets_dir):
    output_file = os.path.expanduser(f"{vscode_snippets_dir}/{lang}.json")
    snippets = load_snippets(output_file)

    if prefix not in snippets:
        log(f"Snippet with prefix '{prefix}' not found in '{output_file}'.")
        return

    body_content = "\n".join(snippets[prefix].get("body", []))
    sys.stdout.write(body_content)


def update_snippet(lang, prefix, code, vscode_snippets_dir):
    output_file = os.path.expanduser(f"{vscode_snippets_dir}/{lang}.json")
    body = code.splitlines()

    snippets = load_snippets(output_file)
    if prefix not in snippets:
        log(f"Snippet with prefix '{prefix}' not found in '{output_file}'. Cannot update.")
        return

    snippets[prefix]["body"] = body
    snippets[prefix]["description"] = snippets[prefix].get("description", "")

    save_snippets(output_file, snippets)

    log(f"Snippet '{prefix}' updated successfully in '{output_file}'.")


def delete_snippet(lang, prefix, vscode_snippets_dir):
    output_file = os.path.expanduser(f"{vscode_snippets_dir}/{lang}.json")

    snippets = load_snippets(output_file)
    if prefix not in snippets:
        log(f"Snippet with prefix '{prefix}' not found in '{output_file}'. Cannot delete.")
        return

    del snippets[prefix]
    save_snippets(output_file, snippets)

    log(f"Snippet '{prefix}' deleted successfully from '{output_file}'.")


def main():
    action = os.environ.get('action')
    lang = os.environ.get('lang')
    prefix = os.environ.get('prefix')
    code = os.environ.get('code')
    vscode_snippets_dir = os.environ.get('vscode_snippets_dir')

    log(f"Action: {action}")
    log(f"Language: {lang}")
    log(f"Prefix: {prefix}")
    log(f"Code: {code}")
    log(f"VSCode Snippets Directory: {vscode_snippets_dir}")

    if not action:
        log("No action specified.")
        sys.exit(1)

    if not lang:
        log("No language specified.")
        sys.exit(1)

    action = action.lower()
    if action == 'create':
        if not prefix or not code:
            log("Create operation requires 'prefix' and 'code'.")
            sys.exit(1)
        create_snippet(lang, prefix, code, vscode_snippets_dir)

    elif action == 'read':
        if not prefix:
            log("Read operation requires 'prefix'.")
            sys.exit(1)
        read_snippets(lang, prefix, vscode_snippets_dir)

    elif action == 'update':
        if not prefix or not code:
            log("Update operation requires 'prefix' and 'code'.")
            sys.exit(1)
        update_snippet(lang, prefix, code, vscode_snippets_dir)

    elif action == 'delete':
        if not prefix:
            log("Delete operation requires 'prefix'.")
            sys.exit(1)
        delete_snippet(lang, prefix, vscode_snippets_dir)

    else:
        log(f"Invalid action '{action}'. Supported actions are: create, read, update, delete.")
        sys.exit(1)


if __name__ == "__main__":
    main()
