from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK
from app.api.dependencies.database import get_repository
from app.api.dependencies.service import get_service
from app.services.users import UsersService
from app.models.analytic_segment import AnalyticSegment
from app.schemas.analytic_segment import AnalyticSegmentResponse
from app.utils import ERROR_RESPONSES, handle_result
from app.api.dependencies.auth import get_current_user_auth
from app.database.repositories.users import UsersRepository

router = APIRouter()


@router.get(
    "/{analytic_segment_id}",
    status_code=HTTP_200_OK,
    response_model=AnalyticSegmentResponse,
    responses=ERROR_RESPONSES,
    name="user:info-by-id",
)
async def read_user_by_id(
    *,
    analytic_segment_id: AnalyticSegment = Depends(get_current_user_auth()),
    users_service: UsersService = Depends(get_service(UsersService)),
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
    user_id: int,
) -> AnalyticSegmentResponse:
    result = await users_service.get_user_by_id(users_repo=users_repo, user_id=user_id)

    return await handle_result(result)
