import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Task } from 'src/app/interfaces/task';
import { TaskService } from 'src/app/services/taskservice';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {
  private createMode: boolean = true;
  public formGroup: FormGroup;
  task: Task | undefined;

  constructor(private route: ActivatedRoute,
              private taskService: TaskService,
              private location: Location,
              private formBuilder: FormBuilder) {
    this.formGroup = this.formBuilder.group({
      title: ['', Validators.compose([Validators.required,
                                      Validators.minLength(3), 
                                      Validators.maxLength(50)])],
      description: ['', Validators.compose([Validators.minLength(3), 
                                            Validators.maxLength(150)])],
      completed: [false]
    });
  }

  getTask(id: string): void {
    this.taskService.getTask(+id)
      .subscribe(task => this.task = task);
  }

  goBack() {
    this.location.back();
  }

  saveTask() {


    if (this.createMode) {
      this.taskService.createTask(this.formGroup.value)
        .subscribe(() => this.goBack());
    } else {
      const formData = {id: this.task?.id, ...this.formGroup.value};  
      this.taskService.updateTask(formData)
        .subscribe(() => this.goBack());
    }
  }

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.getTask(id);
      this.createMode = false;
    } else {
      this.task = undefined;
    }
  }

}

