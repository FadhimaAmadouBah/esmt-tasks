import { Injectable, PLATFORM_ID, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';
import { isPlatformBrowser } from '@angular/common';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/api';
  private currentUserSubject = new BehaviorSubject<any>(null);
  currentUser$ = this.currentUserSubject.asObservable();
  private isBrowser: boolean;

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) platformId: Object
  ) {
    this.isBrowser = isPlatformBrowser(platformId);
    if (this.isBrowser) {
      const user = localStorage.getItem('user');
      if (user) this.currentUserSubject.next(JSON.parse(user));
    }
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login/`, { username, password }).pipe(
      tap((response: any) => {
        if (this.isBrowser) {
          localStorage.setItem('access_token', response.access);
          localStorage.setItem('refresh_token', response.refresh);
          this.getMe().subscribe(user => {
            localStorage.setItem('user', JSON.stringify(user));
            this.currentUserSubject.next(user);
          });
        }
      })
    );
  }

  register(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register/`, data);
  }

  getMe(): Observable<any> {
    return this.http.get(`${this.apiUrl}/users/me/`);
  }

  getUsers(): Observable<any> {
    return this.http.get(`${this.apiUrl}/users/`);
  }

  logout() {
    if (this.isBrowser) localStorage.clear();
    this.currentUserSubject.next(null);
  }

  isLoggedIn(): boolean {
    if (!this.isBrowser) return false;
    return !!localStorage.getItem('access_token');
  }

  getToken(): string | null {
    if (!this.isBrowser) return null;
    return localStorage.getItem('access_token');
  }

  getCurrentUser(): any {
    return this.currentUserSubject.value;
  }
}
