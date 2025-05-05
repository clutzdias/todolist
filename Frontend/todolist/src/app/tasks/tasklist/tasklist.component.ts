import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
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
    const originalValue = task.completed;
    task.completed = !task.completed;

    const updatedTask: Task = { ...task };

    this.taskService.updateTask(updatedTask).subscribe({
      next: () => {
      
      },
      error: () => {
        task.completed = originalValue;
      }
    });
    
  }


  ngOnInit() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd && this.router.url === '/home') {
        this.getTasks(); // re-busca as tarefas ao voltar
      }
    });
    this.getTasks();
  }

}
