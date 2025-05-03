import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { TaskService } from 'src/app/services/taskservice';
import { TaskComponent } from './task.component';

const routes: Routes = [
    {
        path: '',
        component: TaskComponent
    },
    {
        path: 'task',
        loadChildren: '../task/task.module#TaskModule' 
    },
    {
        path: 'task/:id',
        loadChildren: '../task/task.module#TaskModule'
    }
]

@NgModule({
    declarations: [
        TaskComponent
    ],
    imports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(routes)
    ],
    providers: [
        TaskService
    ]
})
export class TaskModule {}