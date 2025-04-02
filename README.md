# Hadoop installation and configuration using Ansible

## Overview

Apache Hadoop is used to process and analyze large datasets. This project provides an easy way to deploy a Hadoop cluster using Ansible. Also, it includes Python notebooks for running Hadoop jobs.

## Project Structure

- **Configuration Files:** Adjust settings including formatting for the NameNode and startup configuration for the NameNode and DataNode.
- **Environment Variables:** Set Hadoop’s runtime parameters.


## Key Features

- **Scalability:** Distribute workloads across multiple nodes for vast data processing.
- **Fault Tolerance:** Utilize Hadoop’s built-in redundancy and error recovery mechanisms.
- **Flexibility:** Integrate custom processing logic and third-party tools.
- **Automation:** Use provided scripts and configuration to deploy and run Hadoop jobs effortlessly.

## Prerequisites

Before running the project, make sure you have:

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (includes Docker Compose)
- Sufficient system resources (at least 4GB of RAM recommended)

## Setup Instructions

1. **Clone the Repository:**
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hiltonmbr/bigdata-hadoop.git
   ```

2. **Review Configurations:**
   Check and update configuration files and environment variables as needed for your setup.

3. **Start the Cluster:**
   Launch your Hadoop cluster using Docker Compose:

   ```bash
   docker compose up -d
   ```

4. **Verify Services:**
   Once started, check the status of all containers:
   ```bash
   docker compose ps
   ```

## Stopping the Cluster

To stop the Hadoop cluster, run:

```bash
docker compose down
```

## Accessing the Services

- **NameNode Web UI:** Open [http://localhost:9870](http://localhost:9870)
- **Code-Server (Python Notebooks for Hadoop jobs):** Open [http://localhost:8443](http://localhost:8443)

## Troubleshooting

- **Cluster Not Starting:**

  - Ensure Docker Desktop is running.
  - Inspect container logs for errors:
    ```bash
    docker compose logs
    ```

- **Service Access Issues:**
  - Verify that no firewall or network settings are blocking the required ports.
  - Confirm that all containers are running using:
    ```bash
    docker compose ps
    ```

## Usage Example with Code-Server

After setting up the environment:

1. Copy the notebook file `example.ipynb` to the shared workspace folder `./code-server/workspace/example.ipynb`.

2. - Press `Ctrl + Shift + P` to open the command palette.

- Type "Python: Create a virtual environment" and select the option "Python: Create a virtual environment".
- Select the option "Create a .venv in the current workspace" and press Enter.
- Select the option "Python 3.12" and press Enter.
- Wait for the virtual environment to be created.

3. Open the notebook (`example.ipynb`) in your code-server interface to start working with Hadoop jobs.

4. Select Kernel and install suggested extensions `Python` and `Jupyter`.

5. Select Kernel again and create a Python Virtual Environment (`.venv`).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements, bug fixes, or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Apache Hadoop community for providing a robust data processing framework.
- Special thanks to contributors and maintainers for their support and development efforts.
