# GPT4Pandas

GPT4Pandas is a tool that uses the GPT4ALL language model and the Pandas library to answer questions about dataframes. With this tool, you can easily get answers to questions about your dataframes without needing to write any code.

## Installation

To install GPT4ALL Pandas Q&A, you can use pip:
```bash
pip install gpt4pandas
```

## Usage

To use GPT4ALL Pandas Q&A, you can import the `GPT4Pandas` class and create an instance of it with your dataframe:
```python
import pandas as pd
from gpt4pandas import GPT4Pandas
# Load a sample dataframe
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"],
    "Salary": [50000, 60000, 70000],
}
df = pd.DataFrame(data)

# Initialize the GPT4Pandas model
model_path = <the path to the model file>
gpt = GPT4Pandas(model_path, df, verbose=False)
```

Then ask a question about your dataframe:

```python
# Ask a question about the dataframe
question = "What is the average salary?"
print(question)
answer = gpt.ask(question)
print(answer)  # Output: "mean(Salary)"
```

Here is a complete example that you can also find in examples folder :

```python
import pandas as pd
from gpt4pandas import GPT4Pandas
from pathlib import Path
from tqdm import tqdm
import urllib
import sys

# If there is no model, then download one 
# These models can be automatically downloaded, uncomment the model you want to use
# url = "https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-quantized-ggml.bin"
# url = "https://huggingface.co/ParisNeo/GPT4All/resolve/main/gpt4all-lora-unfiltered-quantized.new.bin"
# url = "https://huggingface.co/eachadea/legacy-ggml-vicuna-7b-4bit/resolve/main/ggml-vicuna-7b-4bit-rev1.bin"
url = "https://huggingface.co/eachadea/ggml-vicuna-13b-4bit/resolve/main/ggml-vicuna-13b-4bit-rev1.bin"
model_name  = url.split("/")[-1]
folder_path = Path("models/")

model_full_path = (folder_path / model_name)

# ++++++++++++++++++++ Model downloading +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Check if file already exists in folder
if model_full_path.exists():
    print("File already exists in folder")
else:
    # Create folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)
    progress_bar = tqdm(total=None, unit="B", unit_scale=True, desc=f"Downloading {url.split('/')[-1]}")
    # Define callback function for urlretrieve
    def report_progress(block_num, block_size, total_size):
        progress_bar.total=total_size
        progress_bar.update(block_size)
    # Download file from URL to folder
    try:
        urllib.request.urlretrieve(url, folder_path / url.split("/")[-1], reporthook=report_progress)
        print("File downloaded successfully!")
    except Exception as e:
        print("Error downloading file:", e)
        sys.exit(1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Load a sample dataframe
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"],
    "Salary": [50000, 60000, 70000],
}
df = pd.DataFrame(data)

# Initialize the GPT4Pandas model
model_path = "models/"+model_name
gpt = GPT4Pandas(model_path, df, verbose=False)

print("Dataframe")
print(df)
# Ask a question about the dataframe
question = "What is the average salary?"
print(question)
answer = gpt.ask(question)
print(answer)  # Output: "mean(Salary)"

# Ask another question
question = "Which person is youngest?"
print(question)
answer = gpt.ask(question)
print(answer)  # Output: "max(Age)"

# Set a new dataframe and ask a question
new_data = {
    "Name": ["David", "Emily"],
    "Age": [40, 45],
    "City": ["Berlin", "Tokyo"],
    "Salary": [80000, 90000],
}
new_df = pd.DataFrame(new_data)
print("Dataframe")
print(new_df)

gpt.set_dataframe(new_df)
question = "What is salary in Tokyo?"
print(question)
answer = gpt.ask(question)
print(answer)  # Output: "min(Salary) where City is Tokyo"
```

This will output the answer to your question.
Here is one of the answers :

```
Dataframe
      Name  Age      City  Salary
0    Alice   25  New York   50000
1      Bob   30     Paris   60000
2  Charlie   35    London   70000
What is the average salary?
The average salary is $60,000.
Which person is youngest?
Alice is the youngest.
Dataframe
    Name  Age    City  Salary
0  David   40  Berlin   80000
1  Emily   45   Tokyo   90000
What is salary in Tokyo?
The salary in Tokyo is $90,000.
```
tested using vcuna 7B model.

# limitations

Please notice that the results depend on the model size, context size and dataframe size. if the dataframe is bigger than the context, you'll have an error.


# License
GPT4ALL Pandas Q&A is licensed under the Apache License, Version 2.0. See the LICENSE file for more information.
