from enum import Enum
from luna.config.luna_db import todolist_collection
from luna.core.errors_handler import TaskExists

class Status(Enum):
  CREATED = 1
  PENDING = 1 
  COMPLETED = 1 

class Task:
  def __init__(self, name: str, description: str, status: Status=Status.CREATED):
    self.__name = name 
    self.__description = description 
    self.__status = status
  
  def create_task(self, user_id: int) -> bool:
    task_exists = todolist_collection.find_one({
      "name": self.__name,
      "user_id": user_id, 
    })

    if task_exists:
      raise TaskExists("Essa tarefa já existe!")
    
    try:
      todolist_collection.insert_one({ 
        "name": self.__name,
        "description": self.__description,
        "status": "created",
        "user_id": user_id, 
      })
      
      return True 
    except Exception as err:
      print(f"an error ocurred to create the task\n{err}")
      return False 
    