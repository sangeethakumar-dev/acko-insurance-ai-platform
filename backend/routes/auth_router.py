from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.management.auth_service import (
    register_customer_service,
    customer_login_service,
    admin_login_service
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================================
# REQUEST SCHEMAS
# ==========================================

class RegisterRequest(BaseModel):
    customer_name: str
    email: str
    password: str
    phone: str | None = None
    address: str | None = None


class LoginRequest(BaseModel):
    email: str
    password: str


# ==========================================
# CUSTOMER REGISTER
# ==========================================

@router.post("/register")
def register_customer(request: RegisterRequest):

    try:

        return register_customer_service(
            customer_name=request.customer_name,
            email=request.email,
            password=request.password,
            phone=request.phone,
            address=request.address
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# CUSTOMER LOGIN
# ==========================================

@router.post("/customer/login")
def customer_login(request: LoginRequest):

    try:

        return customer_login_service(
            email=request.email,
            password=request.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# ADMIN LOGIN
# ==========================================

@router.post("/admin/login")
def admin_login(request: LoginRequest):

    try:

        return admin_login_service(
            email=request.email,
            password=request.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )