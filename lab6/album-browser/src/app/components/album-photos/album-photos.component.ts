import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumService } from '../../services/album.service';
import { Photo } from '../../models/photo';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  photos: Photo[] = [];
  loading = true;
  error: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumService: AlbumService
  ) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    console.log('Loading photos for album:', id);
    
    this.albumService.getAlbumPhotos(id).subscribe({
      next: (data) => {
        console.log('Photos received:', data);
        
        // Конвертируем http в https для всех фото
        this.photos = data.map(photo => ({
          ...photo,
          thumbnailUrl: photo.thumbnailUrl.replace('http://', 'https://'),
          url: photo.url.replace('http://', 'https://')
        }));
        
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading photos:', error);
        this.error = 'Failed to load photos';
        this.loading = false;
      }
    });
  }

  // ДОБАВЛЯЕМ ЭТОТ МЕТОД
  handleImageError(event: Event): void {
    const imgElement = event.target as HTMLImageElement;
    console.log('Image failed to load:', imgElement.src);
    
    // Скрываем сломанное изображение
    imgElement.style.display = 'none';
    
    // Создаем и показываем fallback
    const container = imgElement.parentElement;
    if (container) {
      // Проверяем, нет ли уже fallback
      let fallback = container.querySelector('.image-fallback');
      if (!fallback) {
        fallback = document.createElement('div');
        fallback.className = 'image-fallback';
        fallback.innerHTML = '📷';
        container.appendChild(fallback);
      }
    }
  }

  goBack() {
    const id = this.route.snapshot.paramMap.get('id');
    this.router.navigate(['/albums', id]);
  }
}