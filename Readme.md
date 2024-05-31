Setting up a Python virtual environment on Windows

Create a virtual environment in the .venv folder:
py -m venv .venv

To activate virtual environment:
source .venv/bin/activate

To install required libraries:
pip install -r requirements.txt

Create file called ".env"
If using OpenAI:
Set OPENAI_API_KEY to your API key

To set up vector database:
Save your file in the "content" directory
python dbsetup.py --file_name "file_name"
(Replace "file_name" with the name of your file)

