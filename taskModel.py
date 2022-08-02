from datetime import datetime
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "jira_tasks_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    jira_number: Mapped[str]
    status_from: Mapped[str]
    status_to: Mapped[str]
    date_of_status_change: Mapped[datetime]
    orbit_number: Mapped[Optional[int]]
    time_in_status: Mapped[Optional[int]]
    percent_time_status_for_task: Mapped[Optional[float]]
    issue_type: Mapped[Optional[str]]
    team: Mapped[Optional[str]]
    churn: Mapped[bool]
    def __repr__(self) -> str:
        return f"Jira Number(id={self.jira_number!r}, team={self.team!r}, Issue Type={self.issue_type!r})"

