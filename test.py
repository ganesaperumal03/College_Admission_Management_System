

# # import os

# # old_file_path = 'profile_images/2024/2428001_Father_Profile_Image_Capture.PNG'

# # if old_file_path:
# #     if os.path.exists(old_file_path):
# #         os.remove(old_file_path)



import qrcode

def generate_qr_code(link, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the data (URL) to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)

# Example usage
website_link = 'http://172.16.1.5:9000/image_check'
output_filename = 'qrcode.png'
generate_qr_code(website_link, output_filename)

# from datetime import datetime

# current_year = datetime.now().year
# add_digit = current_year + 1
# count = 5+ 1
# print(f"{current_year}-{add_digit % 100:02d}/{count:03d}") 
