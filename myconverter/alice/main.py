import phrases
from movies import get_film
from phrases import get_phrase

event = {
  "meta": {
    "locale": "ru-RU",
    "timezone": "UTC",
    "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
    "interfaces": {
      "screen": {},
      "payments": {},
      "account_linking": {}
    }
  },
  "session": {
    "message_id": 0,
    "session_id": "7e7a64c5-f49c-45a6-b57c-e99f2342beda",
    "skill_id": "60b900ed-90b0-41ab-af3a-b4c9290b8960",
    "user": {
      "user_id": "CAD2EBA89C2756D74ABA199C679A756854EC1A4688FF0BDFC14604E40C3C6CA4"
    },
    "application": {
      "application_id": "16D619CE73E09E2FFE05F73E0FA3F41A8A083810F7802C342F3A558005265C34"
    },
    "user_id": "16D619CE73E09E2FFE05F73E0FA3F41A8A083810F7802C342F3A558005265C34",
    "new": True
  },
  "request": {
    "command": "кто играл в фильме зеленая миля",
    "original_utterance": "кто играл в фильме зеленая миля",
    "nlu": {
      "tokens": [
        "кто",
        "играл",
        "в",
        "фильме",
        "зеленая",
        "миля"
      ],
      "entities": [],
      "intents": {
        "film.on": {
          "slots": {
            "what": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 3,
                "end": 4
              },
              "value": "фильме"
            },
            "where": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 4,
                "end": 6
              },
              "value": "зеленая миля"
            }
          }
        }
      }
    },
    "markup": {
      "dangerous_context": False
    },
    "type": "SimpleUtterance"
  },
  "state": {
    "session": {},
    "user": {},
    "application": {}
  },
  "version": "1.0"
}

# fake_films_persons_db = {
#     "на кухне" : "люстра",
#     "в коридоре" : "лампа"
# }

fake_films_persons_db = {
    "зеленая миля" : "Том Хэнкс",
    "криминальное чтиво" : "Джон Траволта"
}

print(f' eto event : {event}')
intents = event.get("request", {}).get("nlu", {}).get("intents", {})


print(f' eto intents: {intents}')
value = intents.get('film.on').get("slots").get('where').get('value')
print(f' eto value: {value}')
for k,v in fake_films_persons_db.items():
    if k==value:
        var = v
        print(f'herre {k , var, value}')



def handler(event, context):
    fake_db = {
    "на кухне" : "люстра",
    "в коридоре" : "лампа"
    }
    fake_films_persons_db = {
    "зеленая миля" : "Том Хэнкс",
    "криминальное чтиво" : "Джон Траволта"
    }
    # current_state = event.get("state", {}).get("session", {}).get("current_state", {})
    # last_phrase = event.get("state", {}).get("session", {}).get("last_phrase")


    intents = event.get("request", {}).get("nlu", {}).get("intents", {})
    command = event.get("request", {}).get("command")

    text = get_phrase(phrases.INTRO)
    end_session = "false"

    if intents.get("exit"):
        text = get_phrase(phrases.EXIT)
        end_session = "true"
    elif intents.get("help"):
        text = get_phrase(phrases.HELP)
    elif intents.get("repeat"):
        text = get_phrase(phrases.REPEAT)
    # elif intents.get("film"):
    #     text = get_film(intents.get("film"))
    elif intents.get("film.on"):
        value = intents.get('film.on').get("slots").get('where').get('value')
        for k,v in fake_films_persons_db.items():
            if k==value:
                text2 = v
    elif intents.get("turn.on"):
        text = 'том хэнкс turn.on'
        value = intents.get('turn.on').get("slots").get('where').get('value')
        for k,v in fake_db.items():
            if k==value:
                text2 = v

    elif command:
        text = get_phrase(phrases.UNSUCCESSFUL)

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text2,
            # Don't finish the session after this response.
            'end_session': 'false'
        },
    }

