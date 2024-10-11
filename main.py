from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


result_db = [
    {"result_id": 1, "result_title": "Laboratory Activity", "result_desc": "Create Lab Act 2", "is_finished": False}
]


class Result(BaseModel):
    result_title: str
    result_desc: str
    is_finished: bool = False

@app.get("/result/{result_id}")
def get_result(result_id: int):
    result = next((result for result in result_db if result["result_id"] == result_id), None)
    if result:
        return {"status": "ok", "result": result}
    raise HTTPException(status_code=404, detail="Result not found")


@app.post("/result")
def create_result(result: Result):
    new_result_id = (max(result["result_id"] for result in result_db) + 1) if result_db else 1
    new_result = {"result_id": new_result_id, **result.dict()}
    result_db.append(new_result)
    return {"status": "ok", "result": new_result}


@app.patch("/result/{result_id}")
def update_result(result_id: int, updated_result: Result):
    result = next((result for result in result_db if result["result_id"] == result_id), None)
    if result:
        result.update(updated_result.dict())
        return {"status": "ok", "result": result}
    raise HTTPException(status_code=404, detail="Result not found")

@app.delete("/result/{result_id}")
def delete_result(result_id: int):
    result = next((result for result in result_db if result["result_id"] == result_id), None)
    if result:
        result_db.remove(result)
        return {"status": "ok", "result": f"Result {result_id} deleted"}
    raise HTTPException(status_code=404, detail="Result not found")

@app.put("/result/{result_id}")
def replace_result(result_id: int, result: Result):
    result_index = next((i for i, r in enumerate(result_db) if r["result_id"] == result_id), None)
    if result_index is not None:
        updated_result = {"result_id": result_id, **result.dict()}
        result_db[result_index] = updated_result
        return {"status": "ok", "result": updated_result}
    raise HTTPException(status_code=404, detail="Result not found")