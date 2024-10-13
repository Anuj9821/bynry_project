# Gas Utility Customer Service Application

## Overview
This is a Django-based web application developed for a gas utility company to handle customer service requests online. The application provides features for customers to submit service requests, track request status, update personal information, and view their account details. The system also provides administrators with tools to manage and resolve customer service requests.

## Features
- **Service Request Submission**: Customers can submit requests for gas services (e.g., installations, repairs, etc.).
- **Request Tracking**: Customers can track the status of their service requests.
- **Service Request Status Updates**: Admins can update the status of customer requests (pending, in-progress, resolved, etc.).
- **File Attachments**: Customers can upload relevant documents or photos with their requests.
- **Search Functionality**: Search for service requests by customer name or phone number.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite for development
- **Containerization**: Docker 

## Installation & Setup

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)
- `virtualenv` for creating isolated Python environments
- Docker (optional, if running in a containerized environment)

### Step-by-Step Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/bynry_project.git
    cd bynry_project
    ```

2. **Create and activate a virtual environment**:
    ```bash
    virtualenv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the app**:
    Open your browser and go to `http://127.0.0.1:8000/gas/submit`.

### Using Docker (Optional)

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/gas_utility_case_study.git
cd gas_utility_case_study
```

2. **Build the Docker image:**
```bash
docker build -t gas_utility_case_study .
```

3.**Run the Docker container:**
```bash
docker run -d -p 8000:8000 gas_utility_case_study
```

5. **Access the app**:
```bash
   Open your browser and go to `http://127.0.0.1:8000/gas/submit`.
   ```

## Routes

- **`submit/`**: Submits a new service request.
- **`request/<int:pk>/`**: Displays the details of a specific service request.
- **`requests/`**: Lists all service requests.
- **`request/<int:pk>/update/`**: Allows customer support to update the status of a specific service request.
- **`search_service_request/`**: Searches for a service request by customer name or phone number.
