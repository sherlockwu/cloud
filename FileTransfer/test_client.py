import jobupload_client

if __name__ == '__main__':
    print("Welcome to the job upload client")
    jobupload_client.upload('-a 1 -b 2 -c 4', '/Users/sherlock/Desktop/test.py')
    print("End")
