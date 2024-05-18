import base64

def image_to_string(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file and encode it as base64
        encoded_string = base64.b64encode(image_file.read())
        # Convert the encoded bytes to a string
        image_string = encoded_string.decode('utf-8')
    return image_string
image_path = "profile_images\\2024\\2428002_Father_Profile_Image_2.jpg"
image_string = image_to_string(image_path)
print(image_string)
