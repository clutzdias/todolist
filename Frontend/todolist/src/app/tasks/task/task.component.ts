import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Task } from 'src/app/interfaces/task';
import { TaskService } from 'src/app/services/taskservice';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  task: Task | undefined;

  constructor(private route: ActivatedRoute,
              private taskService: TaskService,
              private location: Location) { }

  getTask(id: string): void {
    this.taskService.getTask(+id)
      .subscribe(task => this.task = task);
  }

  goBack() {
    this.location.back();
  }

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.getTask(id);
    } else {
      this.task = undefined;
    }
  }

}
