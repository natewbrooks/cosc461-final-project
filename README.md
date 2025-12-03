## Python AI Tutor Setup Guide

This project uses a local Python virtual environment and the Hugging Face Inference API to power an AI-driven Python tutoring system. 

Follow the steps below to configure your environment, install dependencies, and supply your Hugging Face API key.

---

## 1. Create and Activate a Virtual Environment

From the project root:

```bash
python -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

Once activated, your terminal should show `(.venv)` before the prompt.

## 2. Install Required Python Packages

Run:

```bash
pip install -r requirements.txt
```

## 3. Create a Hugging Face API Key

You must generate a **fine-grained API token** with permission to call inference providers.

### Steps:

1. Go to your Hugging Face account:
   [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

2. Click **New token**.

3. Choose **Fine-grained token**.

4. Give it a name (e.g., `deepseek-tutor`).

5. Under permissions, **enable only**:

   * **Make calls to inference providers**

   Do **not** enable any additional scopes.

6. Create the token and copy the generated key.

## 4. Add the API Key to Your `.env` File

In the project root, create a file named:

```
.env
```

Inside it, place your token like this:

```
HF_API_KEY="{your new key}"
```

Make sure there are:

* no extra spaces,
* no trailing quotes,
* and the variable name matches exactly.

Your project will load this value using `python-dotenv`.

## 5. Running the Tutor

From the activated virtual environment:

```bash
python cli.py
```

Example usage:

```
You: Explain what a Python list is.
```

Allow the AI time to respond before exiting the program.
