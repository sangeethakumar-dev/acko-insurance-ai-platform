from backend.database.auth_queries import (
    register_customer,
    customer_login,
    admin_login,
    customer_email_exists
)


# ==========================================
# CUSTOMER REGISTER
# ==========================================

def register_customer_service(
    customer_name,
    email,
    password,
    phone,
    address
):
    """
    Register a new customer.
    """

    if customer_email_exists(email):
        raise ValueError("Email already registered.")

    customer_id = register_customer(
        customer_name,
        email,
        password,
        phone,
        address
    )

    return {
        "message": "Customer registered successfully.",
        "customer_id": customer_id
    }


# ==========================================
# CUSTOMER LOGIN
# ==========================================

def customer_login_service(
    email,
    password
):
    """
    Customer login.
    """

    customer = customer_login(
        email,
        password
    )

    if customer is None:
        raise ValueError("Invalid email or password.")

    return {
        "message": "Login successful.",
        "customer_id": customer[0],
        "customer_name": customer[1],
        "email": customer[2]
    }


# ==========================================
# ADMIN LOGIN
# ==========================================

def admin_login_service(
    email,
    password
):
    """
    Admin login.
    """

    admin = admin_login(
        email,
        password
    )

    if admin is None:
        raise ValueError("Invalid admin credentials.")

    return {
        "message": "Admin login successful.",
        "admin_id": admin[0],
        "admin_name": admin[1],
        "email": admin[2]
    }