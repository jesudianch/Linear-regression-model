# lilinear-regression-module

# Build the Docker image
docker build -t linear-regression-demo .

# Run the Docker container
docker run -p 8000:8000 linear-regression-demo


```bash
curl -X POST "http://localhost:8000/predict/" \
-H "Content-Type: application/json" \
-d '{
  "data": {
    "Hours Studied": 5,
    "Previous Scores": 70,
    "Extracurricular Activities": "Yes",
    "Sleep Hours": 6,
    "Sample Question Papers Practiced": 3
  }
}'
```


```curl -X POST "http://localhost:8000/predict/" \
-H "Content-Type: application/json" \
-d '{
  "data": {
    "Hours Studied": 5,
    "Previous Scores": 70,
    "Extracurricular Activities": "Yes",
    "Sleep Hours": 6,
    "Sample Question Papers Practiced": 3
  }
}'
```