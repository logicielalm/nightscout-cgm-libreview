# python-project

## Overview
This project is a Python package designed to interact with the Nightscout API, allowing users to send glucose data to a Nightscout server.

## Structure
The project consists of the following files and directories:

- `src/`: Contains the source code for the Nightscout package.
  - `nightscout/`: The main package directory.
    - `__init__.py`: Initializes the `nightscout` package.
    - `nightscout_client.py`: Contains the `NightscoutClient` class for sending glucose data.
    - `glucose_data.py`: Defines the `GlucoseData` class representing glucose data structure.
- `requirements.txt`: Lists the dependencies required for the project.
- `setup.py`: Used for packaging the project and includes metadata.

## Installation
To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage
To use the `NightscoutClient`, import it from the `nightscout` package and create an instance with the Nightscout URL and API secret. Use the provided methods to send glucose data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.