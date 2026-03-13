import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-register',
  imports: [FormsModule, CommonModule, RouterLink],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class RegisterComponent {
  username = '';
  email = '';
  password = '';
  role = 'etudiant';
  error = '';
  loading = false;

  constructor(private auth: AuthService, private router: Router) {}

  onSubmit() {
    this.loading = true;
    this.error = '';
    this.auth.register({ username: this.username, email: this.email, password: this.password, role: this.role }).subscribe({
      next: () => {
        this.auth.login(this.username, this.password).subscribe({
          next: () => setTimeout(() => this.router.navigate(['/dashboard']), 500),
          error: () => this.router.navigate(['/login'])
        });
      },
      error: () => {
        this.error = 'Erreur lors de l\'inscription.';
        this.loading = false;
      }
    });
  }
}
