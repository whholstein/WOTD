import requests
import json

debug_level = 0

def WOTD():

    url = "https://word-of-the-day2.p.rapidapi.com/word/today"

    headers = {
    'X-RapidAPI-Key': 'db00b3feb4mshacc8ba3511749a7p13af16jsn9919a2c829bf',
    'X-RapidAPI-Host': 'word-of-the-day2.p.rapidapi.com'
    }

    # Enclosing query in a try statement to capture cases where connection fails
    try:
        response = requests.request("GET", url, headers=headers)

    except:
        print("\nERROR:  Problem connecting to server")
        raise NameError('Problem connecting to server')

    else:
        #Response is returned in a mixed list/jason format
        #  Convert to json, and then capture list of dictionaries
        data = json.loads(response.text)
        print(json.dumps(data, indent=4)) if debug_level > 0 else None
        word_dict=data[1]
        word_dict_length = len(word_dict)

        result_string = ""
        for i in range(1, word_dict_length+1):
            entry = data[i]
            if entry['word']!="":
                result_string = (result_string + "Word: " + entry['word'] + "\nMeaning: " + entry['mean'] + "\n")
                if i < word_dict_length:
                    result_string = result_string + "\n"
    return result_string

if __name__ == '__main__':
    results = WOTD()
    print(results)