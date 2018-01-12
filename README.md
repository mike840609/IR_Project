# IR_Project


## Requirements
- python > 3.5

##### Virtualenv will isolate your Python setup on a per-project basis.
- Start your virtual environment by running: 
```bash

    win :
    $ python -m venv venv
    $ myvenv\Scripts\activate

    osx : 
    $ python3 -m venv venv
    $ source\myvenv\bin\activate
```

- Installing requirements.txt:
```
pip install -r requirements.txt
python main.py
```

- Json Format :
```
{
  "text": "Thank you @GOPLeader Kevin McCarthy! Couldn\u2019t agree w/you more. TOGETHER, we are #MAGA\ud83c\uddfa\ud83c\uddf8 https://t.co/QaxtqpyXTR",
  "created_at": "Wed Jan 10 03:48:26 +0000 2018",
  "id_str": "950937350003183618",
  "text_filtered": "thank you  gopleader kevin mccarthy! couldn t agree w you more. together  we are  maga   ",
  "lemma_arr": [
    "thank",
    "gopleader",
    "kevin",
    "mccarthy",
    "couldn",
    "t",
    "agree",
    "w",
    "maga"
  ]
}
```