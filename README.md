# GPT4Pandas

GPT4Pandas is a tool that uses the GPT4ALL language model and the Pandas library to answer questions about dataframes. With this tool, you can easily get answers to questions about your dataframes without needing to write any code.

## Installation

To install GPT4ALL Pandas Q&A, you can use pip:
```bash
pip install gpt4all-pandasqa
```

## Usage

To use GPT4ALL Pandas Q&A, you can import the `PandasQA` class and create an instance of it with your dataframe:

```python
import pandas as pd
from gpt4all_pandasqa import PandasQA

df = pd.read_csv('my_data.csv')

pandasqa = PandasQA(df)
```
Once you have an instance of PandasQA, you can ask it questions about your dataframe:

```python
answer = pandasqa.ask('What is the average value of column X?')

print(answer)
```

This will output the answer to your question.

License
GPT4ALL Pandas Q&A is licensed under the Apache License, Version 2.0. See the LICENSE file for more information.
