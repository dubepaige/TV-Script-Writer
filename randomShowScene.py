import pandas as pd
import numpy as np
import re
'''
This file comes up with a random sample of 10 lines of a scene from the actual show. 
it's meant to match format of model output (no punctuation, uppercase, or characters outside main 6)
Made for testing whether or not model outputs are indistinguishable from actual show scenes.
'''

# load data
df = pd.read_csv("friends_transcripts.tsv", sep="\t")

main_cast = {
    "Monica Geller",
    "Ross Geller",
    "Rachel Green",
    "Chandler Bing",
    "Joey Tribbiani",
    "Phoebe Buffay"
}

# filter to only main cast
df_main = df[df["speaker"].isin(main_cast)].copy()

df_main = df_main.sort_values(
    ["season_id", "episode_id", "scene_id", "utterance_id"]
).reset_index(drop=True)

def clean_text(t):
    t = str(t).lower()
    t = re.sub(r"[^a-zA-Z\s]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

def get_random_10_lines_main_cast():
    start = np.random.randint(0, len(df_main) - 10)

    # get 10 consecutive lines
    sample = df_main.iloc[start:start+10]

    # print clean
    for _, row in sample.iterrows():
        print(f"{row['speaker']}: {clean_text(row['transcript'])}")


get_random_10_lines_main_cast()