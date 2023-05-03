import pandas as pd
from pyllamacpp.model import Model
from transformers import pipeline
import re

from typing import Optional
import pandas as pd
from pyllamacpp.model import Model



from pyllamacpp.model import Model
import pandas as pd

class GPT4Pandas:
    def __init__(self, 
                model_path, 
                df=None, 
                antiprompts=[
                "#",
                "## Human",
                "## Question",
                "## Human:",
                "## Question:"
                ],
                verbose=False):
        self.model = Model(model_path=model_path)
        self.df = df
        self.verbose = verbose
        self.antiprompts=antiprompts
    def set_dataframe(self, df):
        self.df = df
        
    def ask(self, question, n_predict=50, temp=0.1, top_k=5, top_p=0.98, n_threads=8):
        # Combine the question and dataframe into a single input string
        prompt = f"## Dataframe:\n {self.df.to_string(index=False)}\n## Question:\n{question}\n## Answer:\n"
        output = ""
        for tok in self.model.generate(prompt, n_threads=n_threads, n_predict=n_predict, temp=temp, top_k=top_k, top_p=top_p):
            output += tok
            if any(antiprompt.lower() in output.lower() for antiprompt in self.antiprompts):
                break
            if self.verbose:
                print(tok, end='')
        for antiprompt in self.antiprompts:
            output = output.replace(antiprompt, "")
        return output.strip()
