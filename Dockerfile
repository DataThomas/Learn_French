# app/Dockerfile

FROM python:3.10.12-slim

WORKDIR /TOOLS_DS2

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "project.py", "--server.port=8501", "--server.address=0.0.0.0"]