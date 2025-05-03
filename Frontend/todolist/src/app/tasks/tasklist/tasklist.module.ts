import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { TasklistComponent } from './tasklist.component';
import { TaskService } from 'src/app/services/taskservice';

const routes: Routes = [
    {
        path: '',
        component: TasklistComponent
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
        TasklistComponent
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
export class TasklistModule {}