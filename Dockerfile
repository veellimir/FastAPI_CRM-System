FROM python:3.12.7

WORKDIR /crm

RUN pip install --upgrade pip wheel

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]