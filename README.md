# Rytr

Before using the library, create an enviroment variable with your Rytr API KEY.

```bash
Enviroment:
RYTR_API_KEY=XXXX
```

## Install

```bash
pip install rytr
```


## Languages

```python
from rytr.languages import Languages

Languages.list()
>>> {'success': True, 'message': '', 'data': [...]}

Languages.find_by_slug('english')
>>> {'_id': '607adac76f8fe5000c1e636d', 'isDefault': True, 'name': '🇺🇸 English', 'slug': 'english', 'createdAt': '2021-04-17T12:55:35.150Z', 'isNew': False}
```

## Tones
```python
from rytr.tones import Tones

Tones.list()
>>> {'success': True, 'message': '', 'data': [...]}

Tones.find_by_slug('enthusiastic')
>>> {'_id': '6058213830f7b1000c1c4f8e', 'name': 'Enthusiastic', 'slug': 'enthusiastic', 'createdAt': '2021-03-22T04:46:48.471Z', 'isNew': False}
```

## Use-case

```python
from rytr.tones import Tones

UseCases.list()
>>> {'success': True, 'message': '', 'data': [...]}

UseCases.find_by_slug('question-answer-generator')
>>> {'_id': '611e2a98045b460ef10242ce', 'name': 'Question & Answer', 'key': 'questions-generator', ...}

UseCases.get(id="611e2a98045b460ef10242ce")
>>> {'success': True, 'message': '', 'data': {'_id': '611e2a98045b460ef10242ce', 'name': 'Question & Answer', 'slug': 'question-answer-generator' ... }}
```

## Content

```python
from rytr.usecases import UseCases
from rytr.content import Content

usecase = UseCases.get(id="607c7ae91ebe15000cbbc7af")
usecase = usecase["data"]

content = Content.generate(
    user_id=1,
    language_id="607adac76f8fe5000c1e636d",
    tone_id="6058213830f7b1000c1c4f8e",
    usecase_id=usecase["_id"],
    input_contexts={
        usecase["contextInputs"][0]["keyLabel"]: "I'M LOVIN 'IT",
        usecase["contextInputs"][1]["keyLabel"]: "I love the result."
    },
)
```

| Props | Description | Optional |Type|
| --- | --- | --- |--- |
| user_id | Primary key for users database table. As a consumer of Rytr API, they assume you have a product/service with users | no | String|
| language_id | Language ID | no |String |
| tone_id | Tone ID | no | String|
| usecase_id |  Use Case ID | no | String|
| inputContexts | Key/value dictionary | no | Object |
| format | html / text  | yes | String |
| creativityLevel | default / none / low / medium / high / max | yes | String|
| variations | 1 to 3 | yes | String|

