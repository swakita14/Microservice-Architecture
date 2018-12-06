import json 
import requests
import sys
import argparse



def main():
	id = sys.argv
	response = requests.get('https://jsonplaceholder.typicode.com/todos/' + str(id[1]))
	data = response.json()
	print(data)



if __name__ == "__main__":
	main()


