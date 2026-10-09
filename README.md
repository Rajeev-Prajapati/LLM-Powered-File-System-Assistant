# LLM-Powered File System Assistant

## 1. Project Overview

The LLM-Powered File System Assistant is a Python application that uses a Large Language Model (LLM) and function calling to perform file-system operations based on natural-language requests.

The assistant can read resume documents, list files, search for keywords, and write summary files using predefined Python tools.

## 2. Features

* Read PDF, TXT, and DOCX resume files.
* List files in a directory and filter by extension.
* Extract file metadata, including name, size, and modification date.
* Search document content using case-insensitive keyword matching.
* Return matching text with surrounding context.
* Create text files and parent directories.
* Use Groq LLM function calling to select tools based on user requests.
* Handle file errors and restrict file access to the project workspace.

## 3. Technologies Used

* Python
* Groq API
* Python Groq SDK
* pypdf
* python-docx
* python-dotenv

## 4. Project Structure

```text
LLM_Projects/
├── fs_tools.py
├── llm_file_assistant.py
├── create_sample_resumes.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── resumes/
└── summaries/
```

The `.env` file is local configuration and must not be committed to Git.

## 5. Prerequisites

* Python 3.9 or later (use a currently supported Python version).
* A Groq account and valid API key.
* Internet access for LLM requests.
* Visual Studio Code or another Python editor (optional).

## 6. Setup Instructions

### Step 1: Clone the repository

```powershell
git clone https://github.com/Rajeev-Prajapati/LLM-Powered-File-System-Assistant.git
cd LLM-Powered-File-System-Assistant
```

Alternatively, open the project folder directly if you already have the source code.

### Step 2: Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own valid key. Never commit `.env` or share the API key.

### Step 5: Create sample resumes

```powershell
python create_sample_resumes.py
```

This creates eight fictional resume files in the `resumes/` directory.

### Step 6: Run the assistant

```powershell
python llm_file_assistant.py
```

Enter a natural-language request at the prompt. Type `exit` to stop the application.

## 7. Example Usage

### List resumes

```text
List all files in the resumes folder.
```

### Search for Python experience

```text
Find resumes mentioning Python experience.
```

### Read and summarize a resume

```text
Read resumes/resume_01_alex.txt and summarize it.
```

### Create a summary file

```text
Create a summary file for resumes/resume_01_alex.txt
at summaries/alex_summary.txt.
```

The assistant should invoke the relevant tools, process their results, and return a response based on those results.

## 8. Available Tools

### read_file(filepath)

Reads a supported PDF, TXT, or DOCX file and returns its extracted content and metadata.

### list_files(directory, extension=None)

Lists files in a directory, optionally filtering by extension.

### write_file(filepath, content)

Writes text content to a file and creates missing parent directories.

### search_in_file(filepath, keyword)

Searches the document content without case sensitivity and returns matching text with context.

## 9. How Tool Calling Works

1. The user enters a natural-language request.
2. The application sends the request and tool schemas to the Groq API.
3. The LLM selects a tool and returns structured arguments.
4. The Python application validates the request and executes the corresponding function.
5. The tool result is sent back to the LLM.
6. The LLM generates a final response.

The LLM requests tools; the Python application executes them.

## 10. Limitations

* Scanned PDFs may require OCR to extract their text.
* PDF extraction quality depends on the document.
* DOCX tables may require additional parsing logic.
* API requests require internet access and valid credentials.
* Tool calls and model responses can be incorrect and should be validated.
* Only supported file types can be read by the provided tools.

## 11. Security

* Keep API keys in `.env`.
* Never commit secrets to Git.
* Restrict file operations to the project workspace.
* Validate tool names and arguments.
* Do not treat document contents as trusted instructions.
* Use fictional resumes for demonstrations.
* Avoid transmitting confidential personal information to an external LLM.

## 12. Future Enhancements

* Add OCR for scanned PDF resumes.
* Extract tables from DOCX files.
* Add unit tests and automated integration tests.
* Add explicit overwrite confirmation.
* Support recursive file listing.
* Add structured logging and improved error reporting.

## 13. Author

Add your name and project submission details here.
