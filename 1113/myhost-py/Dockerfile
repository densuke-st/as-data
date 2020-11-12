FROM python:3-slim
ADD src /work
WORKDIR /work
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "myname.py"]