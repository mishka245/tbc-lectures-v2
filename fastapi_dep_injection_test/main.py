from fastapi import FastAPI, Request, Depends, HTTPException

app = FastAPI()

# First-level dependency: Extract all cookies from the request
def extract_cookies(request: Request):
    return request.cookies

# Second-level dependency: Extract `ajs_anonymous_id` from cookies
def get_ajs_anonymous_id(cookies: dict = Depends(extract_cookies)) -> str | None:
    # Look for `ajs_anonymous_id` in the cookies
    ajs_anonymous_id = cookies.get("ajs_anonymous_id")
    if ajs_anonymous_id is None:
        raise HTTPException(status_code=400, detail="Cookie 'ajs_anonymous_id' not found")
    return ajs_anonymous_id

# Endpoint: Demonstrate nested dependency injection
@app.get("/ajs-id")
def get_ajs_id_endpoint(ajs_id: str = Depends(get_ajs_anonymous_id)):
    return {"ajs_anonymous_id": ajs_id}
