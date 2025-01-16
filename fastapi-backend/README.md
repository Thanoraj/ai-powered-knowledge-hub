# AI-Powered Knowledge Hub

Repo for AI-Powered Knowledge Hub

Set up configuration

1. Install black formatter extension if not installed.
   https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter

2. Create .env file to store credentials and API keys in backend folder.

3. Setup virtual environment

- Navigate to backend folder
I. Open the editor in fastapi-backend folder

or 

II. Navigate terminal to fastapi-backend folder using below command from root dir
  ```bash
  cd fastapi-backend
  ```

- Use the following command to create a virtual environment:

```bash
python3.12 -m venv venv
```

- Activate virtual environment

I. in unix

```bash
source venv/bin/activate
```

II. in windows

```
./venv/scripts/activate
```

- Install necessary libraries

```bash
pip install -r requirements.txt
```

4. Run code

```bash
fastapi dev app/main.py
```
