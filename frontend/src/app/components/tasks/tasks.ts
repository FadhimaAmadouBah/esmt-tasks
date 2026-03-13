import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { ProjectService } from '../../services/project';
import { TaskService } from '../../services/task';

@Component({
  selector: 'app-tasks',
  imports: [CommonModule, FormsModule],
  templateUrl: './tasks.html',
  styleUrl: './tasks.css'
})
export class TasksComponent implements OnInit {
  user: any = null;
  project: any = null;
  tasks: any[] = [];
  filteredTasks: any[] = [];
  users: any[] = [];
  showForm = false;
  editingTask: any = null;
  statusFilter = '';
  userFilter = '';
  form: any = { title: '', description: '', assigned_to: null, status: 'a_faire', priority: 'normale', due_date: '' };
  error = '';
  projectId!: number;

  constructor(
    private auth: AuthService,
    private projectService: ProjectService,
    private taskService: TaskService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.user = this.auth.getCurrentUser();
    this.projectId = +this.route.snapshot.paramMap.get('id')!;
    this.projectService.getProject(this.projectId).subscribe(data => this.project = data);
    this.loadTasks();
    this.auth.getUsers().subscribe(data => {
      if (this.user?.role === 'etudiant') {
        this.users = data.filter((u: any) => u.role === 'etudiant');
      } else {
        this.users = data;
      }
    });
  }

  loadTasks() {
    this.taskService.getTasks(this.projectId).subscribe(data => {
      this.tasks = data;
      this.applyFilters();
    });
  }

  applyFilters() {
    this.filteredTasks = this.tasks.filter(task => {
      const statusOk = !this.statusFilter || task.status === this.statusFilter;
      const userOk = !this.userFilter || task.assigned_to === +this.userFilter;
      return statusOk && userOk;
    });
  }

  openForm(task?: any) {
    this.showForm = true;
    if (task) {
      this.editingTask = task;
      this.form = { ...task, due_date: task.due_date ? task.due_date.slice(0, 16) : '' };
    } else {
      this.editingTask = null;
      this.form = { title: '', description: '', assigned_to: null, status: 'a_faire', priority: 'normale', due_date: '' };
    }
  }

  closeForm() {
    this.showForm = false;
    this.editingTask = null;
  }

  onSubmit() {
    if (this.editingTask) {
      this.taskService.updateTask(this.editingTask.id, this.form).subscribe({
        next: () => { this.loadTasks(); this.closeForm(); },
        error: () => { this.error = 'Erreur lors de la modification.'; }
      });
    } else {
      this.taskService.createTask(this.projectId, this.form).subscribe({
        next: () => { this.loadTasks(); this.closeForm(); },
        error: () => { this.error = 'Erreur lors de la création.'; }
      });
    }
  }

  deleteTask(id: number) {
    if (confirm('Supprimer cette tâche ?')) {
      this.taskService.deleteTask(id).subscribe(() => this.loadTasks());
    }
  }

  isCreator(): boolean {
    return this.project?.created_by?.username === this.user?.username;
  }

  canEdit(task: any): boolean {
    return this.isCreator() || task.assigned_to === this.user?.id;
  }

  getStatusLabel(status: string): string {
    const labels: any = { 'a_faire': 'À faire', 'en_cours': 'En cours', 'termine': 'Terminé' };
    return labels[status] || status;
  }

  getUserName(userId: number): string {
    const user = this.users.find(u => u.id === userId);
    return user ? user.username : '';
  }

  logout() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }
}
