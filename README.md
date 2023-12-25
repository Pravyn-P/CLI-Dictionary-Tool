***************************************************************************************                                      
                      ### Command Line Dictionary Tool ###

        * This project provides a flexible and user-friendly way to interact with the Merriam-Webster Dictionary API from the command line. Users can specify a word and, optionally, a part of speech to filter the definitions.

***************************************************************************************
Table of Contents:
1. Introduction
    1.1 Purpose
    1.2 Features
2. Installation
    2.1 Prerequisites
    2.2 Setup
3. Usage
    3.1 Command Line Arguments
    3.2 Example
4. Implementation Details
    4.1 Dependencies
    4.2 API Key
    4.3 Functionality
5. Dependencies
6. Error Handling
7. Future Enhancements
8. Contribution Guidelines
9. Contact Information
***************************************************************************************


1. Introduction
    1.1 Purpose
        * The purpose of this project is to create a command-line dictionary tool that fetches word definitions using the Merriam-Webster Dictionary API.

    1.2 Features
        * Fetches and displays the definition of a given word.
        * Handles errors gracefully, such as API errors or invalid JSON responses.
        * Provides a user-friendly command-line interface using argparse.

2. Installation
    2.1 Prerequisites
        * Ensure the following prerequisites are met before using the script:
        * Python (version 3.6 or higher): Install the Python and set up the         environment variable. Check python installation status, execute the command ('python --version')
        * Get the Merriam-Webster API_URL and API_Key from https://dictionaryapi.com/. 

    2.2 Setup
        * Ensure that the required dependencies, such as 'requests' and 'argparse' libraries are installed. You can install using 'pip' i.e 'pip install requests' and 'pip install argparse'.

3. Usage
    3.1 Command Line Arguments
        * To use the command-line dictionary tool, run the script with the following command:
            'python script_name.py word_to_define'
        * Replace script_name.py with the actual name of your Python script, and word_to_define with the word for which you want to fetch the definition.
    
    3.2 Example
        * For example if your script_name.py is 'DictionaryTool.py' and the word_to_define is 'Exercise', then use the below command:
            'python DictionaryTool.py Exercise'

4. Code Structure
    * Key components in the code structure are:
        * fetch_definition function: Fetches the word definition from the Merriam-Webster API.
        * main function: Parses command-line arguments and calls fetch_definition.
        * API key and URL definitions.

5. Dependencies
    * Here the 'requests' library is the external dependency, required for the script to run. Used for making HTTP requests.
    * To use the 'Merriam-Webster' dictionay, you need to obtain an API key. Replace the 'API_KEY' variable in the script with your valid key.

6. Error Handling
    * The script handles various error scenarios gracefully, including HTTP request failures, JSON decoding errors, and cases where the word has no definition.

7. Future Enhancements
    * Here are some potential improvements or features that could be added in the future.
        1. Interactive Mode:
            Implement an interactive mode where the user can enter multiple words without restarting the script for each query.
        2. Synonyms and Antonyms:
            Include synonyms and antonyms along with definitions to provide a more comprehensive understanding of the word.
        3. Custom Output Formats:
            Allow users to specify different output formats (e.g., JSON, plain text) for the fetched definitions.
        4. Language Support:
            Extend the script to support multiple languages and dictionaries.
        5. Enhanced CLI Interface:
            Use a more sophisticated command-line interface library (e.g., click) to provide a better user experience.

8. Contribution Guidelines
    * This is an open source project, you can also provide your contributions, including reporting the issues or submiting the pull requests.


9. Contact Information
    * Contact information of the project maintainer or contributor: pravyn.it@gmail.com

***************************************************************************************


***************************************************************************************
                    ### Source Code Explanation ###

    * This Python script is a command-line tool that fetches and displays word definitions using the Merriam-Webster Dictionary API. It has several features, including the ability to filter definitions by part of speech. Below is a breakdown and explanation of the script:

* Explanation:

1. Imports:
    * 'requests' library is used to make HTTP requests to the Merriam-Webster API.
    'argparse' library is used to parse command-line arguments.

2. API Key and URL:
    * 'API_KEY' and 'API_URL' are constants defining the Merriam-Webster API key and URL.
      
3. 'fetch_definition' Function:
    * Makes an HTTP request to the Merriam-Webster API with the specified word and API key.
    * Parses the JSON response and extracts the definitions, filtering by part of speech if specified.
    * Handles errors such as bad responses, JSON decoding errors, and cases where the word has no definition.

4. 'main' Function:
    * Sets up the command line argument parser using 'argparse'.
    * Defines two command-line arguments: the word to fetch the definition for ('word') and an optional part of speech filter ('--pos').
    * Parses the command-line arguments.
    * Calls the 'fetch_definition' function with the specified word and part of speech.
    * Prints the results to the console.

5. Execution:
    * The 'main' function is called when the script is executed.
    * If the script is run from the command line ('python script_name.py ...'), it fetches and displays word definitions based on the provided arguments.
    
***************************************************************************************
