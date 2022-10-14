import phrases
# from movies import get_actor, get_director, get_film, get_films, get_person
from phrases import get_phrase
import requests

def handler(event, context):
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
    elif intents.get("film"):
        # text, current_state = get_films(intents.get("films"), current_state)
        text = requests.get(f"http://127.0.0.1:8002/api/v1/alice_api/return_film_data/")

    elif command:
        text = get_phrase(phrases.UNSUCCESSFUL)

    response = {
        "version": event["version"],
        "session": event["session"],
        "response": {"text": text, "end_session": end_session},
        "session_state": {"last_phrase": text.json()},
    }

    return response