# Nightscout CGM LibreView Uploader

A Python application that fetches glucose data from LibreView and uploads it to Nightscout.

## Overview

This application connects to the LibreView API to retrieve Continuous Glucose Monitoring (CGM) data and automatically uploads it to your Nightscout instance.

## Prerequisites

- Python 3.11 or higher
- Docker (optional)
- A LibreView account
- A Nightscout instance

## Installation

### Using Docker (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/logicielalm/nightscout-cgm-libreview.git
cd nightscout-cgm-libreview
```

2. Build and run the Docker container:
```bash
docker-compose up --build
```

3. Access the application:
```
http://localhost:5000
```

## Configuration

Create a `.env` file in the project root and add your LibreView and Nightscout credentials:

```
LIBREVIEW_EMAIL=your_libreview_email
LIBREVIEW_PASSWORD=your_libreview_password
NIGHTSCOUT_URL=http://your_nightscout_url
NIGHTSCOUT_API_SECRET=your_nightscout_api_secret
```

## Usage

1. Start the application (see [Installation](#installation)).
2. The application will fetch the latest CGM data from LibreView and upload it to Nightscout.
3. Access the web interface at `http://localhost:5000` to monitor the upload status.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.