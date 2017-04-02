# Try BigQuery Python

## How do I set up my development environment?

This is the process almost from scratch, assuming you're on a Mac and have installed Homebrew already.

1. Install Python: `brew install python3`
2. Upgrade package management tools: `pip3 install --upgrade pip setuptools wheel virtualenv`
4. Prepare to create you virtual environment: `mkdir ~/.virtualenvs`
5. Create your virtual environment: `python3 -m venv ~/.virtualenvs/try-bigquery-python`
6. Activate your virtual environment: `source ~/.virtualenvs/try-bigquery-python/bin/activate`
7. Clone the repository: `git clone git@github.com:yhoiseth/try-bigquery-python.git`
8. Navigate into the project: `cd try-bigquery-python`
9. Install the required packages: `pip install -r requirements.txt`

To _deactivate_ (exit) your virtual environment, use the `deactivate` command.