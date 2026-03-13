import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class TaskService {
  private apiUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  getTasks(projectId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/projects/${projectId}/tasks/`);
  }

  getTask(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/tasks/${id}/`);
  }

  createTask(projectId: number, data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/projects/${projectId}/tasks/`, data);
  }

  updateTask(id: number, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/tasks/${id}/`, data);
  }

  deleteTask(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/tasks/${id}/`);
  }

  getStatistics(): Observable<any> {
    return this.http.get(`${this.apiUrl}/statistics/`);
  }
}
