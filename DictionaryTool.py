# Importing 'requests' and 'argparse' libraries.
import requests
import argparse

# Define 'API_URL' and 'API_KEY' of 'Merriam Webster' dictionary.
API_KEY = "1e7bda28-6014-4d0c-9d7f-659086aad543"  
API_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

# Defining the function
def fetch_definition(word, part_of_speech=None):
    # Make a request to the Merriam Webster API
    url = f"{API_URL}{word}?key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        return f"Error making the request: {e}"
    
    # Check if the request was successful and define the exception handling
    if response.status_code == 200:
        try:
            # Parse the JSON response
            definitions = response.json()
        except requests.exceptions.JSONDecodeError:
            return f"Error decoding JSON. Empty or unexpected response for the word: {word}"
        
        # Check if word exists in the Dictionary
        if definitions:
            # Extract and format the first definition
            formatted_definitions = []
            for definition in definitions:
                if part_of_speech and part_of_speech.lower() != definition.get('fl', '').lower():
                    continue  # Skip definitions not matching the specified part of speech
                formatted_definition = f"{word} ({definition.get('fl', 'N/A')}): {definition.get('shortdef', ['No definition'])[0]}"
                formatted_definitions.append(formatted_definition)
            return formatted_definitions if formatted_definitions else [f"No definitions found for the word '{word}' with the specified part of speech."]
        else:
            return f"No definitions found for the word: {word}"
    else:
        return f"Failed to fetch definitions. Status code: {response.status_code}"

# Define 'main' function
def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="Command Line Dictionary Tool")
    
    # Defining arguments for parser object
    parser.add_argument("word", help="The word to fetch the definition for")
    parser.add_argument("--pos", help="Filter definitions by part of speech (e.g., noun, verb, adjective)")

    # Parse the arguments from standard input
    args = parser.parse_args()
    
    # Fetch and print the definition
    results = fetch_definition(args.word, args.pos)
    
    if isinstance(results, list):
        for result in results:
            print(result)
    else:
        print(results)

# Call the 'main' function
if __name__ == "__main__":
    main()
