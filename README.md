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

- Install `sshpass``

  - On Linux distros and Windows WSL:

   ```bash
   sudo apt update && apt install sshpass -y
   ```

- On Mac OSX:

   ```bash
   # install homebrew
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install sshpass
   ```
- Install Python 3.6+

## Setup Instructions

1. **Clone the Repository:**
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/hiltonmbr/hadoop-ansible.git
   ```

2. **Review Configurations:**
   Check and update configuration files and environment variables as needed for your setup.

3. **Start the Cluster:**
   Install Ansible:
   ```bash
   pip3 install ansible
   ```

## Accessing the Services

- **NameNode Web UI:** Open [http://localhost:9870](http://localhost:9870)
- **Code-Server (Python Notebooks for Hadoop jobs):** Open [http://localhost:8443](http://localhost:8443)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements, bug fixes, or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Apache Hadoop community for providing a robust data processing framework.
- Special thanks to contributors and maintainers for their support and development efforts.
