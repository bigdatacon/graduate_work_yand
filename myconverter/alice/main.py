import phrases
from movies import get_film
from phrases import get_phrase


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
    # elif intents.get("film"):
    #     text = get_film(intents.get("film"))
    elif intents.get("film"):
        text = 'том хэнкс'
    elif command:
        text = get_phrase(phrases.UNSUCCESSFUL)

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text,
            # Don't finish the session after this response.
            'end_session': 'false'
        },
    }

