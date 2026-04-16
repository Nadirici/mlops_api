import pandas as pd
import os
import requests
import dotenv

dotenv.load_dotenv()

path_kedro = r"C:\Users\nadir\Desktop\VsCode\purchase-predict"

dataset = pd.read_csv(os.path.join(path_kedro, r"data\03_primary\primary.csv"))
dataset = dataset.drop(["user_session", "user_id", "purchased"], axis=1)

sample = dataset.sample(n=10).fillna("unknown")

response = requests.post(
    "https://purchase-predict-api-736850329675.us-central1.run.app/predict",
    json=sample.to_dict(orient="records")
)

print(response.status_code)
print(response.text)