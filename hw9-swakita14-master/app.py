import json 
import requests
import time




def main():
	url = 'http://http://0.0.0.0:8080/api/post'
	print('Accessing post on: ' + url)
	while True:
		response = requests.get('http://0.0.0.0:8080/api/post')
		data = response.json()
		print('Version: ' + str(data[0]["version"]))
		if "votes" in data[0]:
			print('votes: ' + str(data[0]["votes"]))
		time.sleep(1)



if __name__ == "__main__":
	main()