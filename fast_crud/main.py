from fastapi import FastAPI
import uvicorn
import student
import user
import authentication
import worker
app = FastAPI()
app.include_router(student.router)
app.include_router(user.router)
app.include_router(authentication.router)


@app.get('/task/')
def test_celery():
    result = worker.add.delay()
    print(result.result)
    return { "result": result }


if __name__ == "__main__":
    uvicorn.run(app)
