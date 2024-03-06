import requests

url = "http://127.0.0.1:8000/search/"
params = {"keyword": "chicken"}

try:
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the JSON response
        data = response.json()
        # Process the response data as needed
        print(data)
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error connecting to the server:", e)
