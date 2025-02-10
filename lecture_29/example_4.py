from fastapi import FastAPI, Depends
from starlette.authentication import (
    AuthenticationBackend,
    SimpleUser,
    AuthCredentials,
    requires,
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import Request

# Custom Authentication Backend
class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request: Request):
        # # Extract the "Authorization" header
        # auth_header = request.headers.get("Authorization")
        # if not auth_header:
        #     return None  # No credentials provided
        #
        # try:
        #     # Assume the header is in the format: "Basic <base64_encoded_credentials>"
        #     scheme, credentials = auth_header.split(" ", 1)
        #     if scheme.lower() != "basic":
        #         raise AuthenticationError("Invalid authentication scheme.")
        #
        #     # Decode credentials (example: "username:password")
        #     import base64
        #     decoded_credentials = base64.b64decode(credentials).decode("utf-8")
        #     username, _, password = decoded_credentials.partition(":")
        #
        #     # Verify credentials (Replace with your logic)
        #     if username == "admin" and password == "password123":
        #         return AuthCredentials(["authenticated"]), SimpleUser(username)
        #
        #     raise AuthenticationError("Invalid username or password.")
        # except Exception as e:
        #     raise AuthenticationError("Invalid authentication header.") from e
        return AuthCredentials(["authenticated"]), SimpleUser("123123username")


# Initialize FastAPI application
app = FastAPI()

# Add Authentication Middleware
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())

# example dependency
async def get_user(request: Request):
    return "userrrrrrrrr"

# Protected route with @requires
@app.get("/protected")
@requires("authenticated")
async def protected_route(request: Request, user: str = Depends(get_user)):
    return {"message": f"Hello, {user}!"}


# Public route
@app.get("/")
async def public_route(request: Request,):
    return {"message": "This is a public endpoint."}


# Another protected route with specific permissions
@app.get("/admin")
@requires("authenticated", status_code=403)
async def admin_route(request: Request, user: SimpleUser = Depends()):
    if user.display_name != "admin":
        return {"error": "Only admin can access this route."}
    return {"message": f"Welcome to the admin panel, {user.display_name}."}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("example_4:app", host="0.0.0.0", port=8001, reload=True)