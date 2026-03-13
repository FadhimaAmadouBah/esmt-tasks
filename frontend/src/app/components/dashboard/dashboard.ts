import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth';
import { ProjectService } from '../../services/project';
import { TaskService } from '../../services/task';

@Component({
  selector: 'app-dashboard',
  imports: [CommonModule, RouterLink],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class DashboardComponent implements OnInit {
  user: any = null;
  projects: any[] = [];
  stats: any = null;

  constructor(
    private auth: AuthService,
    private projectService: ProjectService,
    private taskService: TaskService,
    private router: Router
  ) {}

  ngOnInit() {
    this.user = this.auth.getCurrentUser();
    this.projectService.getProjects().subscribe(data => this.projects = data);
    this.taskService.getStatistics().subscribe(data => this.stats = data);
  }

  logout() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }

  goToProject(id: number) {
    this.router.navigate(['/projects', id, 'tasks']);
  }
}
