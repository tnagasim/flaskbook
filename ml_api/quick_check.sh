#! /bin/sh
curl http://127.0.0.1:5000/v1/probabilities -X POST -H "Content-Type: application/json" -d '{"file_id": "dummy"}'
curl http://127.0.0.1:5000/v1/check-schema -X POST -H "Content-Type: application/json" -d '{"file_id": 1, "file_name": "handwriting"}'
curl http://127.0.0.1:5000/v1/check-schema -X POST -H "Content-Type: application/json" -d '{"file_id": 1, "file_name": 12345}'
