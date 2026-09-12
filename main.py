"""API. /search takes structured criteria; /ask takes free text (+ optional sort)."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from matching import Need, find_products
from parse_need import parse_text

app = FastAPI(title="sfatbebe API")

# CORS: allow the frontend to call this API from the browser.
# MVP: "*" (anyone). Once the domain is fixed, replace with ["https://sfatbebe.ro"].
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Ask(BaseModel):
    text: str
    sort: str = "recommended"   # 'recommended' or 'price'


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/search")
def search(need: Need):
    products = find_products(need)
    return {"count": len(products), "products": products}


@app.post("/ask")
def ask(q: Ask):
    """Free text -> criteria (step 1) -> filter + rank (step 2) -> products."""
    need = parse_text(q.text)
    sort = q.sort if q.sort in ("recommended", "price") else "recommended"
    products = find_products(need, sort=sort)
    return {
        "understood": need.model_dump(exclude_none=True),
        "count": len(products),
        "products": products,
    }
