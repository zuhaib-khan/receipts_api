# Receipt Processor API

This is a Python `3.9` app.

## Running via Docker

Build the Docker Image:
```sh
docker build -t receipt-processor .
```

Run the Container:
```sh
docker run -p 5000:5000 receipt-processor
```

The API will be available at [http://localhost:5000](http://localhost:5000)

---

## Running Locally

Create and Activate a Virtual Environment:
```sh
python -m venv .venv
```

Windows:
```sh
.venv\Scripts\activate
```

macOS/Linux:
```sh
source .venv/bin/activate
```

Install Dependencies:
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

Run the Application:
```sh
flask --app=api/app.py run
```

The API will be available at [http://localhost:5000](http://localhost:5000)
