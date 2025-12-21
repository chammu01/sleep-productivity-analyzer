import pandas as pd
import random

data = []

for i in range(30):
    sleep = round(random.uniform(4, 9), 1)
    screen = round(random.uniform(2, 8), 1)
    caffeine = random.randint(0, 300)
    study = round(random.uniform(1, 6), 1)
    productivity = max(1, min(10, int(sleep + random.uniform(-2, 2))))
    mood = random.choice(["bad", "neutral", "good"])

    data.append([
        f"2025-01-{i+1:02d}",
        sleep, screen, caffeine, study, productivity, mood
    ])

df = pd.DataFrame(data, columns=[
    "date", "sleep_hours", "screen_time_hours",
    "caffeine_mg", "study_hours",
    "productivity_score", "mood"
])

df.to_csv("data/sleep_data.csv", index=False)

