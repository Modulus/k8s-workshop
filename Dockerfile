FROM python:3.6-alpine3.8 as builder

COPY . .

RUN pip install -r requirements.txt

RUN pelican content


FROM nginx:1.14-alpine

COPY --from=builder /output /usr/share/nginx/html

EXPOSE 80