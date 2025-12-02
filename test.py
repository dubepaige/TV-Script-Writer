import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

ban_words = ["hey", "hi", "hello", "how's it going", "how s it going",
             "what's up", "ok", "okay"]

def is_good(line):
    return not any(bw in line for bw in ban_words)

def penalize_similarity(sims, used_indices, penalty=0.40):
    sims = sims.copy()
    for idx in used_indices:
        sims[idx] *= penalty
    return sims

def generate_scene(num_lines=10):
    # start with a random line from the cluster
    idx = np.random.randint(len(topic_df))
    current_line = topic_df.iloc[idx]
    scene = [f"{current_line['speaker']}: {current_line['clean_text']}"]

    current_emb = emb[df.index.get_loc(current_line.name)]
    used = set([df.index.get_loc(current_line.name)])

    for _ in range(num_lines - 1):
        sims = cosine_similarity([current_emb], emb)[0]

        # Diversity penalty
        sims = penalize_similarity(sims, used)

        # consider top 40 candidates
        top_idx = sims.argsort()[-40:][::-1]

        # filter out greetings and fillers
        candidate_indices = [i for i in top_idx if is_good(df.iloc[i]["clean_text"])]

        if len(candidate_indices) == 0:
            candidate_indices = top_idx  # fallback

        next_idx = np.random.choice(candidate_indices)

        next_line = df.iloc[next_idx]
        scene.append(f"{next_line['speaker']}: {next_line['clean_text']}")

        current_emb = emb[next_idx]
        used.add(next_idx)

    return "\n".join(scene)

print(generate_scene(12))
