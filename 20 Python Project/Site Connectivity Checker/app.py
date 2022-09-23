from urllib import response
import urllib.request as urllib

def main (url):
    response = urllib.urlopen(url)
    print("Response Code: " , response.getcode())
    print("Response Code: " + str(response.getcode()))

input_url = input("Supply URL: ")
main(input_url)
