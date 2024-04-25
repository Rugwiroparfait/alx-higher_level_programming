# Project: ALX Higher Level Programming - Python Network 0

This repository contains scripts and solutions for the Python Network 0 project as part of the ALX Higher Level Programming curriculum.



## Description

This project consists of several Bash and Python scripts aimed at understanding and working with HTTP requests, specifically using cURL and Python's requests library. The tasks involve sending requests, handling responses, setting headers, and exploring various HTTP methods.

## Learning Objectives

Upon completing this project, learners should be able to:

- Understand the basics of HTTP, including URLs, request methods, response codes, headers, and cookies.
- Send HTTP requests using cURL in Bash scripts.
- Send HTTP requests using Python's requests library.
- Handle HTTP responses in Bash and Python scripts.
- Set custom headers in HTTP requests.
- Utilize various HTTP methods such as GET, POST, DELETE, etc.

## Requirements

- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts should be exactly 3 lines long, ending with a new line, and executable.
- Python scripts should adhere to PEP8 style guidelines and be documented properly.
- Quiz questions must be answered without external help.
- Plagiarism is strictly prohibited.
- All scripts should use the specified shebang line and be executed on the appropriate environment.

## Tasks

The following tasks are included in this project:

1. **cURL body size**: Script to display the size of the body of a response from a given URL.
2. **cURL to the end**: Script to display the body of a response from a given URL with a 200 status code.
3. **cURL Method**: Script to send a DELETE request to a given URL and display the body of the response.
4. **cURL only methods**: Script to display all HTTP methods accepted by a server for a given URL.
5. **cURL headers**: Script to send a GET request to a URL with a custom header and display the body of the response.
6. **cURL POST parameters**: Script to send a POST request to a URL with specified parameters and display the body of the response.
7. **Find a peak**: Python function to find a peak in an unsorted list of integers with the lowest complexity.

## Usage

Each script can be executed individually by providing the appropriate arguments as specified in the task descriptions.

Example:
```bash
./0-body_size.sh 0.0.0.0:5000
```

## Files

- `0-body_size.sh`: Bash script for task 0.
- `1-body.sh`: Bash script for task 1.
- `2-delete.sh`: Bash script for task 2.
- `3-methods.sh`: Bash script for task 3.
- `4-header.sh`: Bash script for task 4.
- `5-post_params.sh`: Bash script for task 5.
- `6-peak.py`: Python script containing the function for task 6.
- `6-peak.txt`: Text file containing the complexity analysis for task 6.

## Author

This project is authored by ALX.

## License

This project is licensed under the ALX License.