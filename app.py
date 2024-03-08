from flask import Flask, jsonify
import csv

# Initialize Flask application
app = Flask(__name__)

# Define a route to serve IOCs from a CSV file
@app.route('/api/iocs', methods=['GET'])
def get_iocs():
    # Path to the CSV file - this needs to match the Docker container volume mount
    # and file location. If you change the file name or the mounted directory,
    # you'll need to update this path accordingly.
    csv_file_path = '/data/ioc_md5.csv'  # Variable: Update this path if changed in Docker setup or CSV file name/location changes
    
    iocs = []  # List to hold the IOCs read from the CSV
    
    try:
        # Open the CSV file for reading
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)  # Use DictReader to read CSV into dictionaries
            
            # Loop through rows in the CSV, appending each IOC to the iocs list
            for row in csv_reader:
                iocs.append(row)
                
        # Convert the list of IOCs to JSON and return it
        return jsonify(iocs)
        
    except Exception as e:
        # Return the error as a string with a 500 Internal Server Error status code
        # This could be further customized to handle specific exceptions differently
        return str(e), 500

# Entry point for running the Flask application
if __name__ == '__main__':
    # Running the application with debug=True is useful for development, but
    # it should be set to False in a production environment for security reasons.
    app.run(debug=True)  # Variable: Set debug=False for production use
