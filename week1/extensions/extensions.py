extensions = input("File name: ").lower().strip().split(".")


if extensions[-1] == "gif":
    print("image/gif")

elif extensions[-1] == "jpg" or extensions[-1] == "jpeg":
    print("image/jpeg")

elif extensions[-1] == "png":
    print("image/png")

elif extensions[-1] == "pdf":
    print("application/pdf")

elif extensions[-1] == "txt":
    print("text/plain")

elif extensions[-1] == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
