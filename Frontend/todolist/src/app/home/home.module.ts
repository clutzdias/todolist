import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { TasklistModule } from '../tasks/tasklist/tasklist.module';


const routes: Routes = [
    {
        path: '',
        component: HomeComponent
    }
]

@NgModule({
    declarations: [
        HomeComponent
    ],
    imports: [
        TasklistModule,
        CommonModule,
        RouterModule.forChild(routes)
    ]
})
export class HomeModule {}