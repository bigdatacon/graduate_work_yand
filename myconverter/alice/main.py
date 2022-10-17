import phrases
from movies import get_film
from phrases import get_phrase
from fuzzywuzzy import fuzz

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
    "session_id": "7ac4c21e-be2c-4c58-8870-2cc623910d28",
    "skill_id": "60b900ed-90b0-41ab-af3a-b4c9290b8960",
    "user": {
      "user_id": "CAD2EBA89C2756D74ABA199C679A756854EC1A4688FF0BDFC14604E40C3C6CA4"
    },
    "application": {
      "application_id": "16D619CE73E09E2FFE05F73E0FA3F41A8A083810F7802C342F3A558005265C34"
    },
    "new": True,
    "user_id": "16D619CE73E09E2FFE05F73E0FA3F41A8A083810F7802C342F3A558005265C34"
  },
  "request": {
    "command": "в каких фильмах снимался джон траволта",
    "original_utterance": "в каких фильмах снимался Джон Траволта?",
    "nlu": {
      "tokens": [
        "в",
        "каких",
        "фильмах",
        "снимался",
        "джон",
        "траволта"
      ],
      "entities": [
        {
          "type": "YANDEX.FIO",
          "tokens": {
            "start": 4,
            "end": 6
          },
          "value": {
            "first_name": "джон",
            "last_name": "траволта"
          }
        }
      ],
      "intents": {
        "actorm.on": {
          "slots": {
            "what": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 3,
                "end": 4
              },
              "value": "снимался"
            },
            "intro": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 0,
                "end": 2
              },
              "value": "в каких"
            },
            "where": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 2,
                "end": 3
              },
              "value": "фильмах"
            },
            "who": {
              "type": "YANDEX.STRING",
              "tokens": {
                "start": 4,
                "end": 6
              },
              "value": "джон траволта"
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

fake_films_persons_db_full = [
    {'film' : 'зеленая миля', 'rating' : '8.2', 'actor': 'Том Хэнкс', 'genre' : 'драма'},
    {'film' : 'криминальное чтиво', 'rating' : '7.7', 'actor': 'Джон Траволта', 'genre' : 'комедия'},
    {'film' : 'пираты карибского моря', 'rating' : '9.4', 'actor': 'Джони Депп', 'genre' : 'комедия'},
    {'film' : 'страх и ненависть в Лас-Вегасе', 'rating' : '6.5', 'actor': 'Джони Депп', 'genre' : 'комедия'}
]


print(f' eto event : {event}')
intents = event.get("request", {}).get("nlu", {}).get("intents", {})


# print(f' eto intents: {intents}')
# value = intents.get('film.on').get("slots").get('where').get('value')
# print(f' eto value: {value}')
# actor = "Джон Траволта"

#информация по актеру на простой базе
# for k,v in fake_films_persons_db.items():
#     if v==actor:
#         var = k
#         print(f'herre simple {k , var, actor}')


#информация по названию фильма
def find_film_info(input_film: str):
    rating = None
    genre = None
    all = None
    for el in fake_films_persons_db_full:
        for k,v in el.items():
            if k == 'film':
                x = fuzz.WRatio(input_film.lower().replace(' ', ''), v.lower().replace(' ', ''),)
                if x>=90:
                    # print(f'here in full : {input_film} : {k}, {x}, {el}, {el.get("rating")}')
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    return rating, genre, all
    return rating, genre, all

# print(find_film_info(value))

input_actor = intents.get('actorm.on').get("slots").get('who').get('value')
print(f' here input_actor from slots : {input_actor}')

#информация по актеру
def find_film_actor(input_actor: str):
    film_list = []
    all_list = []
    for el in fake_films_persons_db_full:
        for k, v in el.items():
            if k == 'actor':
                x = fuzz.WRatio(input_actor.lower().replace(' ', ''), v.lower().replace(' ', ''), )
                if x >= 90:
                    print(f'here in full actor : {input_actor} : {k}, {x}, {el}, {el.get("rating")}')
                    film = el.get("film")
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    film_list.append(film)
                    all_list.append(el)
    return film_list, all_list

def find_film_actor_match(input_actor: str):
    film_list = []
    all_list = []
    for el in fake_films_persons_db_full:
        for k, v in el.items():
            if k == 'actor':
                if input_actor.lower().replace(' ', '')==v.lower().replace(' ', ''):
                    print(f'here in full actor : {input_actor} : {k},  {el}, {el.get("rating")}')
                    film = el.get("film")
                    rating = el.get("rating")
                    genre = el.get("genre")
                    all = el
                    film_list.append(film)
                    all_list.append(el)
    return film_list[0]

def find_film_rating(input_rating: str):
    film_list = []
    for el in fake_films_persons_db_full:
        if float(el.get('rating')) >=float(input_rating):
            film_list.append(el)
    return film_list


print(f' eto find_film_actor : {find_film_actor(input_actor)}')
print(f' eto find_film_actor_match : {find_film_actor_match(input_actor)}')


def handler(event, context):
    fake_db = {
        "на кухне": "люстра",
        "в коридоре": "лампа"
    }
    fake_films_persons_db = {
        "зеленая миля": "том хэнкс",
        "криминальное чтиво": "джон траволта"
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
        for k, v in fake_films_persons_db.items():
            if k == value:
                text2 = v

    # elif intents.get("actor.on"):
    #     value = intents.get('actor.on').get("slots").get('person').get('value')
    #     for k,v in fake_films_persons_db.items():
    #         if v==value:
    #             text2 = k

    elif intents.get("actorm.on"):
        value = intents.get('actorm.on').get("slots").get('who').get('value')
        text2 = str(find_film_actor_match(value))
    elif intents.get("rating.on"):
        value = intents.get('rating.on').get("slots").get('who').get('value')
        text2 = str(find_film_rating(value))
        # for k,v in fake_films_persons_db.items():
        #     if v==value:
        #         text2 = k

    elif intents.get("turn.on"):
        text = 'том хэнкс turn.on'
        value = intents.get('turn.on').get("slots").get('where').get('value')
        for k, v in fake_db.items():
            if k == value:
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



