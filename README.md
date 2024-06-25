---
license: mit
task_categories:
- text-classification
- feature-extraction
language:
- en
tags:
- not-for-all-audiences
pretty_name: Perfume dataset
size_categories:
- 10K<n<100K
---


## Perfume dataset, over 26k perfumes

### Dataset Description

Perfume dataset, over 26k perfumes

## How to use

unzip images.zip

## Dataset Structure

**SQLlite and JSON**

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