from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
from fastapi import Request
from fastapi.templating import Jinja2Templates
app=FastAPI()
# class login(BaseModel):
#     username:str
#     password:str

Jinja2Templates=Jinja2Templates(directory="templates")
@app.post("/login")
async def calling(username:str=Form(),password:str=Form()):
    if username == 'ggbf' and password == 'fgrgr':
        return  ({'username': 'Login successful'})
    else:
        return ({'message': 'Login is not sucessfull.'})

@app.get("/")
async def home(Request:Request):
    Jinja2Templates.TemplateResponse("loginpage.html",{'request':Request})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)