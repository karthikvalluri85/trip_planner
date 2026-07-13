# trip_planner
A multi-agent travel agent using LangGraph

## How to run?

### 1. Create the virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment (Windows / PowerShell)

From the project root (`C:\projects_de\trip_planner`), run:

```powershell
.venv\Scripts\Activate.ps1
```

> **Note:** In PowerShell the activation script is `Activate.ps1` — not the bare
> `activate` file (that one is for bash/cmd). PowerShell also won't run a script
> from the current folder without a path prefix, so if you're already inside
> `.venv\Scripts` use `.\Activate.ps1` instead.

If you get a **"running scripts is disabled on this system"** error, allow signed
scripts for your user account (no admin rights needed) and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

When activation succeeds, your prompt is prefixed with `(.venv)`. To leave the
environment later, run `deactivate`.

### 3. Create and isntall requirments.txt file

```bash
pip install -r requirements.txt
```
