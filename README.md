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
  "text": "The single greatest Witch Hunt in American history continues. There was no collusion, everybody including the Dems knows there was no collusion, &amp; yet on and on it goes. Russia &amp; the world is laughing at the stupidity they are witnessing. Republicans should finally take control!",
  "created_at": "Wed Jan 10 15:14:15 +0000 2018",
  "id_str": "951109942685126656",
  "text_filtered": "the single greatest witch hunt in american history continues. there was no collusion  everybody including the dems knows there was no collusion   amp  yet on and on it goes. russia  amp  the world is laughing
at the stupidity they are witnessing. republicans should finally take control!",
  "lemma_arr": [
    "single",
    "greatest",
    "witch",
    "hunt",
    "american",
    "history",
    "continues",
    "collusion",
    "everybody",
    "including",
    "dems",
    "know",
    "collusion",
    "amp",
    "go",
    "russia",
    "amp",
    "world",
    "laughing",
    "stupidity",
    "witnessing",
    "republican",
    "finally",
    "control"
  ]
}
```