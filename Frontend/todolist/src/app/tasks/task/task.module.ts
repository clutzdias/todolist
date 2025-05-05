import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { TaskService } from 'src/app/services/taskservice';
import { TaskComponent } from './task.component';

const routes: Routes = [
    {
        path: '',
        component: TaskComponent
    },

]

@NgModule({
    declarations: [
        TaskComponent
    ],
    imports: [
        CommonModule,
        ReactiveFormsModule,
        RouterModule.forChild(routes)
    ],
    providers: [
        TaskService
    ]
})
export class TaskModule {}