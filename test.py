import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Read binary data from the image file
        binary_data = image_file.read()

        # Encode the binary data to Base64
        base64_data = base64.b64encode(binary_data).decode('utf-8')

    return base64_data

# Example usage
image_path = "static/images/rit.jpg"
base64_encoded_image = image_to_base64(image_path)

# Print or use the Base64-encoded image data as needed
print(base64_encoded_image)

def export_to_excel(request):
    # Get all column names from the Personal_Details model
    personal_details_columns = [field.name for field in Personal_Details._meta.get_fields()]

    # Get all column names from Model1, Model2, Model3, and Model4
    model1_columns = [field.name for field in HSC_Marks._meta.get_fields()]
    model2_columns = [field.name for field in Academic_Details._meta.get_fields()]
    model3_columns = [field.name for field in Diplomo._meta.get_fields()]

    # Create a range for iteration in the template
    for_ten = range(1, 11)

    return render(request, 'dashboard/export_page.html', {'all_columns': personal_details_columns, 'for_ten': for_ten})




def export_to_personal_excel(request):
    data = Personal_Details.objects.all().values()  # Query the data you want to export
    df = pd.DataFrame(data)  # Create a DataFrame from the data

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response

def export_to_hsc_excel(request):
    data = Personal_Details.objects.all().values()  # Query the data you want to export
    df = pd.DataFrame(data)  # Create a DataFrame from the data

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response

def export_to_academic_excel(request):
    data = Personal_Details.objects.all().values()  # Query the data you want to export
    df = pd.DataFrame(data)  # Create a DataFrame from the data

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response

def export_to_diploma_excel(request):
    data = Personal_Details.objects.all().values()  # Query the data you want to export
    df = pd.DataFrame(data)  # Create a DataFrame from the data

    # Create a response with Excel content type and set the file name
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response

import pandas as pd

excel_file_path = 'school.xlsx'
    # Read the Excel file
try:
    df = pd.read_excel(excel_file_path)
except pd.errors.EmptyDataError:
        # Handle the case where the Excel file is empty
    df = pd.DataFrame(columns=['name'])

    # Extract school names
school_names = df['name'].tolist()

print(school_names)