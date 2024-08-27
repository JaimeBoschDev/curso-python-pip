import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def getlist():
    return[1,2,3]

@app.get("/contact", response_class=HTMLResponse)
def getContact():
    return """
        <h1>Soy la respuesta</h1>
    """

def run():
    store.ConsumeProductos()

if __name__ == '__main__':
    run()


