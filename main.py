from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.routes.chat_router import router as chat_router
from backend.routes.quote_router import router as quote_router
from backend.routes.claim_router import router as claim_router
from backend.routes.dashboard_router import router as dashboard_router
from backend.routes.quotation_router import router as quotation_router
from backend.routes.policy_router import router as policy_router
from backend.routes.analytics_router import router as analytics_router
from backend.routes.admin_chat_router import router as admin_chat_router
from backend.routes.customer_router import router as customer_router
from backend.routes.admin_claim_router import router as admin_claim_router
from backend.routes.auth_router import router as auth_router


app = FastAPI(
    title="ACKO Insurance AI Platform"  
)

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


app.include_router(chat_router)
app.include_router(quote_router)
app.include_router(claim_router)
app.include_router(dashboard_router)
app.include_router(quotation_router)
app.include_router(policy_router)
app.include_router(analytics_router)
app.include_router(admin_chat_router)
app.include_router(customer_router)
app.include_router(admin_claim_router)
app.include_router(auth_router)


@app.get("/test")
def test():
    print("TEST ROUTE CALLED")
    return {"message": "working"}