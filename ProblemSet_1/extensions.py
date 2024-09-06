extensions = input("File name: ")

if ".gif" in extensions:
    print("image/gif")

elif ".jpg" in extensions or ".jpeg" in extensions:
    print("image/jpeg")

elif ".png" in extensions:
    print("image/png")

elif ".pdf" in extensions:
    print("application/pdf")

elif ".txt" in extensions:
    print ("text/plain")

elif ".zip" in extensions:
    print("application/zip")

else:
    print("application/octet-stream")
