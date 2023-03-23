# plyway

A database migration tool written in Python and inpsired by Flyway.

## Dev Setup

1. Install [pyenv](https://github.com/pyenv/pyenv)
2. With `pyenv`, install Python 3.11 and setup as your default system version
3. Run `pyenv version` and you should see:
    ```
    3.11.0 (set by /Users/<user>/.pyenv/version)
    ```
4. Run `which python` and you should see the below output (make sure it references `pyenv` so you are using the correct Python installation)
    ```
    /Users/<user>/.pyenv/shims/python
    ```
5. Run `which pip` and you should see the below output (make sure it references `pyenv` so you are using the correct Python installation)
    ```
    /Users/<user>/.pyenv/shims/pip
    ```
6. Clone project locally and run `poetry install`. Poetry will create a virtual env for the project. Virtual environments are just Python's way of splitting up dependencies for different projects
7. Add the below to your vscode `settings.json`:
    ```json
    // Python
    {
        "python.formatting.provider": "black",
        "python.linting.flake8Enabled": true,
        "python.linting.pylintEnabled": false,
        "python.linting.mypyEnabled": true,
        "python.venvFolders": ["/Users/<user>/Library/Caches/pypoetry/virtualenvs"], // Update the path to the correct user
        "python.analysis.indexing": true,
        "python.analysis.autoImportCompletions": true,
        "python.analysis.extraPaths": ["${workspaceRoot}"],
        "python.autoComplete.extraPaths": ["${workspaceRoot}"],
        "[python]": {
            "diffEditor.ignoreTrimWhitespace": false,
            "editor.wordBasedSuggestions": false,
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.fixAll": true, 
                "source.organizeImports": true
            },
            "editor.formatOnType": true
        },
    }
    ```
8. In the VSCode actions look for `Python: Select Interpretor`. Selec this and look for a virtual environment named something like `plyway-<random characters>-py3.11` (you may need to click the little refresh button to see it show up). Select this one so VSCode uses the correct virtual env (you only have to do this once for the project)
9. You can now open a terminal in vscode and it should activate the virtual environment automatically. Otherwise, run `poetry shell` to activate it.
10. You can now run `python -m plyway.main` to kick off the script.


