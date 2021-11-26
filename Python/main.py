from recommendation.recommendation_system import RecSystem

from fastapi import FastAPI
from typing import List

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_recommendations(p):
    rec_sys = RecSystem()
    rec_sys.process(p)

    recommendations = rec_sys.get_recommendations()
    return recommendations


@app.post("/getRecs")
async def getRec(inputs: List[str]):
    print(inputs)
    recs = get_recommendations(inputs)
    return list(zip(recs['Brand'], recs['Variety'], recs['Style'], recs['Country']))
