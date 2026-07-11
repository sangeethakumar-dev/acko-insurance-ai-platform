from backend.database.customer_queries import (
    get_all_customers,
    get_customer_by_id,
    search_customers,
    get_customer_policies,
    get_customer_claims,
    get_customer_statistics,
    delete_customer
)


# GET ALL CUSTOMERS

def get_all_customer_service():
    """
    Return all customers.
    """
    return get_all_customers()


# GET CUSTOMER BY ID

def get_customer_service(customer_id):
    """
    Return customer details.
    """

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("Customer not found.")

    return customer


# SEARCH CUSTOMERS

def search_customer_service(keyword):
    """
    Search customers.
    """

    if not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    return search_customers(keyword)


# CUSTOMER POLICIES

def get_customer_policies_service(customer_id):
    """
    Return all policies belonging to a customer.
    """

    return get_customer_policies(customer_id)


# CUSTOMER CLAIMS

def get_customer_claims_service(customer_id):
    """
    Return all claims belonging to a customer.
    """

    return get_customer_claims(customer_id)


# CUSTOMER STATISTICS

def get_customer_statistics_service(customer_id):
    """
    Return customer statistics.
    """

    return get_customer_statistics(customer_id)



# CUSTOMER PROFILE

def get_customer_profile_service(customer_id):
    """
    Return complete customer profile.
    """

    customer = get_customer_by_id(customer_id)

    if customer is None:
        raise ValueError("Customer not found.")

    return {

        "customer": customer,

        "statistics": get_customer_statistics(customer_id),

        "policies": get_customer_policies(customer_id),

        "claims": get_customer_claims(customer_id)

    }



# DELETE CUSTOMER

def delete_customer_service(customer_id):
    """
    Delete customer.
    """

    delete_customer(customer_id)

    return {

        "message": "Customer deleted successfully."

    }