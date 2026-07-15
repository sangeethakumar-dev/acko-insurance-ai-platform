from fastapi import APIRouter, HTTPException, Query

from backend.management.claim_service import (
    get_all_claim_service,
    get_claim_service,
    search_claim_service,
    update_claim_status_service,
    approve_claim_service,
    reject_claim_service,
    get_claim_images_service,
    get_complete_claim_service,
    delete_claim_service,
    get_pending_claims_service,
    get_approved_claims_service,
    get_rejected_claims_service
)

router = APIRouter(
    prefix="/admin/claims",
    tags=["Admin Claim Management"]
)


@router.get("/")
def get_all_claims():
    try:
        return get_all_claim_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{claim_id}")
def get_claim(claim_id: int):
    try:
        return get_claim_service(claim_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{claim_id}/details")
def get_complete_claim(claim_id: int):
    try:
        return get_complete_claim_service(claim_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/search/")
def search_claims(keyword: str = Query(...)):
    try:
        return search_claim_service(keyword)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{claim_id}/status")
def update_status(claim_id: int, status: str):
    try:
        return update_claim_status_service(claim_id, status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{claim_id}/approve")
def approve_claim(claim_id: int):
    try:
        return approve_claim_service(claim_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{claim_id}/reject")
def reject_claim(claim_id: int):
    try:
        return reject_claim_service(claim_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{claim_id}/images")
def claim_images(claim_id: int):
    try:
        return get_claim_images_service(claim_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/pending")
def pending_claims():
    return get_pending_claims_service()


@router.get("/approved")
def approved_claims():
    return get_approved_claims_service()


@router.get("/rejected")
def rejected_claims():
    return get_rejected_claims_service()


@router.delete("/{claim_id}")
def delete_claim(claim_id: int):
    try:
        return delete_claim_service(claim_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))