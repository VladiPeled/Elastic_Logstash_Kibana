FROM python:3.8-rc-stretch

COPY demo.py /app/demo.py
RUN touch /app/global.log

WORKDIR /app
CMD ["python", "demo.py"]