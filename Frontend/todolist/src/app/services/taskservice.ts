import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Task } from "../interfaces/task";

@Injectable({
    providedIn: 'root'
})
export class TaskService {
    private tasksURL: string = '/tasks';


    constructor(private http: HttpClient) {}

    getTasks(): Observable<Task[]> {
        return this.http.get<Task[]>(this.tasksURL);
    }
    getTask(id: number): Observable<Task> {
        return this.http.get<Task>(`${this.tasksURL}/${id}`);
    }
    createTask(task: Task): Observable<Task> {
        return this.http.post<Task>(this.tasksURL, task);
    }
    updateTask(task: Task): Observable<Task> {  
        return this.http.put<Task>(`${this.tasksURL}/${task.id}`, task);
    }
    deleteTask(id: number): Observable<void> {
        return this.http.delete<void>(`${this.tasksURL}/${id}`);
    }
}