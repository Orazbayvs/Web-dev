import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { Observable, switchMap, of } from 'rxjs';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album$: Observable<Album | null>;
  editedTitle: string = '';

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumService: AlbumService
  ) {
    this.album$ = this.route.paramMap.pipe(
      switchMap(params => {
        const id = Number(params.get('id'));
        return this.albumService.getAlbum(id);
      })
    );
  }

  ngOnInit(): void {
    this.album$.subscribe(album => {
      if (album) {
        this.editedTitle = album.title;
      }
    });
  }

  saveAlbum(): void {
    this.album$.subscribe(originalAlbum => {
      if (originalAlbum && this.editedTitle.trim()) {
        const updatedAlbum: Album = {
          ...originalAlbum,
          title: this.editedTitle.trim()
        };
        
        this.albumService.updateAlbum(updatedAlbum).subscribe({
          next: () => {
            alert('Album updated successfully!');
          },
          error: () => {
            alert('Failed to update album. Please try again.');
          }
        });
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }
}