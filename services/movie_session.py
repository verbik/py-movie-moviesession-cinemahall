from datetime import datetime
from typing import Optional
from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date is not None:
        queryset = queryset.filter(
            show_time__date=session_date
        )
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time

    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    if movie_id is not None:
        movie_session.movie_id = movie_id

    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    return get_movie_session_by_id(session_id).delete()
