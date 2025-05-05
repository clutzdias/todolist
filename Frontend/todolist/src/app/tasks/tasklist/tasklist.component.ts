import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { Task } from 'src/app/interfaces/task';
import { TaskService } from 'src/app/services/taskservice';

@Component({
  selector: 'app-tasklist',
  templateUrl: './tasklist.component.html',
  styleUrls: ['./tasklist.component.css']
})
export class TasklistComponent implements OnInit {

  tasks: Task[] = [];

  constructor(private taskService: TaskService,
              private router: Router) { }

  getTasks(): void {
    this.taskService.getTasks()
      .subscribe(tasks => this.tasks = tasks);
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id)
      .subscribe(() => this.getTasks());
  }

  editTask(id: number): void {
    this.router.navigate(['/task', id]);
  }

  onCompletedChange(task: Task) {
    const updatedTask: Task = {...task, completed: !task.completed};
    this.taskService.updateTask(updatedTask).subscribe(() => {
      task.completed = updatedTask.completed; 
    });
    
  }


  ngOnInit() {
    this.getTasks();
  }

}
