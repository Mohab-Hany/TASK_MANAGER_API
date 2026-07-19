from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies import get_current_user
from ..models import Task

from ..schemas import (
    TaskCreate,
    TaskUpdate,
    TaskStatus
)


router = APIRouter(

    prefix="/tasks",

    tags=["Tasks"]

)


#==================================
# CREATE TASK
#==================================

@router.post("/")
def create_task(

        task: TaskCreate,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    new_task = Task(

        title=task.title,

        description=task.description,

        priority=task.priority,

        deadline=task.deadline,

        owner_id=user_id

    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


#==================================
# GET ALL TASKS + PAGINATION
#==================================

@router.get("/")
def get_tasks(

        page: int = 1,

        limit: int = 10,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    skip = (page - 1) * limit

    tasks = db.query(
        Task
    ).filter(

        Task.owner_id == user_id

    ).offset(skip).limit(limit).all()

    return tasks


#==================================
# GET TASK BY ID
#==================================

@router.get("/{task_id}")
def get_task(

        task_id: int,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    task = db.query(Task).filter(

        Task.id == task_id,

        Task.owner_id == user_id

    ).first()


    if not task:

        raise HTTPException(

            status_code=404,

            detail="Task Not Found"

        )

    return task


#==================================
# UPDATE TASK
#==================================

@router.put("/{task_id}")
def update_task(

        task_id: int,

        task: TaskUpdate,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    db_task = db.query(Task).filter(

        Task.id == task_id,

        Task.owner_id == user_id

    ).first()


    if not db_task:

        raise HTTPException(

            status_code=404,

            detail="Task Not Found"

        )


    db_task.title = task.title
    db_task.description = task.description
    db_task.priority = task.priority
    db_task.deadline = task.deadline

    db.commit()
    db.refresh(db_task)

    return db_task


#==================================
# DELETE TASK
#==================================

@router.delete("/{task_id}")
def delete_task(

        task_id: int,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    task = db.query(Task).filter(

        Task.id == task_id,

        Task.owner_id == user_id

    ).first()


    if not task:

        raise HTTPException(

            status_code=404,

            detail="Task Not Found"

        )


    db.delete(task)
    db.commit()

    return {

        "message": "Task Deleted Successfully"

    }


#==================================
# UPDATE TASK STATUS
#==================================

@router.patch("/{task_id}/status")
def update_status(

        task_id: int,

        task: TaskStatus,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    db_task = db.query(Task).filter(

        Task.id == task_id,

        Task.owner_id == user_id

    ).first()


    if not db_task:

        raise HTTPException(

            status_code=404,

            detail="Task Not Found"

        )


    db_task.status = task.status

    db.commit()
    db.refresh(db_task)

    return db_task


#==================================
# SEARCH TASKS
#==================================

@router.get("/search/")
def search_tasks(

        title: str,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    return db.query(Task).filter(

        Task.title.contains(title),

        Task.owner_id == user_id

    ).all()


#==================================
# FILTER TASKS
#==================================

@router.get("/filter/")
def filter_tasks(

        priority: str,

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    return db.query(Task).filter(

        Task.priority == priority,

        Task.owner_id == user_id

    ).all()


#==================================
# COMPLETED TASKS
#==================================

@router.get("/completed/")
def completed_tasks(

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    return db.query(Task).filter(

        Task.status == True,

        Task.owner_id == user_id

    ).all()


#==================================
# PENDING TASKS
#==================================

@router.get("/pending/")
def pending_tasks(

        db: Session = Depends(get_db),

        user_id: int = Depends(
            get_current_user
        )

):

    return db.query(Task).filter(

        Task.status == False,

        Task.owner_id == user_id

    ).all()
