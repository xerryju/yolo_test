This project contains the basic skeleton files for a FastAPI endpoint called 'count_people' which runs the YOLO algorithm on any image that counts the number of people there are in the image.

To run:
1. Clone repository
2. Make sure required packages are installed (latest versions are all fine)
3. Run `uvicorn main:app --reload` in terminal
4. Send GET request to http://127.0.0.1:8000/health to ensure service is running
5. Send POST requests to http://127.0.0.1:8000/upload-image to run YOLO algorithm and return number of people*
6. *Currently still debugging implementation

TODO:
- Add more documentation in both code and setup OpenAPI JSON documentation for endpoints
- Reorganize file directory
- Debug YOLO Scalar bug (currently the upload-image endpoint does not work)
- Finish setting up Docker container configuration (not complete)
- Update tests.py to use pytest and implement proper unit testing
