from datetime import date

from fastapi import APIRouter, HTTPException, Query

from backend.management.quotation_service import (
    get_all_quotation_service,
    get_quotation_service,
    search_quotation_service,
    update_quotation_status_service,
    delete_quotation_service,
    convert_quotation_to_policy_service,
    approve_quotation_service,
    reject_quotation_service,
    mark_as_bought_service
)

router = APIRouter(
    prefix="/quotations",
    tags=["Quotation Management"]
)


# GET ALL QUOTATIONS

@router.get("/")
def get_all_quotations():

    try:
        return get_all_quotation_service()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# GET QUOTATION BY ID

@router.get("/{quotation_id}")
def get_quotation(quotation_id: int):

    try:
        return get_quotation_service(quotation_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# SEARCH QUOTATIONS

@router.get("/search/")
def search_quotations(
    keyword: str = Query(...)
):

    try:
        return search_quotation_service(keyword)

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


# UPDATE STATUS

@router.put("/{quotation_id}/status")
def update_status(
    quotation_id: int,
    status: str
):

    try:
        return update_quotation_status_service(
            quotation_id,
            status
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


# APPROVE QUOTATION

@router.put("/{quotation_id}/approve")
def approve_quotation(
    quotation_id: int
):

    try:
        return approve_quotation_service(
            quotation_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# REJECT QUOTATION

@router.put("/{quotation_id}/reject")
def reject_quotation(
    quotation_id: int
):

    try:
        return reject_quotation_service(
            quotation_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# MARK AS BOUGHT

@router.put("/{quotation_id}/bought")
def mark_as_bought(
    quotation_id: int
):

    try:
        return mark_as_bought_service(
            quotation_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# CONVERT TO POLICY

@router.post("/{quotation_id}/convert-policy")
def convert_to_policy(
    quotation_id: int,
    policy_number: str,
    start_date: date,
    expiry_date: date
):

    try:

        return convert_quotation_to_policy_service(
            quotation_id,
            policy_number,
            start_date,
            expiry_date
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# DELETE QUOTATION

@router.delete("/{quotation_id}")
def delete_quotation(
    quotation_id: int
):

    try:

        return delete_quotation_service(
            quotation_id
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )