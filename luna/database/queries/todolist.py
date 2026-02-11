from enum import Enum
from luna.config.luna_db import todolist_collection
from luna.core.errors_handler import TaskNotExists, TaskExists
from bson import ObjectId

class Status(Enum):
  CREATED = "created"
  PENDING = "pending" 
  COMPLETED = "completed"

class Task:
  @staticmethod
  def find_tasks(id: str=None, *, user_id: int=None) -> list | None:
    if id == None:
      if not user_id:
        raise ValueError("User id is missing!")
      
      task_by_user_id = todolist_collection.find_one({ "user_id": user_id })
      if not task_by_user_id:
        raise TaskNotExists("Tasks not found by this user!")
      
      all_user_tasks = list(todolist_collection.find({ "user_id": user_id }))
      return all_user_tasks
    
    task_by_id = todolist_collection.find_one({ "_id": ObjectId(id.strip()) })

    if not task_by_id:
      raise TaskNotExists("Tasks not found!")
    return task_by_id

  @staticmethod
  def create_task(name: str, description: str, status: Status=Status.CREATED, *, user_id: int) -> None:
    task_exists = todolist_collection.find_one({
      "name": name,
      "user_id": user_id, 
    })

    if task_exists:
      raise TaskExists("Task already exists!")
    
    try:
      todolist_collection.insert_one({ 
        "name": name,
        "description": description,
        "status": status.value,
        "user_id": user_id, 
      })
    except Exception as err:
      print(f"an error ocurred to create the task\n{err}")
    
  @staticmethod 
  def delete_task(task_id: str=None, *, user_id: int) -> None:
    if task_id is None:
      tasks_exists = todolist_collection.find_one({ "user_id": user_id })
      if not tasks_exists:
        raise TaskNotExists("Tasks not found!")
      
      todolist_collection.delete_many({ "user_id": user_id })
      return 
    
    task_exists = todolist_collection.find_one({ "_id": ObjectId(task_id.strip()) })

    if not task_exists:
      raise TaskNotExists("Task doesn't exists!")
    
    try:
      todolist_collection.delete_one({ "_id": ObjectId(task_id.strip()) })
    except Exception as err:
      print(f"an error ocurred to delete the task\n{err}")