# VSCodeSnippetManager

[GitHub Repository](https://github.com/karutt/VSCodeSnippetManager)  
Easily manage your Visual Studio Code (VSCode) snippets directly from Alfred without having to switch between apps. With this workflow, you can seamlessly create, read, update, and delete your snippets without leaving Alfred.

## Features

-   **CRUD Operations**: Manage VSCode snippets through simple commands that enable you to create, read, update, and delete snippets effortlessly.
-   **Clipboard Integration**: Quickly register text from your clipboard as a VSCode snippet.
-   **Customizable Keywords**: The default keywords are `snc` (Create), `snr` (Read), `snu` (Update), and `snd` (Delete), but you can easily modify them through the Configuration Builder to suit your preference.

> **Note**: This workflow directly manipulates the JSON files of your VSCode snippets. Any comments in these files will be removed when the workflow modifies them. If you want to preserve comments, consider adding them as JSON elements or refrain from using this workflow.

## Installation

1. Download the workflow:
    - [GitHub Releases](https://github.com/karutt/VSCodeSnippetManager/releases/tag/alfred)
2. Double-click the downloaded workflow file and follow the prompts to install it in Alfred.
3. **Configure Environment Variables (if needed)**:
    - **VSCode Snippet Directory**:
        - Ensure that the environment variable `vscode_snippets_dir` points to your VSCode snippets directory.
        - By default, this path is set to:
            ```
            ~/Library/Application Support/Code/User/snippets/
            ```
        - If the default path does not work for your setup, find your own VSCode snippets directory and update the environment variable accordingly.

## Usage

Follow these steps to perform basic operations:

1. **Input Keywords**:

    - Open Alfred and type the default keywords (`snc`, `snr`, `snu`, `snd`), followed by a space and the language of your snippet.
    - Example: `snc python` (Create a Python snippet)

2. **Select the Language**:
    - After typing the keyword and a space, choose the programming language for which you want to manage snippets.

### 1. Create Snippet

-   **Steps**:
    1. Copy the code you want to register as a snippet to your clipboard.
    2. Open Alfred, type the keyword `snc` followed by the language, and choose the language from the suggestions.
    3. Enter the prefix for the snippet.
    4. The script will register the clipboard content as a new snippet in VSCode.

### 2. Read Snippet

-   **Steps**:
    1. Open Alfred, type the keyword `snr` followed by the language, and choose the language from the suggestions.
    2. Select the snippet prefix from the list to read its content.
    3. The selected snippet will be copied to your clipboard, and if a text editor is active, it will be pasted automatically.

### 3. Update Snippet

-   **Steps**:
    1. Copy the updated code to your clipboard.
    2. Open Alfred, type the keyword `snu` followed by the language, and choose the language from the suggestions.
    3. Select the prefix of the snippet you want to update.
    4. The existing snippet will be updated with the new clipboard content.

### 4. Delete Snippet

-   **Steps**:
    1. Open Alfred, type the keyword `snd` followed by the language, and choose the language from the suggestions.
    2. Select the prefix of the snippet you want to delete.
    3. The script will remove the selected snippet from your VSCode snippet file.

## Troubleshooting

-   **Snippet is not being registered**:

    -   Make sure that the `vscode_snippets_dir` environment variable is set correctly.
    -   Verify that you have read/write permissions for the snippet directory.

-   **Alfred is not responding**:

    -   Restart Alfred to ensure it has loaded the workflow correctly.
    -   Check that the workflow is enabled in Alfred's settings.

-   **Still having issues?**:
    -   Use the workflow's debug mode to see detailed script outputs.
    -   Based on the debug information, you can take the appropriate action or reach out with a comment if you need further assistance.
