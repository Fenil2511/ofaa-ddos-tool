# OFAA: DDoS Test Tool

## Overview

**OFAA** is a low bandwidth DoS test tool designed to perform HTTP denial-of-service (DoS) attacks on web servers. By maintaining multiple connections open with partial HTTP requests, it aims to exhaust the server's resources and prevent legitimate users from accessing the service.

## Features

- **Customizable Host and Port**: Specify the target host and port for the stress test.
- **Socket Management**: Control the number of sockets used in the attack.
- **Proxy Support**: Optionally use a SOCKS5 proxy to route traffic.
- **Random User-Agent**: Randomize user-agent strings for each request to mimic different clients.
- **HTTPS Support**: Perform attacks over HTTPS connections.
- **Verbose Logging**: Enable detailed logging for debugging and monitoring.

## Requirements

- Python 3.x
- Required libraries:
  - `argparse`
  - `logging`
  - `random`
  - `socket`
  - `ssl` (optional, for HTTPS support)
  - `socks` (optional, for proxy support)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Fenil2511/ofaa-ddos-tool
   cd ofaa-ddos-tool
   ```

2. Install required libraries if needed:
   ```bash
   pip install pysocks  # For SOCKS proxy support
   ```

## Usage

Run the script with the following command-line arguments:

```bash
python ofaa.py <host> [options]
```

### Arguments

- `host`: The target host to perform the stress test on (required).
- `-p`, `--port`: The port of the web server (default: 80).
- `-s`, `--sockets`: The number of sockets to use in the test (default: 150).
- `-v`, `--verbose`: Increases logging verbosity.
- `-ua`, `--randuseragents`: Randomizes user-agents with each request.
- `-x`, `--useproxy`: Use a SOCKS5 proxy for connecting.
  - `--proxy-host`: SOCKS5 proxy host (default: 127.0.0.1).
  - `--proxy-port`: SOCKS5 proxy port (default: 8080).
- `--https`: Use HTTPS for the requests.
- `--sleeptime`: Time to sleep between each header sent (default: 15 seconds).

### Example Command

```bash
python ofaa.py example.com -p 80 -s 200 --randuseragents --useproxy --proxy-host localhost --proxy-port 8080 --https
```

## Important Notes

- This tool is intended for educational purposes and ethical hacking only. Unauthorized use against websites without permission is illegal and unethical.
  
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For any questions or issues, please open an issue in this repository or contact me directly.
