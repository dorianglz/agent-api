from fastapi import FastAPI
from app.routes.agent_routes import router as agent_router

app = FastAPI(
    title="Agent D API",
    description="API pour générer des idées, contenus, feedbacks via Agent D",
    version="1.0.0"
)

# Inclusion des routes
app.include_router(agent_router)

# Endpoint de test
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Agent D 🚀"}