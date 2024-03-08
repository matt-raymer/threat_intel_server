Threat Intelligence Server

This project is a simple Flask application designed to serve Indicators of Compromise (IOCs) from a CSV file through a RESTful API. It's containerized with Docker for easy deployment and scalability.
Directory Structure

To properly organize your project, follow this structure:

```
/threat_intel_server
├── app.py              # Flask application file
├── Dockerfile          # Dockerfile for building the application container
├── requirements.txt    # Python dependencies
└── data                # Directory for CSV data files
    └── ioc_md5.csv     # Example CSV file containing IOCs
```
Requirements

1. Docker installed on your host machine.
2. Basic knowledge of Docker commands and operations.

Deployment Instructions
1. Prepare the CSV File

Place your IOC data in a CSV file within the data directory. The CSV file should have headers corresponding to the data fields.
2. Build the Docker Image

Navigate to the root directory of the project (threat_intel_server) and run the following command to build the Docker image:

```docker build -t flask-ti-server .```

3. Run the Docker Container

After building the image, run the container with the following command, which mounts the data directory and forwards port 8000:

```docker run -p 8000:8000 -v $(pwd)/data:/data flask-ti-server```

Ensure to replace $(pwd) with the absolute path to the data directory if you're not running the command from the root project directory on Linux or macOS. On Windows, specify the full path manually.
Accessing the Application

Once the application is running, you can access the IOC data through the following API endpoint:

```http://<host_ip>:8000/api/iocs```

Replace ```<host_ip>``` with the IP address of the machine where the Docker container is running. If testing locally, you can use localhost or 127.0.0.1.
Example curl Request

```curl http://localhost:8000/api/iocs```

This command fetches the IOCs from your CSV file and returns them as a JSON response.
Customization and Notes

  CSV File Path: The default path for the CSV file is ```/data/ioc_md5.csv``` inside the Docker container. If you use a different file name or location, update the ```csv_file_path``` variable in ```app.py.```
  
  Security: The Flask debug mode is enabled for development purposes in app.py. For production deployment, set debug=False.
  
  Additional Endpoints: You can expand the Flask application by adding more endpoints in app.py, following the existing pattern for serving data.

Troubleshooting

  File Not Found Errors: Ensure the CSV file exists in the data directory and the Docker volume is mounted correctly.
  Port Conflicts: If port 8000 is already in use on your host machine, you can change the port forwarding in the Docker run command to an available ```port: -p <other_port>:8000.```

For further assistance, consult the Docker and Flask documentation.
