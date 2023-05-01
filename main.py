"""
    File to run main app
"""


from rest_api import app
import uvicorn


if __name__ == "__main__":
    uvicorn.run(app)

