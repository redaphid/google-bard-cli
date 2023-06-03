import requests

def get_bard_response(question):
    """
    Gets a response from the Google Bard API for the given question.

    Args:
        question (str): The question to ask Bard.

    Returns:
        str: The response from Bard.
    """

    url = "https://bard.google.com/v1/query"
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
    }

    response = requests.post(url, headers=headers, data={"query": question})

    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"Error getting response from Bard API: {response.status_code}")

def main():
    """
    Main function.
    """

    question = input("Enter a question: ")

    response = get_bard_response(question)

    print(response)

if __name__ == "__main__":
    main()
