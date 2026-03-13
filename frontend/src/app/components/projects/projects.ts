import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth';
import { ProjectService } from '../../services/project';

@Component({
  selector: 'app-projects',
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './projects.html',
  styleUrl: './projects.css'
})
export class ProjectsComponent implements OnInit {
  user: any = null;
  projects: any[] = [];
  users: any[] = [];
  showForm = false;
  editingProject: any = null;
  form = { name: '', description: '', members: [] as number[] };
  error = '';

  constructor(private auth: AuthService, private projectService: ProjectService, private router: Router) {}

  ngOnInit() {
    this.user = this.auth.getCurrentUser();
    this.loadProjects();
    this.auth.getUsers().subscribe(data => this.users = data);
  }

  loadProjects() {
    this.projectService.getProjects().subscribe(data => this.projects = data);
  }

  openForm(project?: any) {
    this.showForm = true;
    if (project) {
      this.editingProject = project;
      this.form = { name: project.name, description: project.description, members: project.members.map((m: any) => m.id) };
    } else {
      this.editingProject = null;
      this.form = { name: '', description: '', members: [] };
    }
  }

  closeForm() { this.showForm = false; this.editingProject = null; }

  onSubmit() {
    if (this.editingProject) {
      this.projectService.updateProject(this.editingProject.id, this.form).subscribe({
        next: () => { this.loadProjects(); this.closeForm(); },
        error: () => this.error = 'Erreur lors de la modification.'
      });
    } else {
      this.projectService.createProject(this.form).subscribe({
        next: () => { this.loadProjects(); this.closeForm(); },
        error: () => this.error = 'Erreur lors de la création.'
      });
    }
  }

  deleteProject(id: number) {
    if (confirm('Supprimer ce projet ?')) {
      this.projectService.deleteProject(id).subscribe(() => this.loadProjects());
    }
  }

  goToTasks(id: number) { this.router.navigate(['/projects', id, 'tasks']); }
  logout() { this.auth.logout(); this.router.navigate(['/login']); }
  isCreator(project: any): boolean { return project.created_by?.username === this.user?.username; }
  toggleMember(userId: number) {
    const idx = this.form.members.indexOf(userId);
    if (idx === -1) this.form.members.push(userId);
    else this.form.members.splice(idx, 1);
  }
  isMemberSelected(userId: number): boolean { return this.form.members.includes(userId); }
}
