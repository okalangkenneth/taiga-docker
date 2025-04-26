FROM taigaio/taiga-back:6.7.0

# Fix the parse_header import issue
RUN sed -i 's/from django.http.multipartparser import parse_content_disposition_header as parse_header/from django.http.multipartparser import parse_header/' /taiga-back/taiga/base/api/request.py
