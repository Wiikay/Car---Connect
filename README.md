# Car Connect

Car Connect is an intelligent automotive assistant web application that helps users with car-related questions and needs.

## Overview

This project implements a conversational AI interface using Google's Dialogflow to provide automotive assistance through a clean, responsive web interface. The application is built with Flask and can be deployed to cloud platforms.

## Features

- **Car Maintenance Advice**: Get expert guidance on maintaining your vehicle
- **Troubleshooting Assistance**: Identify common car problems and get solutions
- **Service Scheduling Information**: Access information about service scheduling

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Conversational AI**: Google Dialogflow
- **Deployment**: Compatible with cloud platforms that support Flask applications

## Project Structure

- `index.html` - The main web interface
- `main.py` - Flask application for serving the web interface
- `requirements.txt` - Python dependencies

## Getting Started

### Prerequisites

- Python 3.8+
- Pip package manager

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Wiikay/Car---Connect.git
   cd Car---Connect
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:8080`

## Deployment

The application is configured to be deployed to cloud platforms. The port is configurable via the PORT environment variable.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
