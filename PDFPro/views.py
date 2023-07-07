import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import tabula

@csrf_exempt
def process_pdf(request):
    if request.method == 'POST':
        # Check if the request contains a file
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # Get the uploaded file
        file = request.FILES['file']

        # Read the PDF and extract the tables
        dfs = tabula.read_pdf(file, pages='all')

        # Store table data in a dictionary
        table_data = {}
        for table_number, table_data_df in enumerate(dfs, start=1):
            # Generate the table name
            table_name = f"table{table_number}_page{table_number}"
            
            # Get the table header
            table_header = table_data_df.columns.tolist()

            # Get the rows from the table
            table_rows = table_data_df.values.tolist()

            # Store the table data in the dictionary
            table_data[table_name] = {
                'header': table_header,
                'rows': table_rows
            }

        # Convert table_data dictionary to JSON string
        json_data = json.dumps(table_data)

        # Define the file path where the JSON file will be saved
        file_path = 'databse1.json'

        # Save the JSON data to a file
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)

        # Return a JSON response with a success message
        return JsonResponse({'message': 'PDF processed successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def hello(request):
    return JsonResponse({'message': 'welcome'})
