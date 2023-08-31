import requests


image_path = "D:\dog.jpeg"

url = "https://petstore.swagger.io/v2/pet/1/uploadImage"


files = {
    "file": (image_path,open(image_path, "rb"), "image/jpeg")

}
response = requests.post(url, files=files)
if response.status_code == 200:
    print("Image uploaded successfully!")
    print("Response:", response.text)
else:
    print("Image upload failed.")
    print("Response:", response.text)

