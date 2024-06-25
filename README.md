---
license: mit
task_categories:
- text-classification
- feature-extraction
- image-feature-extraction
- image-classification
language:
- en
tags:
- not-for-all-audiences
pretty_name: Perfume dataset
size_categories:
- 10K<n<100K
configs:
- config_name: name_perfume
  data_files: perfumes.csv
---


## Perfume dataset, over 26k perfumes

### Dataset Description

RAW Perfume dataset (2024 Year), over 26k perfumes. Images, ingredients, description, etc.

## How to use

```Python
from huggingface_hub import hf_hub_download

# download raw archive file
zip_file = hf_hub_download(
    repo_id='doevent/perfume',
    repo_type='dataset',
    filename='images.zip',
)
```

```Python
import zipfile

# extract files to your directory
dataset_dir = 'images'
os.makedirs(dataset_dir, exist_ok=True)
with zipfile.ZipFile(zip_file, 'r') as zf:
    zf.extractall(dataset_dir)
```

## Dataset Structure

**RAW data: SQLlite, JSON, CSV**

SQL:
```
  id,
  brand TEXT,
  name_perfume TEXT,
  family TEXT,
  subfamily TEXT,
  fragrances TEXT,
  ingredients TEXT,
  origin TEXT,
  gender TEXT,
  years TEXT,
  description TEXT,
  image_name TEXT,
  image_id TEXT
```

JSON:

```JSON
[
[
    {
        "brand": "Fiorucci",
        "name_perfume": "Wallstreet",
        "family": "FLORAL",
        "subfamily": "AMBERY (ORIENTAL)",
        "fragrances": "Floral Amber Fresher",
        "ingredients": [
            "Jasmine",
            "Lemon",
            "Spicy Notes",
            "Gardenia",
            "Rose",
            "Bergamot",
            "Mint",
            "Pepper"
        ],
        "origin": "Brazil",
        "gender": "Male",
        "years": "2015",
        "description": "A modern aroma, ideal for urban men and that highlights their strengths in everyday life.",
        "image_name": "jsunc6exf3hcx3bfbnx0jw5f2s4zske1770lzwplo5hn2v4ky2qh4lxan392-w500-q85.jpg"
    },
]
```

## Dataset Creation

01.05.2024

## Dataset Card Authors

Max Skobeev
[Twitter](https://twitter.com/DoEvent)
[Telegram](https://t.me/neuralpony)