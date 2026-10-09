from fs_tools import (
    read_file,
    list_files,
    write_file,
    search_in_file,
)

# Create a sample resume.
print(write_file(
    "resumes/sample_resume.txt",
    "John Doe\nPython developer with 4 years of experience.\n"
    "Experience with Django, FastAPI, and PostgreSQL."
))

# List text resumes.
print(list_files("resumes", ".txt"))

# Read the sample resume.
print(read_file("resumes/sample_resume.txt"))

# Search for a keyword.
print(search_in_file(
    "resumes/sample_resume.txt",
    "PYTHON",
))