import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: Album[] = [];
  loading = true;
  error: string | null = null;

  constructor(
    private albumService: AlbumService,
    private router: Router
  ) {
    console.log('📢 AlbumsComponent constructor');
  }

  ngOnInit(): void {
    console.log('📢 AlbumsComponent ngOnInit');
    console.log('📢 AlbumService:', this.albumService);
    this.loadAlbums();
  }

  loadAlbums(): void {
    console.log('📢 loadAlbums() вызван');
    this.loading = true;
    this.error = null;
    
    this.albumService.getAlbums().subscribe({
      next: (data) => {
        console.log('✅ Данные получены:', data);
        console.log('✅ Количество альбомов:', data.length);
        this.albums = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('❌ Ошибка:', err);
        this.error = 'Ошибка загрузки: ' + err.message;
        this.loading = false;
      }
    });
  }

  goToAlbum(id: number): void {
    this.router.navigate(['/albums', id]);
  }

  deleteAlbum(id: number, event: Event): void {
    event.stopPropagation();
    if (confirm('Удалить альбом?')) {
      this.albumService.deleteAlbum(id).subscribe({
        next: () => {
          this.albums = this.albums.filter(a => a.id !== id);
        },
        error: (err) => {
          alert('Ошибка удаления');
        }
      });
    }
  }
}