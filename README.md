# FIA Data Center

## Purpose

FIA Data Center is a desktop client-server application for managing a centralized FIA database. The project provides:
- A PyQt6-based GUI client for login, dashboard, data search, and record management.
- Simple socket-based server components that execute SQL queries against a MySQL database.

## Features
- Login and role-based access via `MAIN PROJECT/MAIN.py` GUI.
- Dashboard summaries (persons, contacts, addresses, vehicles, crimes, jail records).
- Search, view, insert, and update records through the GUI.
- Two server processes: one for queries (read) and one for inserts (write).

## Tech stack
- Python 3.10+ (project contains artifacts from CPython 3.12)
- PyQt6 (GUI)
- mysql-connector-python (database access on server)
- Built-in `socket`, `json`, and standard library modules

## Repository layout (important files)
- [FIA DATA CENTER.sql](FIA%20DATA%20CENTER.sql) — SQL schema + seed data for the MySQL database.
- [MAIN PROJECT/MAIN.py](MAIN%20PROJECT/MAIN.py#L1) — GUI client entrypoint.
- [MAIN PROJECT/config.json](MAIN%20PROJECT/config.json#L1) — client-side server IP/ports.
- [Socket/FIA_Server_Run.py](Socket/FIA_Server_Run.py#L1) — server handling read queries.
- [Socket/FIA_Server_Insert.py](Socket/FIA_Server_Insert.py#L1) — server handling inserts/updates.
- [Socket/config.json](Socket/config.json#L1) — server-side DB credentials and ports.

## Prerequisites
- Python 3.10 or newer installed on Windows.
- MySQL server (or compatible) with an accessible user.
- The database defined in `Socket/config.json` (default `FIA_DATA_CENTER`) created and populated using `FIA DATA CENTER.sql`.

## Installation
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install required packages:

```powershell
pip install PyQt6 mysql-connector-python
```

## Configuration
1. Server DB credentials: edit `Socket/config.json` and set `HOST`, `USER`, `PASSWORD`, and `DATABASE` to your MySQL values.
2. Client server IP/ports: `MAIN PROJECT/config.json` contains `IP`, `PORT-1`, and `PORT-2`. The server scripts will set `IP` automatically when started on the server host, but ensure the client `IP` points to the server machine.

## Setup the database
Import the provided SQL file into your MySQL server. Using command-line:

```powershell
mysql -u <user> -p < FIA\ DATA\ CENTER.sql
```

Or use a GUI tool like MySQL Workbench to run the script.

## Running the servers (on server machine)
Start two server processes (they use different ports):

```powershell
python "Socket\FIA_Server_Run.py"
python "Socket\FIA_Server_Insert.py"
```

These scripts listen on the ports specified in `Socket/config.json` and update the `IP` field automatically using the host's local IP.

## Running the client (on any machine with network access to server)
1. Ensure `MAIN PROJECT/config.json` has `IP` set to the server machine IP and the ports match the server config.
2. Run the GUI client:

```powershell
python "MAIN PROJECT\MAIN.py"
```

The login window should appear. Use a seeded user from the SQL file or create an account in the `users` table.

## Notes & troubleshooting
- Communication between client and server uses simple sockets with a length-prefixed JSON protocol. Ensure no firewall is blocking configured ports.
- If you see MySQL connector errors on the server, verify `Socket/config.json` credentials and that the MySQL server is reachable from the server machine.
- The client uses `PyQt6` and expects the `Images/` folder to be present for icons and backgrounds.

## Development tips
- To run the client and server on the same machine during development, set both `Socket/config.json` and `MAIN PROJECT/config.json` to `IP: 127.0.0.1` and use the ports provided.
- Server logs print queries and error messages to the console.

## Contributing
Open an issue or submit a pull request. If you change DB schema, update `FIA DATA CENTER.sql` accordingly.

## License
No license specified. Add a LICENSE file if you wish to open-source this project.
